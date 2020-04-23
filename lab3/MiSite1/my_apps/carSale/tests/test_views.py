import unittest

from django.contrib.auth.models import User
from django.test import TestCase
from my_apps.carSale.models import Company, EngineType, BodyType, Car
from django.urls import reverse
from my_apps.carSale.forms import LoginForm


class CarListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Company.objects.create(name='BMW')
        EngineType.objects.create(engine_type='Бензин')
        BodyType.objects.create(body_type='Седан')
        company = Company.objects.get(id=1)
        engine_type_obj = EngineType.objects.get(id=1)
        body_type_obj = BodyType.objects.get(id=1)
        number_cars = 15
        for car in range(number_cars):
            Car.objects.create(company=company, name_model='M5', engine=engine_type_obj, body=body_type_obj,
                               description='qwer', img='images/bmw.png',
                               price=10)

    def test_view_url_exist(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Home'))
        self.assertEqual(resp.status_code, 200)


class UserTest(TestCase):

    def setUp(self):
        self.test_user1 = User.objects.create_user(username='testuser1', password='12345')
        self.test_user1.save()

    def test_login(self):
        resp = self.client.post(reverse('login'), {'username': self.test_user1.username, 'password': '12345'})
        self.assertRedirects(resp, '/')

    def test_login_html(self):
        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

    def test_fail_login(self):
        resp = self.client.post(reverse('login'), {'username': self.test_user1.username, 'password': '12355'})
        self.assertRaisesMessage(resp, 'Invalid login')

    def test_logout(self):
        resp = self.client.post(reverse('logout'))
        self.assertRedirects(resp, '/')

    def test_new_car(self):
        resp = self.client.post(reverse('newCar'))
        self.assertRedirects(resp, '/')
