
from abc import ABC, abstractmethod
from entidades.usuario import Usuario
from enums.enums import Rol
from servicios.categoriaservicio import *
from servicios.usuario_servicio import *

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
                return "Saliendo del menú..."
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
                                listar(categoriaservicio1)
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
            
            case "3" | "tres":
                while True:
                    print("""--- USUARIOS ---
1. Listar
2. Crear
3. Editar
4. Eliminar
0. Volver""")
                    seleccion = input("Seleccione: ")
                    match seleccion:
                        case "1" | "uno" | "i" | "listar":
                            if sesion_activa.rol.value == "Admin" or sesion_activa.rol.value == "Usuario":
                                usuarios = usuario_servicio.usuarios_activos()
                                if not usuarios:
                                    print("No hay usuarios cargados.")
                                else:
                                    for usuario in usuarios:
                                        print(f"""Id: {usuario.id}
Nombre: {usuario.nombre}
Apellido: {usuario.apellido}
Mail: {usuario.mail}
Rol: {usuario.rol.name}
-------------------------""")
                        case "2" | "dos" | "ii" | "crear":
                            if sesion_activa.rol.value == "Admin":
                                while True:
                                    nombre = input("Ingrese el nombre del usuario: ").strip()
                                    apellido = input("Ingrese el apellido del usuario: ").strip()
                                    mail = input("Ingrese el mail del usuario: ").strip()
                                    celular = input("Ingrese el celular del usuario: ").strip()
                                    contrasenia = input("Ingrese el contraseña del usuario: ").strip()
                                    rol = input("Ingrese el rol del usuario (1 = Admin | 2 = Usuario): ").strip()
                                    usuario_servicio.crear_usuario(nombre, apellido, mail, celular, contrasenia, rol)
                                    print(f"Usuario creado exitosamente. ID asignado: {nuevo_usuario.id}")
                                    break
                            else:
                                print("Usted no tiene los permisos necesarios para realizar esta opcion.")
                        case "3" | "tres" | "iii" | "editar":
                            if sesion_activa.rol.value == "Admin":
                                _id = input_int("Escriba el ID de la categoria que desea buscar: ", "ID")
                                usuario_a_editar = usuario_servicio.buscar_por_id(_id)
                                while True:
                                    opcion = print(f""" - Usted accedó al Usuario de ID {_id} - {usuario_a_editar.nombre} {usuario_a_editar.nombre} - 
    ¿Qué valor le gustaría actualizar?

1- Nombre
2- Apellido
3- Mail
4- Celular
5- Contraseña
6- Rol
7- Todos
8- Salir


    Seleccione una opción: """)
                                    match opcion:
                                        case "1" | "uno" | "i" | "nombre":
                                            nuevo_nombre = input_str("Ingrese el nuevo nombre: ")
                                            confirmacion = input("""¿Estás seguro de hacer cambio?
- SI 
- NO

    - """)
                                    while True:
                                        match confirmacion:
                                            case "si" | "SI" | "Si":
                                                usuario.nombre = nuevo_nombre
                                                print("Nombre de usuario cambiado.")
                                                break
                                            case "no" | "NO" | "No":
                                                print("Acción cancelada.")
                                                break
                                            case _:
                                                print("Error... Comando incorrecto")
                            else:
                                print("Usted no tiene los permisos necesarios para realizar esta opcion.")


                                
                        case "4" | "cuatro" | "iv" | "eliminar":
                            if sesion_activa.rol.value == "Admin":
                                _id = input_int("Escriba el ID del usuario que desea buscar: ", "ID")
                                usuario_a_borrar = usuario_servicio.buscar_por_id(_id)
                                if usuario_a_borrar == sesion_activa.id:
                                    raise OperacionNoPermitidaError("No puedes borrarte a tí mismo.")
                                if _id:
                                    opcion = input(f"""¿Estás seguro de dar la baja lógica al usuario de id {usuario_a_borrar}?
- Si
- No        
    
    - """)
                                    while True: 
                                        match opcion:
                                            case "si" | "SI" | "Si":
                                                usuario_servicio.eliminar_usuario(usuario_a_borrar)
                                                print(f"Se eliminó al usuario de ID '{usuario_a_borrar}'")
                                                break
                                            case "no" | "NO" | "No":
                                                print("Acción cancelada.")
                                                break
                                            case _:
                                                print("Error... Comando incorrecto")
                                else:
                                    print(f"El ID {_id} no fue encontrado en la lista.")
                            else:
                                print("Usted no tiene los permisos necesarios para realizar esta opcion.")
                        
                        case "5" | "cinco" | "v" | "datos":
                            if sesion_activa.rol.value == "Admin":
                                _id = input_int("Escriba el ID del usuario que desea buscar: ", "ID")
                                usuario = usuario_servicio.buscar_por_id(_id)
                                if usuario:
                                    print(f"""Id: {usuario.id}
    Nombre: {usuario.nombre}
    Apellido: {usuario.apellido}
    Mail: {usuario.mail}
    Rol: {usuario.rol.name}
    -------------------------""")
                                else:
                                    print(f"El ID {usuario} no fue encontrado en la lista.")
                        case "0" | "cero" | "o" | "zero" | "volver":
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
                                listar(categoriaservicio1)
                        case 0 | "0" | "cero" | "o" | "zero" | "volver":
                            print("Regresando...")
                            break


def crear_menu(usuario: Usuario) -> Menu:
    """instancia el menú correcto según el rol de forma polimórfica."""
    if usuario.rol == Rol.ADMIN:
        return MenuAdministrador(usuario)
    return MenuCliente(usuario)