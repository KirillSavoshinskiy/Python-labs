from multiprocessing.pool import ThreadPool

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)


class Mail(models.Model):
    email_caption = models.CharField('Заголовок сообщения', max_length=100)
    email_text = models.TextField('Текст сообщения')
    email_date = models.DateField('Время отправки')
    email_time = models.TimeField()
    resp = models.ManyToManyField(Profile, limit_choices_to={'verified': True}, blank=True)
    check_send = models.BooleanField(default=False)

    def __str__(self):
        if not self.check_send:
            self.check_send = True
            self.send()
            self.save()
        return str(self.email_caption)

    def send(self):
        mess = render_to_string('carSale/email.html', {
            'email_text': self.email_text,
            'email_date': self.email_date,
            'email_time': self.email_time
        })

        email_caption = self.email_caption
        mount = self.resp.count()
        pool = ThreadPool(mount)
        result = []
        for profile in self.resp.all():
            to_email = profile.user.email
            email = EmailMessage(email_caption, mess, to=[to_email])
            result.append(email)
        pool.map(send_mail, result)


def send_mail(email):
    email.send()


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
