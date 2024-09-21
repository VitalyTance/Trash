from django.db import models
from django.core.validators import RegexValidator, ValidationError


# Create your models here.

# Create the Table of Car Models
class CarModel(models.Model):
    # Create a column for car models names
    car_model = models.CharField(
        max_length=500, blank=False, null=False
                                 )
    def __str__(self):
        return self.car_model
    def validate_constraints(self, exclude=['']):
        return self.car_model
    def blank(self):
        if self.car_model == '':
            raise ValidationError


# Create The Detail Table related to Car Model table
class CarDetail(models.Model):
    # Create the foreign key to Car Model Table
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    #Create Registration Number column
    car_number = models.CharField(max_length=6)
    def __str__(self):
        return self.car_number
    #Create Region of Registration number column
    region = models.IntegerField('region of registration', default=0)



