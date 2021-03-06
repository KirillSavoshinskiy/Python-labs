# Generated by Django 3.0.5 on 2020-05-11 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_type', models.CharField(blank=True, choices=[('Седан', 'Седан'), ('Универсал', 'Универсал'), ('Внедорожник', 'Внедорожник'), ('Кроссовер', 'Кроссовер'), ('Хэтчбэк', 'Хэтчбэк'), ('None', 'None')], default='N', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EngineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_type', models.CharField(blank=True, choices=[('Бензин', 'Бензин'), ('Дизель', 'Дизель'), ('Электро', 'Электро'), ('None', 'None')], default='N', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_caption', models.CharField(max_length=100, verbose_name='Заголовок сообщения')),
                ('email_text', models.TextField(null=True, verbose_name='Текст сообщения')),
                ('email_date', models.DateField(null=True, verbose_name='Время отправки')),
                ('email_time', models.TimeField(null=True)),
                ('resp', models.ManyToManyField(limit_choices_to={'verified': False}, to='carSale.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_model', models.CharField(max_length=30, verbose_name='Название модели')),
                ('description', models.TextField(verbose_name='Описание авто')),
                ('img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Фото авто')),
                ('price', models.IntegerField(verbose_name='Цена(в $)')),
                ('year', models.DateField(verbose_name='Год выпуска')),
                ('mileage', models.IntegerField(verbose_name='Пробег')),
                ('engine_volume', models.FloatField(verbose_name='Объём двигателя')),
                ('phone_number', models.CharField(max_length=19, verbose_name='Телефон продавца')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carSale.BodyType', verbose_name='Выберите тип кузова')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carSale.Company', verbose_name='Выберите марку авто')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carSale.EngineType', verbose_name='Выберите тип двигателя')),
            ],
        ),
    ]
