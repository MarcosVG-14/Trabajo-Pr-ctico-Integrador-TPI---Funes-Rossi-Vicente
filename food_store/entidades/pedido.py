from .base import Base
from datetime import datetime
from typing import List
from enums import Estado, FormaPago


class Pedido(Base):
    def __init__(self, detalle_pedido):
    # def __init__(self, id, eliminado, created_at, detalle_pedido):
    # def __init__(self, id: int, eliminado: bool, created_at: datetime, fecha: datetime, estado: Estado, total: float, forma_pago: FormasPago) -> None:
        # super().__init__(id, eliminado, created_at)
        self.detalle_pedido = detalle_pedido
        # self.__fecha = fecha
        # self.__estado = estado
        # self.__total = total
        # self.__forma_pago = forma_pago
        # self.__detalles: List[DetallePedido] = []

