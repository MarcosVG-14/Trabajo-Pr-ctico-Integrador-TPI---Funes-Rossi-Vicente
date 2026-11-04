from datetime import datetime
from .base import Base

class Categoria(Base):
    def __init__(self, nombre, descripcion, id, eliminado, created_at):
        super().__init__(id, eliminado, created_at)
        self.nombre: str = nombre
        self.descripcion: str = descripcion

    # @property
    # def nombre(self) -> str:
    #     return self.__nombre

    # @property
    # def descripcion(self) -> str:
    #     return self.__descripcion