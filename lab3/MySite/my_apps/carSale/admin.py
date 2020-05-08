from django.contrib import admin
from .models import Car, Company, BodyType, EngineType, Profile, Mail


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'verified']


admin.site.register(Mail)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Car)
admin.site.register(Company)
admin.site.register(BodyType)
admin.site.register(EngineType)