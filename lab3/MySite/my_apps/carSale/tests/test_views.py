import pytest
from django.contrib.auth.models import User
from django.http import request
from django.test import TestCase, Client
from my_apps.carSale.apps import CarsaleConfig
from django.urls import reverse

from my_apps.carSale.forms import UserRegistrationForm, CarForm
from my_apps.carSale.models import Company, EngineType, BodyType, Car


class TestApp(TestCase):

    def test_app_name(self):
        app = CarsaleConfig
        assert app.name == 'my_apps.carSale'

 #   @pytest.mark.parametrize("app", [CarsaleConfig.name])
  #  def test_app(self, app):
   #     assert app == 'my_apps.carSale'


class User_Functionality_Test(TestCase):

    # @pytest.fixture()
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(username='testuser1', password='12345', email='savosh28@gmail.com')
        cls.test_user.save()

    def test_login(self):
        resp = self.client.post(reverse('login'), {'username': self.test_user.username, 'password': '12345'})
        self.assertRedirects(resp, '/')

    def test_login_html(self):
        resp = self.client.get('/login/')
        assert resp.status_code == 200

    def test_fail_login(self):
        resp = self.client.post(reverse('login'), {'username': self.test_user.username, 'password': '12355'})
        self.assertRaisesMessage(resp, 'Invalid login')

    def test_logout(self):
        resp = self.client.post(reverse('logout'))
        self.assertRedirects(resp, '/')

    def test_register(self):
        client = Client()
        resp = client.post('/register/')
        assert resp.status_code == 200
        resp = client.post('/register/', {'username': '1', 'first_name': '1', 'email': '1@gmail.com', 'password': '1'})
        assert resp.status_code == 200
        resp = client.get('/register/')
        assert resp.status_code == 200

    def test_invalid_register(self):
        form = UserRegistrationForm()
        self.assertFalse(form.is_valid())

    def test_valid_register(self):
        data = {'username': '1', 'first_name': '1', 'email': '1@gmail.com', 'password': '1'}
        form = UserRegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_create_car(self):
        client = Client()
        resp = client.post('/newCar/')
        assert resp.status_code == 200
