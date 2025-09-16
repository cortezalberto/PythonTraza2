from paprika import *
from articulo import Articulo
from typing import Set
from articulo_insumo import Articulo_insumo

@data
class Articulo_detalle(Articulo):
    id: int
    cantidad: int
    articulo_insumo: Articulo_insumo

    def calcular_precio_final(self):
        pass