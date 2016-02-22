from django.conf.urls import url
#Primeros pasos
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]