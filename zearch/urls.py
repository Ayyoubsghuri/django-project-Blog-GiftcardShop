from django.urls import path
from . import views
# admin.autodiscover()

app_name = "search"


urlpatterns = [
    path('',views.zearch_vi,name='zrch'),
]
