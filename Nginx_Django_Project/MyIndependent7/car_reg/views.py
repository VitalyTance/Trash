from django.shortcuts import render, reverse
from django.views import generic

from .models import Car, Detail, RegDetail
from .forms import CarForm, DetailForm, RegDetailForm
# Create your views here.


def index(request):
    return render(request, 'car_reg/index.html')


class NewCarView(generic.CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car_reg/add_new_car.html'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.save()
        return super(NewCarView, self).form_valid(form)

    def get_success_url(self):
        return reverse('car_reg:add_new_detail')


class NewDetailView(generic.CreateView):
    model = Detail
    form_class = DetailForm
    template_name = 'car_reg/add_new_detail.html'

    def get_initial(self):
        data = Car.objects.all().last()
        initial_data = super(NewDetailView, self).get_initial()
        initial_data['car'] = data.pk
        return initial_data

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.save()
        return super(NewDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('car_reg:add_new_reg_detail')


class NewRegDetailView(generic.CreateView):
    model = RegDetail
    form_class = RegDetailForm
    template_name = 'car_reg/add_new_reg_detail.html'

    def get_initial(self):
        data = Detail.objects.all().last()
        initial_data = super(NewRegDetailView, self).get_initial()
        initial_data['detail'] = data.pk
        return initial_data

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.save()
        return super(NewRegDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('car_reg:index')