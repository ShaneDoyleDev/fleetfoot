from django import forms
from .models import Product, Department, Brand, ShoeType
from .models import ProductStock, Size


class ProductForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    shoe_type = forms.ModelChoiceField(queryset=ShoeType.objects.all())

    class Meta:
        model = Product
        fields = ['sku', 'name', 'description', 'department', 'brand',
                  'shoe_type', 'list_price', 'on_sale', 'sale_percentage', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        department = Department.objects.all()
        names = [(dept.id, dept.name) for dept in department]
        self.fields['department'].choices = names

        brand = Brand.objects.all()
        names = [(brn.id, brn.name) for brn in brand]
        self.fields['brand'].choices = names

        shoe_type = ShoeType.objects.all()
        names = [(shoe.id, shoe.name) for shoe in shoe_type]
        self.fields['shoe_type'].choices = names

    def clean(self):
        cleaned_data = super().clean()
        on_sale = cleaned_data.get('on_sale')
        sale_percentage = cleaned_data.get('sale_percentage')

        if on_sale and sale_percentage is None:
            self.add_error(
                'sale_percentage', 'Sale percentage is required when product is on sale.')

        return cleaned_data
