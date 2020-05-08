import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from my_apps.carSale.models import Company, EngineType, BodyType, Car
from django.urls import reverse


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
                               description='qwer', img='images/nissan-patrol-gr-5-door-24.jpg',
                               price=10, mileage=100, engine_volume=3.0, phone_number='+37533222')

    def test_view_url_exist(self):
        resp = self.client.get('')
        assert resp.status_code == 200

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Home'))
        assert resp.status_code == 200


class UserTest(TestCase):

    # @pytest.fixture()
    @classmethod
    def setUpTestData(cls):
        cls.test_user1 = User.objects.create_user(username='testuser1', password='12345')
        cls.test_user1.save()
        # return  test_user1

    def test_login(self):
        resp = self.client.post(reverse('login'), {'username': self.test_user1.username, 'password': '12345'})
        self.assertRedirects(resp, '/')

    def test_login_html(self):
        resp = self.client.get('/login/')
        assert resp.status_code == 200

    def test_fail_login(self):
        resp = self.client.post(reverse('login'), {'username': self.test_user1.username, 'password': '12355'})
        self.assertRaisesMessage(resp, 'Invalid login')

    def test_logout(self):
        resp = self.client.post(reverse('logout'))
        self.assertRedirects(resp, '/')

    def test_register_post(self):
        resp = self.client.post(reversed('register'))
        assert resp.status_code == 404

    def test_register_get(self):
        resp = self.client.get(reversed('register'))
        assert resp.status_code == 404

    def test_new_car(self):
        resp = self.client.post(reverse('newCar'))
        self.assertRedirects(resp, '/')
