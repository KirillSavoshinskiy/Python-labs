from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import FormView
from .forms import LoginForm, CarForm
from .models import Car
import logging

logging.basicConfig(filename="log-file.log", level=logging.INFO)


class AutoListView(generic.ListView):
    model = Car
    template_name = 'carSale/Home.html'
    logging.info('Car list is presented')


class AutoDetailView(generic.DetailView):
    model = Car
    template_name = 'carSale/DetailCarInfo.html'
    logging.info('Detail car information')


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = 'carSale/register.html'
    success_url = '/'

    def form_valid(self, form):
        logging.info('Register form is valid')
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "carSale/login.html"
    success_url = "/"

    def form_valid(self, form):
        logging.info('Login form is valid')
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


def user_logout(request):
    logging.info('Logout')
    auth.logout(request)
    return redirect('Home')


def new_car(request):
    car_form = CarForm()
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
            logging.info('Added new car')
        return redirect('Home')
    return render(request, 'carSale/newCar.html', {'car_form': car_form})