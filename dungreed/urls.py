from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dps/<int:reqreq>/', views.dps_test, name='dps_test'),
]