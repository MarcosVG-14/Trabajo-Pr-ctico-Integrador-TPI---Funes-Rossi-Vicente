from abc import ABC
from datetime import datetime
from typing import Optional

class Base(ABC):
    _contador_id: int = -1

    def __init__(self, id: int, eliminado: bool, created_at: datetime) -> None:
        self._id: int = Base._contador_id
        Base._contador_id += 1
        self._eliminado: bool = False
        self._created_at: datetime = datetime.now()

    @property
    def id(self) -> int:
        return self._id

    @property
    def eliminado(self) -> bool:
        return self._eliminado

    @eliminado.setter
    def eliminado(self, valor: bool) -> None:
        if not isinstance(valor, bool):
            raise TypeError("El estado de eliminación debe ser un booleano.")
        self._eliminado = valor

    @property
    def created_at(self) -> datetime:
        return self._created_at

    def __eq__(self, otro: Base | int) -> bool:
        if isinstance(otro, Base):
            return self._id == otro._id
        return self._id == otro
