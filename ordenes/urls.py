from django.urls import path
from . import views

app_name = 'ordenes'

urlpatterns = [ #lista de urls
    path('crear/', views.crear_orden, name='crear_orden'), 
]