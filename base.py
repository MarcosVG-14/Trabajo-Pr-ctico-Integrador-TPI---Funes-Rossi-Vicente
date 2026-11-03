from abc import ABC
from datetime import datetime
from typing import Optional

class Base(ABC):
    def __init__(self, id:int, eliminado:bool, created_at:datetime) -> None:
        self.__id = id
        self.__eliminado = eliminado
        self.__created_at = created_at

    @property
    def id(self) -> int:
        return self.__id

    @property
    def eliminado(self) -> bool:
        return self.__eliminado

    @property
    def created_at(self) -> datetime:
        return self.__created_at