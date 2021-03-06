# Generated by Django 3.0.5 on 2020-05-12 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carSale', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='check_send',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mail',
            name='resp',
            field=models.ManyToManyField(limit_choices_to={'verified': True}, to='carSale.Profile'),
        ),
    ]
