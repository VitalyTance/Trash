from django.urls import path

from . import views

# Create app's urlpatterns here
app_name = 'car_tables'
urlpatterns = [
    path('', views.CarModelListView.as_view(), name='index'),
    path('<int:pk>', views.CarDetailView.as_view(), name='detail'),
    path('add_model', views.new_car_model, name='new_model'),
    path('add_model/create', views.add_new_car_model, name='add_new_model'),
    path('add_detail', views.new_car_detail, name='new_detail'),
    path('add_detail/create', views.add_new_car_detail, name='add_new_detail'),
]