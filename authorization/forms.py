from django import forms
from django.contrib.auth.models import User
from messager.forms import PlaceholderForm
from django.contrib.auth.forms import UserCreationForm
import re


class UserCreationPlaceholderForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationPlaceholderForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.help_text


class LoginForm(PlaceholderForm):

    username = forms.CharField(min_length=5, max_length=20,
                               help_text='Username')
    password = forms.CharField(min_length=6, max_length=20,
                               help_text='Password',
                               widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise forms.ValidationError('Invalid password')
        else:
            raise forms.ValidationError('This username not found')


class RegisterForm(UserCreationPlaceholderForm):
    username = forms.CharField(min_length=5, max_length=20,
                               help_text='Username')
    email = forms.EmailField(help_text='Email')
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=6,
                                max_length=20, help_text='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=6,
                                max_length=20, help_text='Confirm password')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_username(self):
        data = self.cleaned_data['username']
        pattern = re.compile("[A-Za-z0-9]+")
        if pattern.fullmatch(data) is None:
            raise forms.ValidationError("Username must not contain special characters")
        return data
