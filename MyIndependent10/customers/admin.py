from django.contrib import admin

from .models import Buyers, Purchases
# Register your models here.


class PurchasesInLine(admin.TabularInline):
    model = Purchases
    extra = 1


class BuyersAdmin(admin.ModelAdmin):
    inlines = [PurchasesInLine]


admin.site.register(Buyers, BuyersAdmin)