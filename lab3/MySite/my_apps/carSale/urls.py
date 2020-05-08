
from django.urls import path
from . import views

urlpatterns = [
     path('', views.AutoListView.as_view(), name='Home'),
     path('<int:pk>/', views.AutoDetailView.as_view(), name='car-detail'),
     path('register/', views.register, name='register'),
     path('login/', views.LoginFormView.as_view(), name='login'),
     path('logout/', views.user_logout, name='logout'),
     path('newCar/', views.AutoCreateView.as_view(), name='newCar'),
     path('<int:pk>/delete/', views.AutoDeleteView.as_view(), name='deleteCar'),
     path('<int:pk>/update/', views.AutoUpdateView.as_view(), name='updateCar')
]