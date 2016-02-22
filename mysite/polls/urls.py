from django.conf.urls import url
#Primeros pasos
#Esto no se vera
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]