import unittest

from django.test import TestCase
from my_apps.carSale.models import Company, EngineType, BodyType, Car


class CompanyModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Company.objects.create(name="Audi")

    def test_name_length(self):
        Company.objects.create(name='Audi')
        company = Company.objects.get(id=1)
        length = company._meta.get_field('name').max_length
        self.assertEqual(length, 30)

    def test_str_name(self):
        Company.objects.create(name='Audi')
        company = Company.objects.get(id=1)
        name = company.name
        self.assertEqual(name, str(company))


class EngineTypeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        EngineType.objects.create(engine_type='Бензин')

    def test_engine_type(self):
        engine_type_obj = EngineType.objects.get(id=1)
        en_type = engine_type_obj.engine_type
        self.assertEqual(en_type, str(engine_type_obj))

    def test_field_length(self):
        engine_type_obj = EngineType.objects.get(id=1)
        length = engine_type_obj._meta.get_field('engine_type').max_length
        self.assertEqual(length, 20)


class BodyTypeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        BodyType.objects.create(body_type='Седан')

    def test_engine_type(self):
        body_type_obj = BodyType.objects.get(id=1)
        b_type = body_type_obj.body_type
        self.assertEqual(b_type, str(body_type_obj))

    def test_field_length(self):
        body_type_obj = BodyType.objects.get(id=1)
        length = body_type_obj._meta.get_field('body_type').max_length
        self.assertEqual(length, 20)


class CarModelTest(TestCase):

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

    def test_field_length(self):
        car = Car.objects.get(id=1)
        length = car._meta.get_field('name_model').max_length
        self.assertEqual(length, 30)

    def test_name_model(self):
        car = Car.objects.get(id=1)
        name = car.name_model
        self.assertEqual(name, str(car))


if __name__ == '__main__':
    unittest.main()
