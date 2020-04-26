from django.contrib import admin
from .models import Car, Company, BodyType, EngineType

admin.site.register(Car)
admin.site.register(Company)
admin.site.register(BodyType)
admin.site.register(EngineType)