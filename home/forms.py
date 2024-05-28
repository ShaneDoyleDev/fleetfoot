from django import forms


class LoginForm(forms.Form):
    """
    A form for user login.

    This form is used to authenticate users by validating their username and password.
    """
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    remember_me = forms.BooleanField(required=False)
