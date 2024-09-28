from django.urls import path

from . import views
# Create your urlpatterns here


app_name = 'car_reg'


urlpatterns = [
    path('', views.index, name='index'),
    path('car_list', views.CarList.as_view(), name='car_list'),
    path('car_list/<int:pk>', views.DetailPage.as_view(), name='detail_page'),
    path('car_list/car_model/detail/<int:pk>', views.RegDetailPage.as_view(), name='reg_detail_page'),
]