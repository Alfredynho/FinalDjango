from django.conf.urls import url
#Primeros pasos
#esta es mi rama master en GitHub
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]