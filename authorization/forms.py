from django import forms
from django.contrib.auth.models import User
from messager.forms import PlaceholderForm
import re


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


class RegisterForm(PlaceholderForm):
    username = forms.CharField(min_length=5, max_length=20,
                               help_text='Username')
    email = forms.EmailField(help_text='Email')
    password = forms.CharField(widget=forms.PasswordInput, min_length=6,
                               max_length=20, help_text='Password')
    confirm = forms.CharField(widget=forms.PasswordInput, min_length=6,
                              max_length=20, help_text='Confirm password')

    def clean_username(self):
        data = self.cleaned_data['username']
        if len(User.objects.filter(username=data)):
            raise forms.ValidationError("This username is already exist.")
        pattern = re.compile("[A-Za-z0-9]+")
        if pattern.fullmatch(data) is None:
            raise forms.ValidationError("Username must not contain special characters")
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        if len(User.objects.filter(email=data)):
            raise forms.ValidationError("This email is already exist.")
        return data

    def clean_password(self):
        data = self.cleaned_data['password']
        pattern = re.compile("[A-Za-z0-9]+")
        if pattern.fullmatch(data) is None:
            raise forms.ValidationError("Password must not contain special characters")
        return data

    def clean(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            confirm = self.cleaned_data['confirm']
            if password != confirm:
                raise forms.ValidationError("Password does not match.")

    def save(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.objects.create_user(username, email, password)
        return user
