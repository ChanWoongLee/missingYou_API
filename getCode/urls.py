from django.urls import path
from . import views

urlpatterns = [
    path('animal/all', views.animal_list, name='animal_list'),
    path('animal/<str:pk>/', views.animal_get, name='animal_get'),
    path('animal/', views.animal_insert, name='animal_insert')
]