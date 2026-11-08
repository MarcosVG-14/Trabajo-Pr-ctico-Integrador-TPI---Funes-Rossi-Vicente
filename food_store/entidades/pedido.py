from .base import Base
from datetime import datetime
from typing import List
from enums.enums import Estado, FormaPago


class Pedido(Base):
    def __init__(self, fecha: datetime, estado: Estado, total: float, forma_pago: FormasPago) -> None:
        super().__init__()
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

    def agregar_detalle(self, detalle):
        self._detalles.append(detalle)