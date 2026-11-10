from datetime import datetime
from .base import Base
from .categoria import Categoria

class Producto(Base):
    def __init__(self, nombre: str, precio: float, descripcion: str, stock: int, imagen: str, disponible: bool) -> None:
        super().__init__()
        self.__nombre = nombre
        self.__precio = precio
        self.__descripcion = descripcion
        self.__stock = stock
        self.__imagen = imagen
        self.__disponible = disponible
        self.__categoria = None

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre) -> None:
        if not isinstance(nombre, str):
            raise DatoInvalidoError("El nombre debe de ser una cadena de texto")
        if not nombre.strip():
            raise DatoInvalidoError("El nombre no puede estar vacío.")
        self.__nombre = nombre

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, precio) -> None:
        if not (isinstance(precio, int) or isinstance(precio, float)):
            raise DatoInvalidoError("El precio debe de ser un valor numerico.")
        if 0 > precio:
            raise DatoInvalidoError("El precio no puede ser menor a cero. ")
        self.__precio = precio

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, descripcion) -> None:
        if not isinstance(descripcion, str):
            raise DatoInvalidoError("La descripcion debe de ser una cadena de texto")
        if not descripcion.strip():
            raise DatoInvalidoError("La descripcion no puede estar vacía.")
        self.__descripcion = descripcion

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, stock) -> None:
        if not (isinstance(stock, int) or isinstance(stock, float)):
            raise DatoInvalidoError("El stock debe de ser un valor numerico.")
        if not 0 < stock:
            raise DatoInvalidoError("El stock debe ser mayor que cero.")
        self.__stock = stock

    @property
    def imagen(self) -> str:
        return self.__imagen

    @imagen.setter
    def imagen(self, imagen) -> None:
        if not isinstance(imagen, str):
            raise DatoInvalidoError("La imagen debe de ser una cadena de texto")
        if not imagen.strip():
            raise DatoInvalidoError("La imagen no puede estar vacío.")
        self.__imagen = imagen

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria) -> None:
        if not (isinstance(categoria, Categoria) or isinstance(categoria, None)):
            raise DatoInvalidoError("La categoria debe venir de la clase Categoria")
        self.__categoria = categoria

    @property
    def disponible(self):
        return self.__disponible
    
    @disponible.setter
    def disponible(self, disponible) -> None:
        if not isinstance(disponible, bool):
            raise DatoInvalidoError("La disponibilidad debe ser un dato booleano.")
        self.__disponible

    def agregar_categoria(self, categoria):
        if self.categoria:
            if categoria.id == self.categoria.id:
                if (categoria.nombre != self.categoria.nombre) or (categoria.descripcion != self.categoria.descripcion):
                    self.categoria = categoria
                else:
                    return("Esta categoria ya esta asignada.")
        else:
            self.categoria = categoria

    def quitar_categoria(self):
        if not self.categoria:
            return("No hay categoria asignada a este producto.")
        else:
            self.categoria = None