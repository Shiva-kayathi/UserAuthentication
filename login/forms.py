from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model, logout
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name')
    password = forms.CharField(widget=forms.PasswordInput, label = 'Password')

    class Meta:
        fields = ['username', 'password']