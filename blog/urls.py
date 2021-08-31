from django.urls import path
from . import views
from django.contrib import admin
# admin.autodiscover()

app_name = "blog"


urlpatterns = [
    path('',views.blog,name='blog'),
    path('<slug:slug>/',views.id,name='blogid'),
    path('vip/<slug:slug>/',views.idvip,name='blogidv'),
]
