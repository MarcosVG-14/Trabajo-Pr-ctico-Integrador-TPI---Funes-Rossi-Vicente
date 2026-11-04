from datetime import datetime
from .base import Base

class Categoria(Base):
    def __init__(self, nombre, descripcion):
        super().__init__()
        self.nombre: str = nombre
        self.descripcion: str = descripcion

    # @property
    # def nombre(self) -> str:
    #     return self.__nombre

    # @property
    # def descripcion(self) -> str:
    #     return self.__descripcion