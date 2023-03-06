from django.urls import path

from . import views

urlpatterns = [
    path('suma/', views.my_view, name='index'),
    path('adios/', views.di_adios),
    path('calc/', views.Calculadora.as_view()),
]