from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic
from django.views.generic import FormView, DetailView
from .forms import LoginForm, CarForm, UserRegistrationForm, ProfileEditForm
from .models import Car, Profile
from .tokens import user_token_generator


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
            new_user.is_activate = False
            new_user.save()
            use_https = request.is_secure()
            current_site = get_current_site(request)
            email_caption = 'Активация аккаунта'
            token = user_token_generator.make_token(new_user)
            message = render_to_string('carSale/email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'token': token,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'protocol': 'https' if use_https else 'http',
            })
            to_email = user_form.cleaned_data.get('email')
            email = EmailMessage(
                email_caption, message, to=[to_email]
            )
            email.send()
            return render(request, 'carSale/emailAlert.html')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'carSale/register.html', {'user_form': user_form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and user_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'carSale/activation.html')


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
