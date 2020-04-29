from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)


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
    year = models.DateField(null=True)
    mileage = models.IntegerField()
    engine_volume = models.FloatField()
    phone_number = models.CharField(max_length=19)

    def __str__(self):
        return self.name_model

    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])
