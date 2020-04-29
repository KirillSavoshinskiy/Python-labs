from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Car, Company, BodyType, EngineType, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'verified']


admin.site.register(Profile, ProfileAdmin)

admin.site.register(Car)
admin.site.register(Company)
admin.site.register(BodyType)
admin.site.register(EngineType)
