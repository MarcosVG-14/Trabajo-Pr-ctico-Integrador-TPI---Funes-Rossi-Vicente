from .base import Base
from .producto import Producto

class DetallePedido(Base):
    def __init__(self, cantidad: int, producto: Producto) -> None:
        super().__init__()
        self.__cantidad: int = cantidad
        self.__producto: Producto = producto
        self.__subtotal: float = cantidad * producto.precio

    @property
    def cantidad(self) -> int:
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, valor: int) -> None:
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("La cantidad debe ser un entero mayor a cero.")
        self.__cantidad = valor
        self.__subtotal = self.__cantidad * self.__producto.precio

    @property
    def subtotal(self) -> float:
        return self.__subtotal

    @property
    def producto(self) -> Producto:
        return self.__producto

    def __str__(self) -> str:
        return (
            f"Producto: {self.__producto.nombre} | "
            f"Cantidad: {self.__cantidad} | "
            f"Precio Unitario: ${self.__producto.precio:.2f} | "
            f"Subtotal: ${self.__subtotal:.2f}"
        )