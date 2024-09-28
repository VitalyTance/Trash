import datetime
from django.db import models

# Create your models here.


class Car(models.Model):
    car_model = models.CharField(max_length=500, default='Car Model')
    def __str__(self):
        return self.car_model
    reg_date = models.DateTimeField(verbose_name='registration date', default=datetime.datetime.now())


class Detail(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    reg_number = models.CharField(max_length=6, default='A000AA')
    def __str__(self):
        return self.reg_number
    def save(self, *args, **kwargs):
        self.reg_number = self.reg_number.upper()
        return super().save(*args, **kwargs)
    reg_region = models.IntegerField(default=0)
    re_sell = models.BooleanField(verbose_name='used?')


class RegDetail(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    reg_time = models.DateTimeField(verbose_name='car number registration date', default=datetime.datetime.now())