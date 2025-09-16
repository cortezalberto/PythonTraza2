from paprika import *
from articulo import Articulo

@data
class Articulo_insumo(Articulo):
    precioCompra: float
    stockActual: int
    stockMaximo: int
    esParaElaborar: bool

    def calcular_precio_final(self):
        pass