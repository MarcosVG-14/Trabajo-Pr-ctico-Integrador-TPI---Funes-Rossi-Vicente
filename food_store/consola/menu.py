from abc import ABC, abstractmethod
from entidades.usuario import Usuario
from enums.enums import Rol
from servicios.categoriaservicio import listar, crear_categoria, editar_categoria, eliminar_categoria, input_seleccion, input_str, input_int
from excepciones.excepciones import OperacionNoPermitidaError

class Menu(ABC):
    def __init__(self, usuario: Usuario) -> None:
        self.__usuario: Usuario = usuario
    
    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @abstractmethod
    def mostrar(self) -> bool:
        pass


class MenuAdministrador(Menu):
    def __init__(self, usuario: Usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio) -> None:
        super().__init__(usuario)
        self.categoria_servicio = categoria_servicio
        self.producto_servicio = producto_servicio
        self.usuario_servicio = usuario_servicio
        self.pedido_servicio = pedido_servicio

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
            case "0":
                return "salir"
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
                            if self.usuario.rol in (Rol.ADMIN, Rol.USUARIO):
                                listar(self.categoria_servicio)
                        case 2 | "2" | "dos" | "ii" | "crear":
                            if self.usuario.rol == Rol.ADMIN:
                                nombre = input_str("Escriba el nombre de la categoria: ", "Nombre")
                                descripcion = input_str("Escriba la descripción de la categoria: ", "Descripción")
                                crear_categoria(nombre, descripcion, self.categoria_servicio)
                                print("¡Categoría creada con éxito!")
                            else:
                                print("Usted no tiene los permisos necesarios.")
                        case 3 | "3" | "tres" | "iii" | "editar":
                            if self.usuario.rol == Rol.ADMIN:
                                _id = input_int("Escriba el ID de la categoria que desea buscar: ","ID")
                                editar_categoria(_id, self.categoria_servicio, self.pedido_servicio)
                            else:
                                print("Usted no tiene los permisos necesarios.")
                        case 4 | "4" | "cuatro" | "iv" | "eliminar":
                            if self.usuario.rol == Rol.ADMIN:
                                _id = input_int("Escriba el ID de la categoria que desea buscar: ","ID")
                                eliminar_categoria(_id, self.categoria_servicio, self.pedido_servicio)
                            else:
                                print("Usted no tiene los permisos necesarios.")
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
                    seleccion = input("Seleccione: ").strip()
                    match seleccion:
                        case "1" | "uno" | "i" | "listar":
                            if self.usuario.rol == Rol.ADMIN:
                                usuarios = self.usuario_servicio.usuarios_activos()
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
                            if self.usuario.rol == Rol.ADMIN:
                                nombre = input("Ingrese el nombre del usuario: ").strip()
                                apellido = input("Ingrese el apellido del usuario: ").strip()
                                mail = input("Ingrese el mail del usuario: ").strip()
                                celular = input("Ingrese el celular del usuario: ").strip()
                                contrasenia = input("Ingrese la contraseña del usuario: ").strip()
                                rol = int(input("Ingrese el rol del usuario (1 = Admin | 2 = Usuario): ").strip())
                                self.usuario_servicio.crear_usuario(nombre, apellido, mail, celular, contrasenia, rol)
                                print("Usuario creado exitosamente.")
                            else:
                                print("Usted no tiene los permisos necesarios.")
                        case "4" | "cuatro" | "iv" | "eliminar":
                            if self.usuario.rol == Rol.ADMIN:
                                _id = input_int("Escriba el ID del usuario que desea buscar: ", "ID")
                                
                                # Valida que el usuario exista antes de confirmar
                                usuario_a_borrar = self.usuario_servicio.buscar_por_id(_id)
                                
                                if usuario_a_borrar.id == self.usuario.id:
                                    raise OperacionNoPermitidaError("No puedes borrarte a tí mismo.")
                                
                                confirmacion = input(f"¿Estás seguro de dar la baja lógica al usuario {usuario_a_borrar.nombre} (ID {_id})? (S/N): ").strip().lower()
                                if confirmacion == "s":
                                    self.usuario_servicio.eliminar_usuario(_id)
                                    print(f"Se eliminó al usuario de ID '{_id}'")
                                else:
                                    print("Acción cancelada.")
                            else:
                                print("Usted no tiene los permisos necesarios.")
                        case "0" | "cero" | "o" | "zero" | "volver":
                            print("Regresando...")
                            break

            case "9":
                return False

            case _:
                print("Opción no válida.")
                return True
        return True


class MenuCliente(Menu):
    def __init__(self, usuario: Usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio) -> None:
        super().__init__(usuario)
        self.categoria_servicio = categoria_servicio
        self.producto_servicio = producto_servicio
        self.usuario_servicio = usuario_servicio
        self.pedido_servicio = pedido_servicio

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
            case "0":
                return "salir"

            case "1":
                while True:
                    print("""--- CATEGORÍAS ---
1. Listar
0. Volver""")
                    seleccion = input_seleccion("Seleccione: ")
                    match seleccion:
                        case 1 | "1" | "uno" | "i" | "listar":
                            listar(self.categoria_servicio)
                        case 0 | "0" | "cero" | "o" | "zero" | "volver":
                            print("Regresando...")
                            break

            case "9":
                print("Cerrando sesión de cliente...")
                return False

            case _:
                print("Opción no válida.")
                return True
        return True


def crear_menu(usuario: Usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio) -> Menu:
    """Instancia el menú correcto según el rol de forma polimórfica."""
    if usuario.rol == Rol.ADMIN:
        return MenuAdministrador(usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio)
    return MenuCliente(usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio)