from django.test import TestCase
from django.shortcuts import reverse, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import CarModel
from . import views

class ModelCarViewTest(TestCase):
    def test_add_blank_model(self):
        model = self.client.post(reverse('car_tables:new_model'), {'car_model': 'new_model'})
        blank = CarModel(car_model=model)
        self.assertIsNotNone(blank)
    def test_href_work_or_not(self):
        for model in CarModel.objects.all():
            url = reverse('car_tables:detail', args=model.id)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)