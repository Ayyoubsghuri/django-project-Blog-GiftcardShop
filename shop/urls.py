from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('',views.shop,name='indexshop'),
    path('payment/',views.payment,name='payp'),
    path('process_order/',views.processOrder,name='paydone'),



]
