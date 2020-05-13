import datetime

from django.contrib.auth.models import User
from django.test import TestCase

from my_apps.carSale.models import Company, EngineType, BodyType, Car, Mail, Profile


class BodyTypeModelTest(TestCase):

    def test_body_type(self):
        body = BodyType.objects.create(body_type='Седан')
        body.save()
        assert 'Седан' == str(body)

    def test_field_length(self):
        body = BodyType.objects.create(body_type='Седан')
        body.save()
        length = body._meta.get_field('body_type').max_length
        assert length == 20


class EngineTypeModelTest(TestCase):

    def test_engine_type(self):
        engine = EngineType.objects.create(engine_type='Бензин')
        engine.save()
        assert 'Бензин' == str(engine)

    def test_field_length(self):
        engine = EngineType.objects.create(engine_type='Бензин')
        engine.save()
        length = engine._meta.get_field('engine_type').max_length
        assert length == 20


class CompanyModelTest(TestCase):

    def test_name_length(self):
        company = Company.objects.create(name='Audi')
        company.save()
        length = company._meta.get_field('name').max_length
        assert length == 30

    def test_str_name(self):
        company = Company.objects.create(name='Audi')
        company.save()
        assert 'Audi' == str(company)


class CarModelTest(TestCase):

    def test_name_model(self):
        user = User.objects.create(username='testuser1', password='12345', email='savosh28@gmail.com')
        user.save()
        company = Company.objects.create(name='BMW')
        company.save()
        engine = EngineType.objects.create(engine_type='Бензин')
        engine.save()
        body = BodyType.objects.create(body_type='Седан')
        body.save()
        car = Car.objects.create(created_by=user, company=company, name_model='M5', engine=engine, body=body,
                                 description='qwer', img='images/nissan-patrol-gr-5-door-24.jpg',
                                 price=10, year='2020-12-12',
                                 mileage=100, engine_volume=3.0, phone_number='+37533222')
        car.save()
        assert 'M5' == str(car)


class MailTest(TestCase):

    def test_mail_str(self):
        mail = Mail.objects.create(email_caption='caption', email_text='text',
                                   email_date='2020-12-12',
                                   email_time="23:18:53", posted=True)

        assert 'caption' == mail.__str__()
