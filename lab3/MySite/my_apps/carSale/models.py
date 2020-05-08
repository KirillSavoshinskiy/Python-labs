from multiprocessing.pool import ThreadPool

from django.core.mail import EmailMessage
from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)


class Mail(models.Model):
    email_caption = models.CharField('Заголовок сообщения', max_length=100)
    email_text = models.TextField('Текст сообщения', null=True)
    email_date = models.DateField('Время отправки', null=True)
    email_time = models.TimeField(null=True)
    resp = models.ManyToManyField(Profile, limit_choices_to={'verified': True})

    def __str__(self):
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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Выберите марку авто', blank=False)
    name_model = models.CharField('Название модели', max_length=30, blank=False)
    engine = models.ForeignKey(EngineType, on_delete=models.CASCADE, verbose_name='Выберите тип двигателя', blank=False)
    body = models.ForeignKey(BodyType, on_delete=models.CASCADE, verbose_name='Выберите тип кузова', blank=False)
    description = models.TextField('Описание авто', blank=False)
    img = models.ImageField('Фото авто', upload_to='images/', null=True, blank=True)
    price = models.IntegerField('Цена(в $)', blank=False)
    year = models.DateField('Год выпуска', blank=False)
    mileage = models.IntegerField('Пробег', blank=False)
    engine_volume = models.FloatField('Объём двигателя', blank=False)
    phone_number = models.CharField('Телефон продавца', max_length=19, blank=False)

    def __str__(self):
        return self.name_model

    def get_absolute_url(self):
        return reverse('car-detail', args=[str(self.id)])
