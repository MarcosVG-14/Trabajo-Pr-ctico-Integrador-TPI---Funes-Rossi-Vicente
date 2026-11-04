from datetime import datetime
from .base import Base

class Producto(Base):
    # def __init__(self, id: int, eliminado: bool, created_at: datetime, nombre: str, precio: float, descripcion: str, stock: int, imagen: str, disponible: bool) -> None:
    #     super().__init__(id, eliminado, created_at)
    #     self.__nombre = nombre
    #     self.__precio = precio
        # self.__descripcion = descripcion
    #     self.__stock = stock
    #     self.__imagen = imagen
    #     self.__disponible = disponible

    def __init__(self,nombre ,categoria:None):
        self.nombre: str = nombre
        self.categoria = None
    
    def agregar_categoria(self, categoria):
        self.categoria = categoria