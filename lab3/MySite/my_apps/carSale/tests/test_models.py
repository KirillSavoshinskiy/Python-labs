from django.test import TestCase
from my_apps.carSale.models import Company, EngineType, BodyType, Car


class BodyTypeModelTest(TestCase):

    def test_engine_type(self):
        BodyType.objects.create(body_type='Седан')
        body_type_obj = BodyType.objects.get(id=1)
        b_type = body_type_obj.body_type
        assert b_type == str(body_type_obj)

    def test_field_length(self):
        BodyType.objects.create(body_type='Седан')
        body_type_obj = BodyType.objects.get(id=2)
        length = body_type_obj._meta.get_field('body_type').max_length
        assert length == 20


