#creamos un archivo url por cada app para tener una mejor organizacion
#de la bilioteca x importamos la clase path
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
#    path('', views.tienda_index, name='tienda_index'), #el nombre puede ser cualquiera
    path('', views.lista_productos, name='lista_productos'),
    path('<slug:categoria_slug>/', views.lista_productos,
        name='lista_productos_por_categoria'),
    path('<int:id>/<slug:slug>/', views.producto_detalle,
        name='producto_detalle'),
]
