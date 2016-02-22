from django.conf.urls import url
#Primeros pasos
#esta es mi rama primero
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]