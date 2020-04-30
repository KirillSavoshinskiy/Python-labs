from multiprocessing.pool import ThreadPool
from urllib import request

import change as change
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from form import form

from MySite.settings import EMAIL_HOST_USER
from django.utils import timezone, dateformat

from .models import Car, Company, BodyType, EngineType, Profile, Mail


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'verified']


admin.site.register(Mail)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Car)
admin.site.register(Company)
admin.site.register(BodyType)
admin.site.register(EngineType)