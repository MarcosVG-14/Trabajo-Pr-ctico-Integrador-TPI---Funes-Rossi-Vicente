from datetime import datetime
from entidades.base import Base
from enums.enums import Rol
from excepciones.excepciones import DatoInvalidoError

class Usuario(Base):
    def __init__(self, nombre: str, apellido: str, mail: str, celular: str, contrasenia: str, rol: Rol) -> None:
        super().__init__()
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.celular = celular
        self.__contrasenia = contrasenia
        self.rol = rol
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor,str):
            raise DatoInvalidoError("El tipo de dato ingresado es incorrecto.")
        if not valor.strip():
            raise DatoInvalidoError("El nombre del usuario no puede estar vacío.")
        self.__nombre = valor.strip()
    
    @property
    def apellido(self) -> str:
        return self.__apellido
    
    @apellido.setter
    def apellido(self, valor: str) -> None:
        if not isinstance(valor,str):
            raise DatoInvalidoError("El tipo de dato ingresado es incorrecto.")
        if not valor.strip():
            raise DatoInvalidoError("El apellido del usuario no puede estar vacío.")
        self.__apellido = valor.strip()
    
    @property
    def mail(self) -> str:
        return self.__mail
    
    @mail.setter
    def mail(self, valor: str) -> None:
        if not valor or "@" not in valor or "." not in valor:
            raise DatoInvalidoError("El formato del mail es inválido.")
        self.__mail = valor.strip().lower()
    
    @property
    def celular(self) -> str:
        return self.__celular
    
    @celular.setter
    def celular(self, valor: str) -> None:
        if not isinstance(valor,str):
            raise DatoInvalidoError("El tipo de dato ingresado es incorrecto.")
        if not valor.strip():
            raise DatoInvalidoError("El celular no puede estar vacío.")
        self.__celular = valor.strip()
    
    @property
    def rol(self) -> Rol:
        return self.__rol
    
    @rol.setter
    def rol(self, valor: Rol) -> None:
        if not isinstance(valor, Rol):
            raise TypeError("El rol debe ser una instancia de la enumeración Rol.")
        self.__rol = valor
    
    def verificar_contrasenia(self, contrasenia_ingresada: str) -> bool:
        """Verifica la contraseña sin exponerla hacia el exterior del objeto."""
        return self.__contrasenia == contrasenia_ingresada
    
    def actualizar_contrasenia(self, nueva_contrasenia: str) -> None:
        """Método seguro para actualizar la contraseña."""
        if not isinstance(nueva_contrasenia,str):
            raise DatoInvalidoError("Tipo de dato ingresado incorrecto.")
        if not len(nueva_contrasenia.strip()) < 4:
            raise DatoInvalidoError("La contraseña debe tener al menos 4 caracteres.")
        self._contrasenia = nueva_contrasenia.strip()
    
    def __str__(self) -> str:
        return (
            f"ID: {self.id} | "
            f"Nombre: {self.nombre} {self.apellido} | "
            f"Mail: {self.mail} | "
            f"Celular: {self.celular} | "
            f"Rol: {self.rol.name}"
        )