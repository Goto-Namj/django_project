from django.urls import path

from . import views


urlpatterns = [
    path('', views.dps_test, name='dps_test'),
]