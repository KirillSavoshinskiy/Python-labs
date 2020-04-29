from django.test import TestCase
from my_apps.carSale.models import Company

class CompanyModelTest(TestCase):

    def test_name_length(self):
        Company.objects.create(name='Audi')
        company = Company.objects.get(id=1)
        length = company._meta.get_field('name').max_length
        assert length == 30

    def test_str_name(self):
        Company.objects.create(name='Audi')
        company = Company.objects.get(id=2)
        name = company.name
        assert name == str(company)

