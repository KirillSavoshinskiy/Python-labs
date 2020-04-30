# Generated by Django 3.0.5 on 2020-04-30 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carSale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_caption', models.CharField(max_length=100, verbose_name='Заголовок сообщения')),
                ('email_text', models.TextField(verbose_name='Текст сообщения')),
                ('email_date', models.DateField(verbose_name='Время отправки')),
                ('email_time', models.TimeField()),
                ('check_send', models.BooleanField(default=False)),
                ('resp', models.ManyToManyField(blank=True, limit_choices_to={'verified': True}, to='carSale.Profile')),
            ],
        ),
    ]
