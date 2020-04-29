from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import FormView
from .forms import LoginForm, CarForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Car, Profile
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


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'carSale/Home.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'carSale/register.html', {'user_form': user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,
                      'carSale/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


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
