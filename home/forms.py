from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    """
    A form for user registration.

    This form is used to authenticate users by validating their username and password.
    """

    def __init__(self, *args, **kwargs):
        # sets the global label_suffix to an empty string
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)


class LoginForm(forms.Form):
    """
    A form for user login.

    This form is used to authenticate users by validating their username and password.
    """
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    remember_me = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        # sets the global label_suffix to an empty string
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
