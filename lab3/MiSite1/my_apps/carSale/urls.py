
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
     path('', views.AutoListView.as_view(), name='Home'),
     path('<int:pk>/', views.AutoDetailView.as_view(), name='car-detail'),
     path('register/', views.RegisterFormView.as_view(), name='register'),
     path('login/', views.user_login, name='login'),
     path('logout/', views.user_logout, name='logout'),
     path('newCar/', views.new_car, name='newCar'),


]
