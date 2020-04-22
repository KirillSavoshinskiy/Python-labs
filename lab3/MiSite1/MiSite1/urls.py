from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('my_apps.carSale.urls')),
    path('admin/', admin.site.urls)
] + static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
