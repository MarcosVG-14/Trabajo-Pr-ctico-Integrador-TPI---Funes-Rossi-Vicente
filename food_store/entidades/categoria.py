from datetime import datetime
from .base import Base

class Categoria(Base):
    def __init__(self, nombre: str, descripcion: str):
        super().__init__()
        self._nombre: str = nombre
        self._descripcion: str = descripcion

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe de ser una cadena de texto.")
        if not nombre.strip():
            raise ValueError(f"El nombre no puede estar vacio")
        self._nombre = nombre

    @property
    def descripcion(self) -> str:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion: str) -> None:
        if not isinstance(descripcion, str):
            raise TypeError("La descripcion debe de ser una cadena de texto.")
        if not descripcion.strip():
            raise ValueError(f"La descripcion no puede estar vacia")
        self._descripcion = descripcion