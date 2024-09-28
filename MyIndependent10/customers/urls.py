from django.urls import path

from . import views
# Create your urlpatterns here


app_name = 'customers'


urlpatterns = [
    path('', views.index, name='index'),
    path('buyers_list', views.BuyersList.as_view(), name='buyers_list'),
    path('buyers_list/<int:pk>', views.PurchasePage.as_view(), name='purchase_page'),
]