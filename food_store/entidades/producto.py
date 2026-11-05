from datetime import datetime
from .base import Base

class Producto(Base):
    def __init__(self, nombre: str, precio: float, descripcion: str, stock: int, imagen: str, disponible: bool) -> None:
        super().__init__()
        self.__nombre = nombre
        self.__precio = precio
        self.__descripcion = descripcion
        self.__stock = stock
        self.__imagen = imagen
        self.__disponible = disponible
        self.categoria = None
    
    def agregar_categoria(self, categoria):
        self.categoria = categoria