from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import FormView
from .forms import LoginForm, CarForm
from .models import Car


class AutoListView(generic.ListView):
    model = Car
    template_name = 'carSale/Home.html'


class AutoDetailView(generic.DetailView):
    model = Car
    template_name = 'carSale/DetailCarInfo.html'


class RegisterFormView(FormView):
    form_class = UserCreationForm
    template_name = 'carSale/register.html'
    success_url = ''

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Home')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'carSale/login.html', {'form': form})


def user_logout(request):
    auth.logout(request)
    return redirect('Home')


def new_car(request):
    car_form = CarForm()
    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
        return redirect('Home')
    return render(request, 'carSale/newCar.html', {'car_form': car_form})