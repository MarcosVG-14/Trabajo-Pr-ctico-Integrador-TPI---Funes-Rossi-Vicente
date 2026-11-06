from datetime import datetime
from entidades.base import Base

class Categoria(Base):
    def __init__(self, id: int, eliminado: bool, created_at: datetime, nombre: str, descripcion: str) -> None:
        super().__init__(id, eliminado, created_at)
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__productos = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def descripcion(self) -> str:
        return self.__descripcion