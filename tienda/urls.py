#creamos un archivo url por cada app para tener una mejor organizacion
#de la bilioteca x importamos la clase path
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.tienda_index, name='tienda_index'), #el nombre puede ser cualquiera
]
