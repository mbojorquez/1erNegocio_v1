from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Categoria, Producto


# Create your views here.
#def tienda_index(request):
#    return HttpResponse("<h1> Tienda MB</h1>")


#MUESTRA LOS PRODUCTOS
def lista_productos(request, categoria_slug=None):
    categoria = None
    categorias = Categoria.objects.all()
    print('Las categorias son: ')
    print(categorias)
    productos = Producto.objects.filter(disponibilidad=True)
    if categoria_slug:
        categoria = get_object_or_404(Categoria, slug=categoria_slug)
        productos = productos.filter(categoria=categoria)
    return render(request, 'tienda/productos/lista.html', 
                    {'categoria': categoria,
                    'categorias': categorias,
                    'productos': productos})

#MUESTRA LOS DETALLES DEL PRODUCTO
def producto_detalle(request, id, slug):
    producto = get_object_or_404(Producto, id=id, 
                                    slug=slug, disponibilidad=True)
    return render(request, 'tienda/productos/detalles.html',
                            {'producto': producto,})