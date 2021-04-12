#creamos un archivo url por cada app para tener una mejor organizacion
#de la bilioteca x importamos la clase path
from django.urls import path
from . import views

app_name = 'nucleo'

urlpatterns = [
    path('', views.index, name='index'), #el nombre puede ser cualquiera
]
