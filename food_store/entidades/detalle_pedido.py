from datetime import datetime
from .base import Base

class DetallePedido(Base):
    def __init__(self):
    # def __init__(self, id: int, eliminado: bool, created_at: datetime, cantidad: int, subtotal: float, producto = None) -> None:
        super().__init__(id, eliminado, created_at)
        self.productos = []
        # self.__cantidad = cantidad
        # self.__subtotal = subtotal
        # self.__producto = producto

    def agregar_producto(self, producto):
        self.productos.append(producto)