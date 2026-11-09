from .base import Base
from .categoria import Categoria
from excepciones.excepciones import DatoInvalidoError

class Producto(Base):
    def __init__(self, nombre: str, precio: float, descripcion: str, stock: int, imagen: str = "", disponible: bool = True) -> None:
        super().__init__()
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.stock = stock
        self.imagen = imagen
        self.__disponible: bool = disponible
        self.__categoria: Categoria | None = None

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise DatoInvalidoError("El nombre del producto no puede estar vacío.")
        self.__nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, valor: float) -> None:
        try:
            num = float(valor)
        except (ValueError, TypeError):
            raise DatoInvalidoError("El precio debe ser un valor numérico.")
        if num < 0:
            raise DatoInvalidoError("El precio no puede ser menor a cero.")
        self.__precio = num

    @property
    def descripcion(self) -> str:
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise DatoInvalidoError("La descripción debe ser una cadena de texto.")
        self.__descripcion = valor.strip()

    @property
    def stock(self) -> int:
        return self.__stock

    @stock.setter
    def stock(self, valor: int) -> None:
        try:
            num = int(valor)
        except (ValueError, TypeError):
            raise DatoInvalidoError("El stock debe ser un valor entero.")
        if num < 0:
            raise DatoInvalidoError("El stock no puede ser menor a cero.")
        self.__stock = num

    @property
    def imagen(self) -> str:
        return self.__imagen

    @imagen.setter
    def imagen(self, valor: str) -> None:
        if not isinstance(valor, str):
            raise DatoInvalidoError("La imagen debe ser una cadena de texto.")
        self.__imagen = valor

    @property
    def disponible(self) -> bool:
        return self.__disponible and self.__stock > 0

    @disponible.setter
    def disponible(self, valor: bool) -> None:
        if not isinstance(valor, bool):
            raise TypeError("El valor de disponibilidad debe ser de tipo booleano.")
        self.__disponible = valor

    @property
    def categoria(self) -> Categoria | None:
        return self.__categoria

    @categoria.setter
    def categoria(self, valor: Categoria | None) -> None:
        self.__categoria = valor

    def __str__(self) -> str:
        cat_nombre = self.__categoria.nombre if self.__categoria else "Sin categoría"
        return (
            f"ID: {self.id} | {self.__nombre} - ${self.__precio:.2f} | "
            f"Stock: {self.__stock} | Categoría: {cat_nombre} | "
            f"Disponible: {'Sí' if self.disponible else 'No'}"
        )