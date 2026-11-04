from datetime import datetime
from .base import Base

class Categoria(Base):
    def __init__(self, nombre, descripcion):
        # super().__init__(id, eliminado, created_at)
        self.nombre: str = nombre
        self.descripcion: str = descripcion
    # def __init__(self, id: int, eliminado: bool, created_at: datetime, nombre: str, descripcion: str) -> None:

    # @property
    # def nombre(self) -> str:
    #     return self.__nombre

    # @property
    # def descripcion(self) -> str:
    #     return self.__descripcion