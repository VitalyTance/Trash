from django.shortcuts import render, reverse
from django.views import generic

from .models import Car, Detail, RegDetail
# Create your views here.


def index(request):
    return render(request, 'car_reg/index.html')


class CarList(generic.ListView):
    model = Car
    template_name = 'car_reg/car_list.html'
    context_object_name = 'car_list'

    def get_queryset(self):
        return Car.objects.all()


class DetailPage(generic.DetailView):
    template_name = 'car_reg/car_detail.html'
    model = Car


class RegDetailPage(generic.DetailView):
    template_name = 'car_reg/reg_detail_page.html'
    model = Detail