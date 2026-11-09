from datetime import date
from typing import List, Optional
from .base import Base
from .calculable import Calculable
from .usuario import Usuario
from .producto import Producto
from .detalle_pedido import DetallePedido
from enums.enums import Estado, FormaPago
from excepciones.excepciones import StockInsuficienteError, DatoInvalidoError

class Pedido(Base, Calculable):
    def __init__(self, usuario: Usuario, forma_pago: FormaPago) -> None:
        super().__init__()
        self.__usuario: Usuario = usuario
        self.__fecha: date = date.today()
        self.__estado: Estado = Estado.PENDIENTE
        self.__forma_pago: FormaPago = forma_pago
        self.__total: float = 0.0
        self.__detalles: List[DetallePedido] = []

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def fecha(self) -> date:
        return self.__fecha

    @property
    def estado(self) -> Estado:
        return self.__estado

    @estado.setter
    def estado(self, nuevo_estado: Estado) -> None:
        if not isinstance(nuevo_estado, Estado):
            raise TypeError("El estado debe ser una instancia de la enumeración Estado.")
        self.__estado = nuevo_estado

    @property
    def total(self) -> float:
        return self.__total

    @property
    def forma_pago(self) -> FormaPago:
        return self.__forma_pago

    @forma_pago.setter
    def forma_pago(self, nueva_forma: FormaPago) -> None:
        if not isinstance(nueva_forma, FormaPago):
            raise TypeError("La forma de pago debe ser una instancia de FormaPago.")
        self.__forma_pago = nueva_forma

    @property
    def detalles(self) -> List[DetallePedido]:
        return list(self.__detalles)

    def calcular_total(self) -> None:
        """Actualiza el total sumando los subtotales de todos los detalles."""
        self.__total = sum(detalle.subtotal for detalle in self.__detalles if not detalle.eliminado)

    def buscar_detalle_por_producto(self, producto: Producto) -> Optional[DetallePedido]:
        """Busca si un producto ya se encuentra en los detalles del pedido."""
        for detalle in self.__detalles:
            if not detalle.eliminado and detalle.producto.id == producto.id:
                return detalle
        return None

    def agregar_detalle(self, cantidad: int, producto: Producto) -> None:
        """Agrega un producto al pedido o suma la cantidad si ya existe."""
        if cantidad <= 0:
            raise DatoInvalidoError("La cantidad a agregar debe ser mayor a 0.")
        if not producto.disponible or producto.eliminado:
            raise DatoInvalidoError(f"El producto '{producto.nombre}' no está disponible.")
        
        detalle_existente = self.buscar_detalle_por_producto(producto)
        cantidad_actual_en_pedido = detalle_existente.cantidad if detalle_existente else 0
        
        if cantidad + cantidad_actual_en_pedido > producto.stock:
            raise StockInsuficienteError(f"Stock insuficiente para '{producto.nombre}'. Stock disponible: {producto.stock}")

        if detalle_existente:
            detalle_existente.cantidad += cantidad
        else:
            nuevo_detalle = DetallePedido(cantidad, producto)
            self.__detalles.append(nuevo_detalle)
        self.calcular_total()

    def eliminar_detalle_por_producto(self, producto: Producto) -> None:
        """Elimina un detalle del pedido basado en su producto."""
        detalle = self.buscar_detalle_por_producto(producto)
        if detalle:
            self.__detalles.remove(detalle)
            self.calcular_total()

    def __str__(self) -> str:
        return (
            f"Pedido ID: {self.id} | "
            f"Cliente: {self.__usuario.nombre} {self.__usuario.apellido} | "
            f"Fecha: {self.__fecha} | "
            f"Estado: {self.__estado.name} | "
            f"Forma de Pago: {self.__forma_pago.name} | "
            f"Total: ${self.__total:.2f}"
        )