from django.test import TestCase
from catalogo.models import Compra

class YourTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_compra = Compra.objects.create(id= 'cacee12d-ab3c-4a58-b1b5-d098ce328cd8', name='zapato', precio=120000, descripcion="de pana")

    def test_descripcion_max_length(self):
        co = Compra.objects.get(id='cacee12d-ab3c-4a58-b1b5-d098ce328cd8')
        max_length = co._meta.get_field('descripcion').max_length
        self.assertEquals(max_length,200)

    def test_first_name_label(self):
        co = Compra.objects.get(id='cacee12d-ab3c-4a58-b1b5-d098ce328cd8')
        field_label= co._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')
