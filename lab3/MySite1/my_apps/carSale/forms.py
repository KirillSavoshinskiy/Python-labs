from django import forms
from django.forms import ModelForm

from my_apps.carSale.models import Car


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailInput()


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class UserCreationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailInput()
