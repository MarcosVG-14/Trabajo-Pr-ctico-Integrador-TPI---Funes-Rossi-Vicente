from .base import Base
from datetime import datetime
from typing import List
from enums import Estado, FormaPago


class Pedido(Base):
    def __init__(self, id: int, eliminado: bool, created_at: datetime, fecha: datetime, estado: Estado, total: float, forma_pago: FormasPago) -> None:
        super().__init__(id, eliminado, created_at)
        self.__fecha = fecha
        self.__estado = estado
        self.__total = total
        self.__forma_pago = forma_pago
        self._detalles: List[DetallePedido] = []

    @property
    def detalles(self):
        return self._detalles
    
    def __len__(self) -> int:
        return len(self._detalles)

    def __iter__(self):
        return iter(self._detalles)

    def __contains__(self, detalle: "Detalle") -> bool:
        return detalle in self._detalles

    def agregar_producto(self, detalle):
        self._detalles.append(detalle)