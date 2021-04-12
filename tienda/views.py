from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def tienda_index(request):
    return HttpResponse("<h1> Tienda MB</h1>")