from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect

from .models import CarModel

# Create the views here

# Create the view to show Car Model List
class CarModelListView(generic.ListView):
    template_name = 'car_tables/index.html'
    context_object_name = 'car_model_list'

    def get_queryset(self):
        return CarModel.objects.all()

# Create the view to show Car Details
class CarDetailView(generic.DetailView):
    model = CarModel
    template_name = 'car_tables/detail.html'

# Create the view to show form to add new Car Model
def new_car_model(request):
    return render(request, 'car_tables/new_model.html')

# Create the view to add new Car Model
def add_new_car_model(request):
    CarModel.objects.create(car_model=request.POST['new_model'])
    return HttpResponseRedirect(reverse('car_tables:new_detail'))

# Create the view to show form to add new Car Detail
def new_car_detail(request):
    return render(request, 'car_tables/new_detail.html')

# Create the view to add new Car Detail
def add_new_car_detail(request):
    new_detail = CarModel.objects.all().last()
    new_detail.cardetail_set.create(car_number=request.POST['new_number'],
                                    region=request.POST['new_region'])
    return HttpResponseRedirect(reverse('car_tables:index'))
