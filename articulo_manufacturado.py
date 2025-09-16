from paprika import *
from articulo import Articulo
from typing import Set
from articulo_manufacturado_detalle import Articulo_detalle

@data
class Articulo_manufacturado(Articulo):
    descripcion: str
    tiempoEstimadoMinutos: int
    preparacion: str
    detalles: Set["Articulo_detalle"]

    def calcular_precio_final(self):
        pass