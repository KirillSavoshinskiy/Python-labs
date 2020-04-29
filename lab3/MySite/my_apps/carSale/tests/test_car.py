from django.test import TestCase
from my_apps.carSale.models import Company, EngineType, BodyType, Car


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
