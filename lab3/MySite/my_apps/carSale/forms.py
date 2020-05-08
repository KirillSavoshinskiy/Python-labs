from django import forms
from django.contrib.auth.models import User
from MySite import settings
from my_apps.carSale.models import Car, Profile, Company, EngineType, BodyType


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    email = forms.CharField(label='Введи email', required=True)
    first_name = forms.CharField(label='Введите ваше имя', required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def check(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class CarForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), label='Выберите марку авто', required=True)
    name_model = forms.CharField(max_length=30, label='Название модели', required=True)
    engine = forms.ModelChoiceField(queryset=EngineType.objects.all(), label='Выберите тип двигателя', required=True)
    body = forms.ModelChoiceField(queryset=BodyType.objects.all(), label='Выберите тип кузова', required=True)
    description = forms.CharField(label='Описание авто', widget=forms.Textarea, required=True)
    price = forms.IntegerField(label='Цена(в $)', required=True)
    year = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, label='Год выпуска', required=True,
                           widget=forms.NumberInput)
    mileage = forms.IntegerField(label='Пробег авто', required=True)
    engine_volume = forms.FloatField(label='Объём двигателя', required=True)
    phone_number = forms.CharField(label='Номер телефона продавца', required=True)

    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('created_by',)
