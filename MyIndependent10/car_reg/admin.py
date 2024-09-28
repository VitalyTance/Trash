from django.contrib import admin

from .models import Car, Detail, RegDetail
# Register your models here.


class RegDetailInLine(admin.StackedInline):
    model = RegDetail
    extra = 1


class DetailAdmin(admin.ModelAdmin):
    inlines = [RegDetailInLine]


admin.site.register(Detail, DetailAdmin)


class DetailInLine(admin.TabularInline):
    model = Detail
    extra = 1
    show_change_link = True


class CarAdmin(admin.ModelAdmin):
    inlines = [DetailInLine]


admin.site.register(Car, CarAdmin)