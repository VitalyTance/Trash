from django.db import models

from car_reg.models import Car
# Create your models here.


class Buyers(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name


class Purchases(models.Model):
    buyer = models.OneToOneField(Buyers, on_delete=models.CASCADE, primary_key=True)
    bought_cars = models.ManyToManyField(Car)


