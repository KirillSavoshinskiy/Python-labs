from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import FormView, DetailView
from .forms import LoginForm, CarForm, UserRegistrationForm, ProfileEditForm
from .models import Car, Profile


class AutoListView(generic.ListView):
    model = Car
    template_name = 'carSale/Home.html'


class AutoDetailView(DetailView):
    model = Car
    template_name = 'carSale/DetailCarInfo.html'


class AutoDeleteView(generic.DeleteView):
    model = Car
    template_name = 'carSale/confirm_delete.html'
    success_url = reverse_lazy('Home')


class AutoUpdateView(generic.UpdateView):
    model = Car
    fields = ('company', 'name_model', 'engine', 'body', 'description', 'price', 'year', 'mileage', 'engine_volume',
              'phone_number')
    template_name = 'carSale/updateCar.html'


class AutoCreateView(generic.CreateView):
    form_class = CarForm
    model = Car
    template_name = 'carSale/newCar.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(AutoCreateView, self).form_valid(form)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return  redirect(reverse('Home'))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'carSale/register.html', {'user_form': user_form})


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "carSale/login.html"
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


def user_logout(request):
    auth.logout(request)
    return redirect('Home')
