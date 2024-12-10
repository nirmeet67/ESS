from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    # You can customize the form fields here if needed
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your password'}))