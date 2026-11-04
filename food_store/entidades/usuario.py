from datetime import datetime
from .base import Base
from enums import Rol

class Usuario(Base):
    def __init__(self, id: int, eliminado: bool, created_at: datetime, nombre: str, apellido: str, mail: str, celular: str, contraseña: str, rol: Rol) -> None:
        super().__init__(id, eliminado, created_at)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail = mail
        self.__celular = celular
        self.__contraseña = contraseña
        self.__rol = rol