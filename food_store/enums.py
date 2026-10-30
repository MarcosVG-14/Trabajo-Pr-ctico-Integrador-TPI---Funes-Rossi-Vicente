from enum import Enum

class FormaPago (Enum):
    TARJETA = "Tarjeta"
    TRANSFERENCIA = "Transferencia"
    EFECTIVO ="Efectivo"
    def __str__(self):
        return self.value

class Rol (Enum):
    ADMIN = "Admin"
    USUARIO = "Usuario"
    def __str__(self):
        return self.value

class Estado (Enum):
    PENDIENTE = "Pendiente"
    CONFIRMADO = "Confirmado"
    TERMINADO = "Terminado"
    CANCELADO = "Cancelado"
    def __str__(self):
        return self.value