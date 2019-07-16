from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dps', views.dps_test, name='dps'),
]