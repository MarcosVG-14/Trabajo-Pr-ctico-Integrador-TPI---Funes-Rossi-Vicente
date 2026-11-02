from enum import Enum

class FormasPago(Enum):
    TARJETA = "Tarjeta"
    TRANSFERENCIA = "Tranferencia"
    EFECTIVO = "Efectivo"

class Rol(Enum):
    ADMIN = "Admin"
    USUARIO = "Usuario"

class Estado(Enum):
    PENDIENTE = "El pedido está pendiente"
    CONFIRMADO = "El pedido fue confirmado!"
    TERMINADO = "El pedido ya está terminado"
    CANCELADO = "El pedido fue cancelado"