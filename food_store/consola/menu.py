
from abc import ABC, abstractmethod
from entidades.usuario import Usuario
from servicios.categoriaservicio import *
from enums.enums import FormaPago, Rol, Estado
from servicios.categoriaservicio import Categoriaservicio
from datetime import datetime

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
            case "1":
                while True:
                    print("""--- CATEGORÍAS ---
1. Listar
2. Crear
3. Editar
4. Eliminar
0. Volver""")
                    seleccion = input_seleccion("Seleccione: ")
                    match seleccion:
                        case 1 | "1" | "uno" | "i" | "listar":
                            if sesion_activa.rol.value == "Admin" or sesion_activa.rol.value == "Usuario":
                                listar_categoria(categoriaservicio1)
                        case 2 | "2" | "dos" | "ii" | "crear":
                            if sesion_activa.rol.value == "Admin":
                                nombre = input_str("Escriba el nombre de la categoria: ", "Nombre")
                                descripcion = input_str("Escriba la descripción de la categoria: ", "Descripción")
                                crear_categoria(nombre, descripcion, categoriaservicio1)
                            else:
                                print("Usted no tiene los permisos necesarios para realizar esta opcion.")
                        case 3 | "3" | "tres" | "iii" | "editar":
                            if sesion_activa.rol.value == "Admin":
                                _id = input_int("Escriba el ID de la categoria que desea buscar: ","ID")
                                editar_categoria(_id, categoriaservicio1, pedido1)
                            else:
                                print("Usted no tiene los permisos necesarios para realizar esta opcion.")
                        case 4 | "4" | "cuatro" | "iv" | "eliminar":
                            if sesion_activa.rol.value == "Admin":
                                _id = input_int("Escriba el ID de la categoria que desea buscar: ","ID")
                                eliminar_categoria(_id, categoriaservicio1, pedido1)
                            else:
                                print("Usted no tiene los permisos necesarios para realizar esta opcion.")
                        case 0 | "0" | "cero" | "o" | "zero" | "volver":
                            print("Regresando...")
                            break

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
            case "1":
                while True:
                    print("""--- CATEGORÍAS ---
1. Listar
0. Volver""")
                    seleccion = input_seleccion("Seleccione: ")
                    match seleccion:
                        case 1 | "1" | "uno" | "i" | "listar":
                            if sesion_activa.rol.value == "Admin" or sesion_activa.rol.value == "Usuario":
                                listar_categoria(categoriaservicio1)
                        case 0 | "0" | "cero" | "o" | "zero" | "volver":
                            print("Regresando...")
                            break

def crear_menu(usuario: Usuario) -> Menu:
    """instancia el menú correcto según el rol de forma polimórfica."""
    if usuario.rol == Rol.ADMIN:
        return MenuAdministrador(usuario)
    return MenuCliente(usuario)