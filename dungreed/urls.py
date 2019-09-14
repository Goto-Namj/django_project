from django.urls import path

from . import views


urlpatterns = [
    path('',
        views.main_page,
        name='main_page'),
    path('dps_test/',
        views.dps_test,
        name='dps_test'),
    path('item_dictionary/',
        views.dps_test,
        name='item_dictionary'),
    path('free_bulletin_board/',
        views.dps_test,
        name='free_bulletin_board'),
    path('guide/',
        views.dps_test,
        name='guide'),
    path('simulator/',
        views.dps_test,
        name='simulator'),
]