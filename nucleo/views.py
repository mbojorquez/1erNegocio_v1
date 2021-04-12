from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    #template_name = '/nucleo/templates/nucleo/index.html'
    return render(request, "nucleo/index.html")
    #return render ("nucleo/index.html")
    #return HttpResponse("<h1> Primer negocio web de MB</h1>")