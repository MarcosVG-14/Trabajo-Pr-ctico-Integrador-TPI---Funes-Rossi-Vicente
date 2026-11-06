from datetime import datetime
from .base import Base

class DetallePedido(Base):
    def __init__(self, cantidad: int, subtotal: float, producto = None) -> None:
        super().__init__()
        self.__cantidad = cantidad
        self.__subtotal = subtotal
        self.__producto = producto

    def agregar_producto(self, producto):
        self.producto = producto