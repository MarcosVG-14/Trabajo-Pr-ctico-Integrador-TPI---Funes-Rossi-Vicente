from abc import ABC, abstractmethod
from entidades.usuario import Usuario
from enums.enums import Rol, Estado, FormaPago
from servicios.categoriaservicio import input_seleccion, input_str, input_int
from servicios.productoservicio import listar_producto_admin, listar_producto_cliente, crear_producto, editar_producto, eliminar_producto, input_float, input_bool, asignar_categoria
from excepciones.excepciones import FoodStoreError, OperacionNoPermitidaError
import os

# Definición de colores ANSI
RESET = "\033[0m"
NEGRITA = "\033[1m"

# Colores de texto
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BLANCO = "\033[37m"

'''Función que regula la ejecución del programa para mantener un orden y tempo'''
def continuar():
    print()
    input("""-- Presione cualquier tecla para continuar --
""")

'''Función que limpia la consola para que se vea mejor'''
def limpiado_consola():
    if os.name == 'nt':
        os.system('cls') 

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
        print(f"{VERDE}1.{AZUL} Categorías{RESET}")
        print(f"{VERDE}2.{AZUL} Productos{RESET}")
        print(f"{VERDE}3.{AZUL} Usuarios{RESET}")
        print(f"{VERDE}4.{AZUL} Pedidos{RESET}")
        print(f"{VERDE}9.{AZUL} Cerrar sesión{RESET}")
        print(f"{ROJO}0.{AZUL} Salir{RESET}")
        
        opcion = input("Seleccione una opción: ").strip()
        
        match opcion:
            case "0":
                return "salir"
            case "1":
                while True:
                    print(f"""--- CATEGORÍAS ---
{VERDE}1.{AZUL} Listar{RESET}
{VERDE}2.{AZUL} Crear{RESET}
{VERDE}3.{AZUL} Editar{RESET}
{VERDE}4.{AZUL} Eliminar{RESET}
{ROJO}0.{AZUL} Volver{RESET}""")
                    try:
                        seleccion = input_seleccion(f"{AMARILLO}Seleccione: {RESET}")
                        match seleccion:
                            case 1 | "1" | "uno" | "i" | "listar":
                                self.categoria_servicio.listar_categoria()
                            case 2 | "2" | "dos" | "ii" | "crear":
                                nombre = input_str("Escriba el nombre de la categoria: ", "Nombre")
                                descripcion = input_str("Escriba la descripción de la categoria: ", "Descripción")
                                res = self.categoria_servicio.crear_categoria(nombre, descripcion)
                                print(res)
                            case 3 | "3" | "tres" | "iii" | "editar":
                                _id = input_int("Escriba el ID de la categoria que desea buscar: ","ID")
                                self.categoria_servicio.editar_categoria(_id, self.pedido_servicio)
                            case 4 | "4" | "cuatro" | "iv" | "eliminar":
                                _id = input_int("Escriba el ID de la categoria que desea buscar: ","ID")
                                self.categoria_servicio.eliminar_categoria(_id, self.pedido_servicio)
                            case 0 | "0" | "cero" | "o" | "zero" | "volver":
                                print(f"{ROJO}Regresando...{RESET}")
                                break
                    except FoodStoreError as e:
                        print(f"\n[Error de Negocio]: {e}")
                    except ValueError as e:
                        print(f"\n[Error de Formato]: {e}")

            case "2" | "dos":
                while True:
                    print(f"""--- PRODUCTOS ---
{VERDE}1.{AZUL} Listar{RESET}
{VERDE}2.{AZUL} Crear{RESET}
{VERDE}3.{AZUL} Editar{RESET}
{VERDE}4.{AZUL} Eliminar{RESET}
{VERDE}5.{AZUL} Asignar una categoria a un producto{RESET}
{ROJO}0.{AZUL} Volver{RESET}""")
                    try:
                        seleccion = input_seleccion(f"{AMARILLO}Seleccione: {RESET}")
                        match seleccion:
                            case 1 | "1" | "uno" | "i" | "listar":
                                listar_producto_admin(self.producto_servicio)
                            case 2 | "2" | "dos" | "ii" | "crear":
                                nombre = input_str("Escriba el nombre del nuevo producto: ", "Nombre")
                                precio = input_float("Escriba el precio del nuevo producto: ", "Precio")
                                descripcion = input_str("Escriba la descripcion del nuevo producto: ", "Descripcion")
                                stock = input_int("Escriba el stock inicial del nuevo producto: ", "Stock")
                                imagen = input_str("Ingrese el url de la imagen del producto: ", "Imagen")
                                disponible = input_bool("¿El producto esta disponible?: ")
                                res = crear_producto(nombre, precio, descripcion, stock, imagen, disponible, self.producto_servicio)
                                print(res)
                            case 3 | "3" | "tres" | "iii" | "editar":
                                _id = input_int("Escriba el ID del producto que desea buscar: ","ID")
                                editar_producto(_id, self.producto_servicio, self.pedido_servicio)
                            case 4 | "4" | "cuatro" | "iv" | "eliminar":
                                _id = input_int("Escriba el ID del producto que desea buscar: ","ID")
                                eliminar_producto(_id, self.producto_servicio, self.pedido_servicio)
                            case 5 | "5" | "cinco" | "v" | "asignar":
                                _id = input_int("Escriba el ID del producto que desea buscar: ", "ID del producto")
                                asignar_categoria(_id, self.producto_servicio, self.pedido_servicio, self.categoria_servicio)
                            case 0 | "0" | "cero" | "o" | "zero" | "volver":
                                print(f"{ROJO}Regresando...{RESET}")
                                break
                            case _:
                                print("Ingrese una opcion mostrada en pantalla.")
                    except FoodStoreError as e:
                        print(f"\n[Error de Negocio]: {e}")
                    except ValueError as e:
                        print(f"\n[Error de Formato]: {e}")

            case "3" | "tres":
                while True:
                    print(f"""--- USUARIOS ---
{VERDE}1.{AZUL} Listar{RESET}
{VERDE}2.{AZUL} Crear{RESET}
{VERDE}3.{AZUL} Editar{RESET}
{VERDE}4.{AZUL} Eliminar{RESET}
{VERDE}5.{AZUL} Mis datos{RESET}
{ROJO}0.{AZUL} Volver{RESET}""")
                    try:
                        seleccion = input("Seleccione: ").strip()
                        limpiado_consola()
                        match seleccion:
                            case "1" | "uno" | "i" | "listar":
                                usuarios = self.usuario_servicio.usuarios_activos()
                                if not usuarios:
                                    print("No hay usuarios cargados.")
                                    continuar()
                                    limpiado_consola()
                                else:
                                    for usuario in usuarios:
                                        print(f"""Id: {usuario.id}
Nombre: {usuario.nombre}
Apellido: {usuario.apellido}
Mail: {usuario.mail}
Rol: {usuario.rol.name}
-------------------------""")
                                    continuar()
                                    limpiado_consola()

                            case "2" | "dos" | "ii" | "crear":
                                nombre = input_str("Ingrese el nombre: ", "Nombre").strip()
                                apellido = input_str("Ingrese el apellido: ", "Apellido").strip()
                                mail = input_str("Ingrese el mail: ", "Mail").strip()
                                celular = input("Ingrese el celular: ").strip()
                                contrasenia = input("Ingrese la contraseña: ").strip()
                                rol = input_int("Ingrese rol (1 = Admin | 2 = Usuario): ", "Rol")
                                self.usuario_servicio.crear_usuario(nombre, apellido, mail, celular, contrasenia, rol)
                                print("Usuario creado exitosamente.")
                                continuar()
                                limpiado_consola()

                            case "3" | "tres" | "iii" | "editar":
                                _id = input_int("Escriba el ID del usuario que desea buscar: ", "ID")
                                usuario_a_editar = self.usuario_servicio.buscar_por_id(_id)
                                
                                # Submenú de edición con el formato integrado
                                editando = True
                                while editando:
                                    print(f"""\n{CYAN}- Usted accedió al Usuario de ID {_id}{RESET}
- {usuario_a_editar.nombre} {usuario_a_editar.apellido}
¿Qué valor le gustaría actualizar?

{VERDE}1.{AZUL} Nombre{RESET}
{VERDE}2.{AZUL} Apellido{RESET}
{VERDE}3.{AZUL} Mail{RESET}
{VERDE}4.{AZUL} Celular{RESET}
{VERDE}5.{AZUL} Contraseña{RESET}
{VERDE}6.{AZUL} Rol{RESET}
{ROJO}8.{AZUL} Salir / Volver{RESET}

Seleccione una opción: """, end="")
                                    opcion_editar = input().strip()

                                    if opcion_editar == "8":
                                        editando = False
                                        break

                                    match opcion_editar:
                                        case "1" | "uno" | "i" | "nombre":
                                            nuevo_nombre = input_str("Ingrese el nuevo nombre: ", "Nombre")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{RESET} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_nombre(usuario_a_editar, nuevo_nombre)
                                                print("Nombre de usuario cambiado.")
                                            else:
                                                print("Acción cancelada.")
                                            continuar()
                                            limpiado_consola()

                                        case "2" | "dos" | "ii" | "apellido":
                                            nuevo_apellido = input_str("Ingrese el nuevo apellido: ", "Apellido")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{RESET} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_apellido(usuario_a_editar, nuevo_apellido)
                                                print("Apellido de usuario cambiado.")
                                            else:
                                                print("Acción cancelada.")
                                            continuar()
                                            limpiado_consola()

                                        case "3" | "tres" | "iii" | "mail":
                                            nuevo_mail = input_str("Ingrese el nuevo mail: ", "Mail")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{RESET} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                try: 
                                                    self.usuario_servicio.cambio_mail(usuario_a_editar, nuevo_mail)
                                                    print("Mail de usuario cambiado.")
                                                except TypeError as e:
                                                    print(e)
                                            else:
                                                print("Acción cancelada.")
                                            continuar()
                                            limpiado_consola()

                                        case "4" | "cuatro" | "iv" | "celular":
                                            nuevo_celular = input_str("Ingrese el nuevo celular: ", "Celular")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{RESET} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_celular(usuario_a_editar, nuevo_celular)
                                                print("Celular de usuario cambiado.")
                                            else:
                                                print("Acción cancelada.")
                                            continuar()
                                            limpiado_consola()

                                        case "5" | "cinco" | "v" | "contraseña":
                                            nueva_contrasenia = input_str("Ingrese la nueva contraseña: ", "Contraseña")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{RESET} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_contrasenia(usuario_a_editar, nueva_contrasenia)
                                                print("Contraseña de usuario cambiada.")
                                            else:
                                                print("Acción cancelada.")
                                            continuar()
                                            limpiado_consola()

                                        case "6" | "seis" | "vi" | "rol":
                                            nuevo_rol = input_int("Ingrese el nuevo rol (1 = Admin | 2 = Usuario): ", "Rol")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{RESET} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_rol(usuario_a_editar, nuevo_rol)
                                                print("Rol de usuario cambiado.")
                                            else:
                                                print("Acción cancelada.")
                                            continuar()
                                            limpiado_consola()

                                        case _:
                                            print("Error... Comando incorrecto")
                                            continuar()
                                            limpiado_consola()

                            case "4" | "cuatro" | "iv" | "eliminar":
                                _id = input_int("Escriba el ID del usuario: ", "ID")
                                usuario_a_borrar = self.usuario_servicio.buscar_por_id(_id)
                                if usuario_a_borrar.id == self.usuario.id:
                                    raise OperacionNoPermitidaError("No puedes borrarte a tí mismo.")
                                
                                confirmacion = input(f"{ROJO}¿Dar baja lógica a {usuario_a_borrar.nombre}? (S/N):{RESET} ").strip().lower()
                                if confirmacion in ["si", "s"]:
                                    self.usuario_servicio.eliminar_usuario(_id)
                                    print(f"Usuario {_id} eliminado.")
                                else:
                                    print(f"Usuario {_id} no ha sido eliminado.")
                                continuar()
                                limpiado_consola()

                            case "5" | "cinco" | "v" | "datos":
                                print(f"""Id: {self.usuario.id}
Nombre: {self.usuario.nombre}
Apellido: {self.usuario.apellido}
Mail: {self.usuario.mail}
Rol: {self.usuario.rol.name}
-------------------------""")
                                continuar()
                                limpiado_consola()

                            case 0 | "0" | "cero" | "o" | "zero" | "volver":
                                print("Volviendo...")
                                break
                    except FoodStoreError as e:
                        print(f"\n{ROJO}[Error de Negocio]: {e}{RESET}")
                        continuar()
                        limpiado_consola()
                    except ValueError as e:
                        print(f"\n{ROJO}[Error de Formato]: {e}{RESET}")
                        continuar()
                        limpiado_consola()
            case "4" | "cuatro":
                while True:
                    print(f"""--- GESTIÓN DE PEDIDOS ---
{VERDE}1.{AZUL} Listar todos los pedidos{RESET}
{VERDE}2.{AZUL} Crear nuevo pedido{RESET}
{VERDE}3.{AZUL} Cambiar estado de pedido{RESET}
{VERDE}4.{AZUL} Eliminar pedido (Baja lógica){RESET}
{ROJO}0.{AZUL} Volver{RESET}""")
                    try:
                        seleccion = input("Seleccione: ").strip()
                        match seleccion:
                            case "1":
                                pedidos = self.pedido_servicio.listar_pedidos_activos()
                                if not pedidos:
                                    print("No hay pedidos registrados.")
                                else:
                                    for p in pedidos:
                                        print(p)
                                        print("  Detalles:")
                                        for d in p.detalles:
                                            print(f"   - {d.producto.nombre if d.producto else 'Producto Eliminado'} x {d.cantidad} (Subtotal: ${d.subtotal:.2f})")
                                        print("-" * 40)
                            case "2":
                                print("\n--- CREAR PEDIDO ---")
                                id_usu = input_int("Ingrese el ID del usuario cliente: ", "ID Usuario")
                                usu = self.usuario_servicio.buscar_por_id(id_usu)
                                
                                print("\nFormas de pago disponibles:")
                                print("1. TARJETA\n2. TRANSFERENCIA\n3. EFECTIVO")
                                op_pago = input_int("Seleccione forma de pago (1-3): ", "Opción")
                                forma_pago = FormaPago.TARJETA if op_pago == 1 else (FormaPago.TRANSFERENCIA if op_pago == 2 else FormaPago.EFECTIVO)
                                
                                items = []
                                while True:
                                    print("\nProductos disponibles:")
                                    for prod in self.producto_servicio.productos:
                                        if not prod.eliminado and prod.disponible:
                                            print(f"ID: {prod.id} | {prod.nombre} - Precio: ${prod.precio} - Stock: {prod.stock}")
                                    
                                    id_prod = input_int("Ingrese el ID del producto (0 para terminar): ", "ID Producto")
                                    if id_prod == 0:
                                        break
                                    
                                    prod_encontrado = None
                                    for prod in self.producto_servicio.productos:
                                        if prod.id == id_prod and not prod.eliminado:
                                            prod_encontrado = prod
                                            break
                                    
                                    if not prod_encontrado:
                                        print("Producto no encontrado.")
                                        continue
                                    
                                    cant = input_int(f"Ingrese la cantidad para '{prod_encontrado.nombre}': ", "Cantidad")
                                    items.append((cant, prod_encontrado))
                                
                                if items:
                                    nuevo_ped = self.pedido_servicio.crear_pedido(usu, forma_pago, items)
                                    print(f"¡Pedido creado con éxito! ID: {nuevo_ped.id} | Total: ${nuevo_ped.total:.2f}")
                                else:
                                    print("No se agregaron items, pedido cancelado.")
                            case "3":
                                id_ped = input_int("Ingrese el ID del pedido a actualizar: ", "ID Pedido")
                                print("\nNuevos estados:")
                                print("1. PENDIENTE\n2. CONFIRMADO\n3. TERMINADO\n4. CANCELADO")
                                op_est = input_int("Seleccione nuevo estado (1-4): ", "Opción")
                                nuevo_estado = (Estado.PENDIENTE if op_est == 1 else 
                                                Estado.CONFIRMADO if op_est == 2 else 
                                                Estado.TERMINADO if op_est == 3 else Estado.CANCELADO)
                                self.pedido_servicio.cambiar_estado(id_ped, nuevo_estado)
                                print("¡Estado del pedido actualizado con éxito!")
                            case "4":
                                id_ped = input_int("Ingrese el ID del pedido a eliminar: ", "ID Pedido")
                                if input("¿Confirma la baja lógica del pedido? (S/N): ").strip().lower() == "s":
                                    self.pedido_servicio.eliminar_pedido(id_ped)
                                    print("Pedido eliminado correctamente.")
                            case "0":
                                break
                    except FoodStoreError as e:
                        print(f"\n[Error de Negocio]: {e}")
                    except ValueError as e:
                        print(f"\n[Error de Formato]: {e}")

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
        print(f"{VERDE}1.{AZUL} Ver categorías{RESET}")
        print(f"{VERDE}2.{AZUL} Ver productos disponibles{RESET}")
        print(f"{VERDE}3.{AZUL} Mis pedidos{RESET}")
        print(f"{VERDE}4.{AZUL} Mis datos{RESET}")
        print(f"{VERDE}9.{AZUL} Cerrar sesión{RESET}")
        print(f"{ROJO}0.{AZUL} Salir{RESET}")
        
        opcion = input("Seleccione una opción: ").strip()
        
        try:
            match opcion:
                case "0":
                    return "salir"

                case "1" | "uno":
                    self.categoria_servicio.listar_categoria()

                case "2" | "dos":
                    listar_producto_cliente(self.producto_servicio)

                case "3":
                    while True:
                        print(f"\n--- MIS PEDIDOS ({self.usuario.nombre}) ---")
                        mis_pedidos = self.pedido_servicio.listar_pedidos_por_usuario(self.usuario)
                        if not mis_pedidos:
                            print("No tenés pedidos registrados.")
                            break
                        for p in mis_pedidos:
                            print(f"ID: {p.id} | Fecha: {p.fecha} | Estado: {p.estado.name} | Pago: {p.forma_pago.name} | Total: ${p.total:.2f}")
                        
                        id_elegido = input_int("Ingrese el ID de un pedido para ver sus detalles (0 para volver): ", "ID")
                        if id_elegido == 0:
                            break
                        
                        encontrado = False
                        for p in mis_pedidos:
                            if p.id == id_elegido:
                                encontrado = True
                                print(f"\nDetalles del Pedido #{p.id}:")
                                for d in p.detalles:
                                    prod_nombre = d.producto.nombre if d.producto else "Producto eliminado"
                                    prod_precio = d.producto.precio if d.producto else 0.0
                                    print(f" - {prod_nombre}: {d.cantidad} un. x ${prod_precio} = ${d.subtotal:.2f}")
                                print(f"TOTAL: ${p.total:.2f}")
                        if not encontrado:
                            print("El ID ingresado no corresponde a ninguno de tus pedidos.")

                case "4":
                    print(f"\n--- MIS DATOS ---")
                    print(f"Nombre: {self.usuario.nombre} {self.usuario.apellido}")
                    print(f"Mail: {self.usuario.mail}")
                    print(f"Celular: {self.usuario.celular}")
                    print(f"Rol: {self.usuario.rol.name}")

                case "9":
                    print("Cerrando sesión de cliente...")
                    return False

                case _:
                    print("Opción no válida.")
        except FoodStoreError as e:
            print(f"\n[Error de Negocio]: {e}")
        except ValueError as e:
            print(f"\n[Error de Formato]: {e}")

        return True


def crear_menu(usuario: Usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio) -> Menu:
    """Instancia el menú correcto según el rol de forma polimórfica."""
    if usuario.rol == Rol.ADMIN:
        return MenuAdministrador(usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio)
    return MenuCliente(usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio)