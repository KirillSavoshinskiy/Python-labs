from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('', include('my_apps.carSale.urls')),
    path('admin/', admin.site.urls)]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()