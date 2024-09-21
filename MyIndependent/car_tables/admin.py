from django.contrib import admin

from .models import CarModel, CarDetail

# Register your models here.

# Create the object to register in common field for Car Model and Car Detail representation

class CarDetailInLine(admin.TabularInline):
    model = CarDetail
    extra = 1

# Create the representatrion common field for Car Model record

class CarDetailInCarModel(admin.ModelAdmin):
    inlines = [CarDetailInLine]
    list_filter = ['car_model']
    search_fields = ['car_model']

admin.site.register(CarModel, CarDetailInCarModel)
