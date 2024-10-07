from django.urls import path

from . import views
# Create your urlpatterns here
app_name = 'car_reg'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_new_car/', views.NewCarView.as_view(), name='add_new_car'),
    path('add_new_detail/', views.NewDetailView.as_view(), name='add_new_detail'),
    path('add_new_reg_detail', views.NewRegDetailView.as_view(), name='add_new_reg_detail')
]