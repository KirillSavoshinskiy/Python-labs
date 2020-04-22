from django.db import models
from django.forms import ModelForm
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class EngineType(models.Model):
    types = (('Бензин', 'Бензин'), ('Дизель', 'Дизель'), ('Электро', 'Электро'), ('None', 'None'))
    engine_type = models.CharField(max_length=20, choices=types, blank=True, default='N')

    def __str__(self):
        return self.engine_type


class BodyType(models.Model):
    types = (
        ('Седан', 'Седан'), ('Универсал', 'Универсал'), ('Внедорожник', 'Внедорожник'), ('Кроссовер', 'Кроссовер'),
        ('Хэтчбэк', 'Хэтчбэк'), ('None', 'None'))
    body_type = models.CharField(max_length=20, choices=types, blank=True, default='N')

    def __str__(self):
        return self.body_type


class Car(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    name_model = models.CharField(max_length=30, null=True)
    engine = models.ForeignKey(EngineType, on_delete=models.CASCADE, null=True)
    body = models.ForeignKey(BodyType, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name_model

    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])


