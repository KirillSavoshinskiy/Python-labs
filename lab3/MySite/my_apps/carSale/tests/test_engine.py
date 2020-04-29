from django.test import TestCase
from my_apps.carSale.models import  EngineType


class EngineTypeModelTest(TestCase):

    def test_engine_type(self):
        EngineType.objects.create(engine_type='Бензин')
        engine_type_obj = EngineType.objects.get(id=1)
        en_type = engine_type_obj.engine_type
        assert en_type == str(engine_type_obj)

    def test_field_length(self):
        EngineType.objects.create(engine_type='Бензин')
        engine_type_obj = EngineType.objects.get(id=2)
        length = engine_type_obj._meta.get_field('engine_type').max_length
        assert length == 20
