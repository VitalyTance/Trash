from django.db import models

# Create your models here.


class Car(models.Model):
    car_model = models.CharField(max_length=500)
    def __str__(self):
        return self.car_model
    reg_time = models.DateTimeField('registration date')


class Detail(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    reg_number = models.CharField(verbose_name='registration number', max_length=500)
    def __str__(self):
        return self.reg_number
    re_sell = models.BooleanField('used?')


class RegDetail(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    reg_date = models.DateTimeField('car number registration date')