
from abc import ABC, abstractmethod
from usuario import Usuario
from enums import Rol

class Menu(ABC):
    def __init__(self, usuario: Usuario) -> None:
        self.__usuario: Usuario = usuario
    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @abstractmethod
    def mostrar(self) -> bool:
        """
        Muestra las opciones del menú y procesa la entrada del usuario.
        Retorna:
            True  -> Si el usuario elige "Cerrar sesión" (vuelve al login)
            False -> Si el usuario elige "Salir" (finaliza el programa)
        """
        pass


class MenuAdministrador(Menu):
    def mostrar(self) -> bool:
        print(f"\n=== FOOD STORE ADMINISTRADOR ({self.usuario.nombre} {self.usuario.apellido}) ===")
        print("1. Categorías")
        print("2. Productos")
        print("3. Usuarios")
        print("4. Pedidos")
        print("9. Cerrar sesión")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        match opcion:
            case "9":
                return False
            case "0":
                return "salir"
            case _:
                print("Opción no válida.")
                return True


class MenuCliente(Menu):
    def mostrar(self) -> bool:
        print(f"\n=== FOOD STORE CLIENTE ({self.usuario.nombre} {self.usuario.apellido}) ===")
        print("1. Ver categorías")
        print("2. Ver productos disponibles")
        print("3. Mis pedidos")
        print("4. Mis datos")
        print("9. Cerrar sesión")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        match opcion:
            case "9":
                print("Cerrando sesión de cliente...")
                return False
            case "0":
                return "salir"
            case _:
                print("Opción no válida.")
                return True


def crear_menu(usuario: Usuario) -> Menu:
    """instancia el menú correcto según el rol de forma polimórfica."""
    if usuario.rol == Rol.ADMIN:
        return MenuAdministrador(usuario)
    return MenuCliente(usuario)