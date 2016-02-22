from django.conf.urls import url

from . import views
#esta es mi rama primero ....
urlpatterns = [
    url(r'^$', views.index, name='index'),
]