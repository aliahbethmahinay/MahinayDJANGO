
from django.urls import path
from . import views


urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('add/', views.add_reservation, name='add_reservation'),
    path(
        'edit/<int:reservation_id>/',
        views.edit_reservation,
        name='edit_reservation'
    ),
    path(
        'delete/<int:reservation_id>/',
        views.delete_reservation,
        name='delete_reservation'
    ),
]
