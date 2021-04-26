from .carrito import Carrito

#función
def carrito(request):
    return {'carrito': Carrito(request)}