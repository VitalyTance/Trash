from django.shortcuts import render, reverse
from django.views import generic

from .models import Buyers, Purchases
# Create your views here.


def index(request):
    return render(request, 'customers/index.html')


class BuyersList(generic.ListView):
    model = Buyers
    template_name = 'customers/buyers_list.html'
    context_object_name = 'buyers_list'

    def get_queryset(self):
        return Buyers.objects.all()


class PurchasePage(generic.DetailView):
    model = Buyers
    template_name = 'customers/purchase.html'