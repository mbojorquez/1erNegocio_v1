#FORMULARIO QUE NOS PERMITE DESPLEGAR HASTA 20 PRODUCTOS EN EL CARRITO DE COMPRA
from django import forms
ELECCION_CANTIDAD_PRODUCTOS = [(i, str(i)) for i in range (1, 21)]

class FormularioAgregarProducto(forms.Form):
    cantidad =forms.TypedChoiceField(choices=ELECCION_CANTIDAD_PRODUCTOS,
                                        coerce=int)
    sobreescribir = forms.BooleanField(required=False,
                                    initial=False,
                                    widget=forms.HiddenInput)
