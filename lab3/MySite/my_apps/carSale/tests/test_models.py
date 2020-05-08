from django.contrib.auth.models import User
from django.test import TestCase
from my_apps.carSale.models import Company, EngineType, BodyType, Car, Mail, Profile


class BodyTypeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        body = BodyType.objects.create(body_type='Седан')
        body.save()

    def test_body_type(self):
        body_type_obj = BodyType.objects.get(id=1)
        b_type = body_type_obj.body_type
        assert b_type == str(body_type_obj)

    def test_field_length(self):
        body_type_obj = BodyType.objects.get(id=1)
        length = body_type_obj._meta.get_field('body_type').max_length
        assert length == 20


class EngineTypeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        engine = EngineType.objects.create(engine_type='Бензин')
        engine.save()

    def test_engine_type(self):
        engine_type_obj = EngineType.objects.get(id=1)
        en_type = engine_type_obj.engine_type
        assert en_type == str(engine_type_obj)

    def test_field_length(self):
        engine_type_obj = EngineType.objects.get(id=1)
        length = engine_type_obj._meta.get_field('engine_type').max_length
        assert length == 20


class CompanyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        copm = Company.objects.create(name='Audi')
        copm.save()

    def test_name_length(self):
        company = Company.objects.get(id=1)
        length = company._meta.get_field('name').max_length
        assert length == 30

    def test_str_name(self):
        company = Company.objects.get(id=1)
        name = company.name
        assert name == str(company)


class CarModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Company.objects.create(name='BMW')
        EngineType.objects.create(engine_type='Бензин')
        BodyType.objects.create(body_type='Седан')
        company = Company.objects.get(id=1)
        engine_type_obj = EngineType.objects.get(id=1)
        body_type_obj = BodyType.objects.get(id=1)
        Car.objects.create(company=company, name_model='M5', engine=engine_type_obj, body=body_type_obj,
                           description='qwer', img='images/nissan-patrol-gr-5-door-24.jpg',
                           price=10, mileage=100, engine_volume=3.0, phone_number='+37533222')
        Car.save()

    def test_field_length(self):
        car = Car.objects.get(id=1)
        length = car._meta.get_field('name_model').max_length
        self.assertEqual(length, 30)

    def test_name_model(self):
        car = Car.objects.get(id=1)
        name = car.name_model
        self.assertEqual(name, str(car))



