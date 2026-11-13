from abc import ABC, abstractmethod
from entidades.usuario import Usuario
from enums.enums import Rol, Estado, FormaPago
from servicios.categoriaservicio import input_seleccion, input_str, input_int_id
from servicios.productoservicio import listar_producto_admin, listar_producto_cliente, crear_producto, editar_producto, eliminar_producto, input_float, input_bool, asignar_categoria, input_int
from excepciones.excepciones import FoodStoreError, OperacionNoPermitidaError
from consola.estetica import *

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
        print(f"{AZUL}\n=== FOOD STORE ADMINISTRADOR ({MORADO}{self.usuario.nombre} {MORADO}{self.usuario.apellido}{AZUL}) ==={RESET}")
        print(f"{VERDE}1.{AZUL} Categorías{RESET}")
        print(f"{VERDE}2.{AZUL} Productos{RESET}")
        print(f"{VERDE}3.{AZUL} Usuarios{RESET}")
        print(f"{VERDE}4.{AZUL} Pedidos{RESET}")
        print(f"{VERDE}9.{AZUL} Cerrar sesión{RESET}")
        print(f"{ROJO}0.{AZUL} Salir{RESET}")
        
        opcion = input(f"{AMARILLO}Seleccione una opción: {RESET}").strip()
        
        match opcion:
            case "0":
                return "salir"
            case "1":
                while True:
                    print(f"""{AZUL}--- CATEGORÍAS ---{RESET}
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
                                nombre = input_str(f"{AMARILLO}Escriba el nombre de la categoria: {RESET}", "Nombre")
                                descripcion = input_str(f"{AMARILLO}Escriba la descripción de la categoria: {RESET}", "Descripción")
                                res = self.categoria_servicio.crear_categoria(nombre, descripcion)
                                print(res)
                            case 3 | "3" | "tres" | "iii" | "editar":
                                _id = input_int_id(f"{AMARILLO}Escriba el ID de la categoria que desea buscar: {RESET}","ID")
                                self.categoria_servicio.editar_categoria(_id, self.pedido_servicio)
                            case 4 | "4" | "cuatro" | "iv" | "eliminar":
                                _id = input_int_id(f"{AMARILLO}Escriba el ID de la categoria que desea buscar: {RESET}","ID")
                                self.categoria_servicio.eliminar_categoria(_id, self.pedido_servicio)
                            case 0 | "0" | "cero" | "o" | "zero" | "volver":
                                print(f"{ROJO}Regresando...{RESET}")
                                break
                    except FoodStoreError as e:
                        print(f"{NARANJA}\n[Error de Negocio]: {e}{RESET}")
                    except ValueError as e:
                        print(f"{NARANJA}\n[Error de Formato]: {e}{RESET}")

            case "2" | "dos":
                while True:
                    print(f"""{AZUL}--- PRODUCTOS ---{RESET}
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
                                nombre = input_str(f"{AMARILLO}Escriba el nombre del nuevo producto: {RESET}", "Nombre")
                                precio = input_float(f"{AMARILLO}Escriba el precio del nuevo producto: {RESET}", "Precio")
                                descripcion = input_str(f"{AMARILLO}Escriba la descripcion del nuevo producto: {RESET}", "Descripcion")
                                stock = input_int(f"{AMARILLO}Escriba el stock inicial del nuevo producto: {RESET}", "Stock")
                                imagen = input_str(f"{AMARILLO}Ingrese el url de la imagen del producto: {RESET}", "Imagen")
                                disponible = input_bool(f"{AMARILLO}¿El producto esta disponible?: {RESET}")
                                res = crear_producto(nombre, precio, descripcion, stock, imagen, disponible, self.producto_servicio)
                                print(res)
                            case 3 | "3" | "tres" | "iii" | "editar":
                                _id = input_int(f"{AMARILLO}Escriba el ID del producto que desea buscar: {RESET}","ID")
                                editar_producto(_id, self.producto_servicio, self.pedido_servicio)
                            case 4 | "4" | "cuatro" | "iv" | "eliminar":
                                _id = input_int(f"{AMARILLO}Escriba el ID del producto que desea buscar: {RESET}","ID")
                                eliminar_producto(_id, self.producto_servicio, self.pedido_servicio)
                            case 5 | "5" | "cinco" | "v" | "asignar":
                                _id = input_int(f"{AMARILLO}Escriba el ID del producto que desea buscar: {RESET}", "ID del producto")
                                asignar_categoria(_id, self.producto_servicio, self.pedido_servicio, self.categoria_servicio)
                            case 0 | "0" | "cero" | "o" | "zero" | "volver":
                                print(f"{ROJO}Regresando...{RESET}")
                                break
                            case _:
                                print(f"{NARANJA}Ingrese una opcion mostrada en pantalla.{RESET}")
                    except FoodStoreError as e:
                        print(f"{NARANJA}\n[Error de Negocio]: {e}{RESET}")
                    except ValueError as e:
                        print(f"{NARANJA}\n[Error de Formato]: {e}{RESET}")
            case "3" | "tres":
                while True:
                    print(f"""{AZUL}--- USUARIOS ---{RESET}
{VERDE}1.{AZUL} Listar{RESET}
{VERDE}2.{AZUL} Crear{RESET}
{VERDE}3.{AZUL} Editar{RESET}
{VERDE}4.{AZUL} Eliminar{RESET}
{VERDE}5.{AZUL} Mis datos{RESET}
{ROJO}0.{AZUL} Volver{RESET}""")
                    try:
                        seleccion = input(f"{AMARILLO}Seleccione: {RESET}").strip()
                        limpiado_consola()
                        match seleccion:
                            case "1" | "uno" | "i" | "listar":
                                usuarios = self.usuario_servicio.usuarios_activos()
                                if not usuarios:
                                    print(f"{NARANJA}No hay usuarios cargados.{RESET}")
                                    continuar()
                                    limpiado_consola()
                                else:
                                    for usuario in usuarios:
                                        print(f"""{AZUL}Id: {MORADO}{usuario.id}{RESET}
{AZUL}Nombre: {MORADO}{usuario.nombre}{RESET}
{AZUL}Apellido: {MORADO}{usuario.apellido}{RESET}
{AZUL}Mail: {MORADO}{usuario.mail}{RESET}
{AZUL}Rol: {MORADO}{usuario.rol.name}{RESET}
-------------------------""")
                                    continuar()
                                    limpiado_consola()
                            case "2" | "dos" | "ii" | "crear":
                                nombre = input_str(f"{AMARILLO}Ingrese el nombre: {RESET}", "Nombre").strip()
                                apellido = input_str(f"{AMARILLO}Ingrese el apellido: {RESET}", "Apellido").strip()
                                mail = input_str(f"{AMARILLO}Ingrese el mail: {RESET}", "Mail").strip()
                                celular = input(f"{AMARILLO}Ingrese el celular: {RESET}").strip()
                                contrasenia = input(f"{AMARILLO}Ingrese la contraseña: {RESET}").strip()
                                rol = input_int(f"{AMARILLO}Ingrese rol (1 = Admin | 2 = Usuario): {RESET}", "Rol")
                                self.usuario_servicio.crear_usuario(nombre, apellido, mail, celular, contrasenia, rol)
                                print(f"{AZUL}Usuario creado exitosamente.{RESET}")
                                continuar()
                                limpiado_consola()
                            case "3" | "tres" | "iii" | "editar":
                                _id = input_int(f"{AMARILLO}Escriba el ID del usuario que desea buscar: {RESET}", "ID")
                                usuario_a_editar = self.usuario_servicio.buscar_por_id(_id)
                                editando = True
                                while editando:
                                    print(f"""{CYAN}- Usted accedió al Usuario de ID {_id}{RESET}
{AZUL}- {MORADO}{usuario_a_editar.nombre} {usuario_a_editar.apellido}{RESET}
{AZUL}¿Qué valor le gustaría actualizar?{RESET}

{VERDE}1.{AZUL} Nombre{RESET}
{VERDE}2.{AZUL} Apellido{RESET}
{VERDE}3.{AZUL} Mail{RESET}
{VERDE}4.{AZUL} Celular{RESET}
{VERDE}5.{AZUL} Contraseña{RESET}
{VERDE}6.{AZUL} Rol{RESET}
{ROJO}8.{AZUL} Salir / Volver{RESET}

{AMARILLO}Seleccione una opción: {RESET}""", end="")
                                    opcion_editar = input().strip()
                                    if opcion_editar == "8":
                                        editando = False
                                        break
                                    match opcion_editar:
                                        case "1" | "uno" | "i" | "nombre":
                                            nuevo_nombre = input_str(f"{AMARILLO}Ingrese el nuevo nombre: {RESET}", "Nombre")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{RESET} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_nombre(usuario_a_editar, nuevo_nombre)
                                                print(f"{AZUL}Nombre de usuario cambiado.{RESET}")
                                            else:
                                                print(f"{AZUL}Acción cancelada.{RESET}")
                                            continuar()
                                            limpiado_consola()
                                        case "2" | "dos" | "ii" | "apellido":
                                            nuevo_apellido = input_str(f"{AMARILLO}Ingrese el nuevo apellido: {RESET}", "Apellido")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO): {RESET}").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_apellido(usuario_a_editar, nuevo_apellido)
                                                print(f"{AZUL}Apellido de usuario cambiado.{RESET}")
                                            else:
                                                print(f"{AZUL}Acción cancelada.{RESET}")
                                            continuar()
                                            limpiado_consola()
                                        case "3" | "tres" | "iii" | "mail":
                                            nuevo_mail = input_str(f"{AMARILLO}Ingrese el nuevo mail: {RESET}", "Mail")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{RESET} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                try: 
                                                    self.usuario_servicio.cambio_mail(usuario_a_editar, nuevo_mail)
                                                    print(f"{AZUL}Mail de usuario cambiado.{RESET}")
                                                except TypeError as e:
                                                    print(e)
                                            else:
                                                print(f"{AZUL}Acción cancelada.{RESET}")
                                            continuar()
                                            limpiado_consola()
                                        case "4" | "cuatro" | "iv" | "celular":
                                            nuevo_celular = input_str(f"{AMARILLO}Ingrese el nuevo celular: {RESET}", "Celular")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{RESET} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_celular(usuario_a_editar, nuevo_celular)
                                                print(f"{AZUL}Celular de usuario cambiado.{RESET}")
                                            else:
                                                print(f"{AZUL}Acción cancelada.{RESET}")
                                            continuar()
                                            limpiado_consola()
                                        case "5" | "cinco" | "v" | "contraseña":
                                            nueva_contrasenia = input_str(f"{AMARILLO}Ingrese la nueva contraseña: {RESET}", "Contraseña")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{RESET} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_contrasenia(usuario_a_editar, nueva_contrasenia)
                                                print(f"{AZUL}Contraseña de usuario cambiada.{RESET}")
                                            else:
                                                print(f"{AZUL}Acción cancelada.{RESET}")
                                            continuar()
                                            limpiado_consola()
                                        case "6" | "seis" | "vi" | "rol":
                                            nuevo_rol = input_int(f"{AMARILLO}Ingrese el nuevo rol (1 = Admin | 2 = Usuario): {RESET}", "Rol")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{RESET} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_rol(usuario_a_editar, nuevo_rol)
                                                print(f"{AZUL}Rol de usuario cambiado.{RESET}")
                                            else:
                                                print(f"{AZUL}Acción cancelada.{RESET}")
                                            continuar()
                                            limpiado_consola()
                                        case _:
                                            print(f"{NARANJA}Error... Comando incorrecto{RESET}")
                                            continuar()
                                            limpiado_consola()
                            case "4" | "cuatro" | "iv" | "eliminar":
                                _id = input_int(f"{AMARILLO}Escriba el ID del usuario: {RESET}", "ID")
                                usuario_a_borrar = self.usuario_servicio.buscar_por_id(_id)
                                if usuario_a_borrar.id == self.usuario.id:
                                    raise OperacionNoPermitidaError(f"{NARANJA}No puedes borrarte a tí mismo.{RESET}")
                                confirmacion = input(f"{ROJO}¿Dar baja lógica a {usuario_a_borrar.nombre}? (S/N):{RESET} ").strip().lower()
                                if confirmacion in ["si", "s"]:
                                    self.usuario_servicio.eliminar_usuario(_id)
                                    print(f"{AZUL}Usuario {_id} eliminado.{RESET}")
                                else:
                                    print(f"{AZUL}Usuario {_id} no ha sido eliminado.{RESET}")
                                continuar()
                                limpiado_consola()
                            case "5" | "cinco" | "v" | "datos":
                                print(f"""{AZUL}Id: {MORADO}{self.usuario.id}{RESET}
{AZUL}Nombre: {MORADO}{self.usuario.nombre}{RESET}
{AZUL}Apellido: {MORADO}{self.usuario.apellido}{RESET}
{AZUL}Mail: {MORADO}{self.usuario.mail}{RESET}
{AZUL}Rol: {MORADO}{self.usuario.rol.name}{RESET}
{AZUL}-------------------------{RESET}""")
                                continuar()
                                limpiado_consola()
                            case 0 | "0" | "cero" | "o" | "zero" | "volver":
                                print(f"{ROJO}Volviendo...{RESET}")
                                break
                    except FoodStoreError as e:
                        print(f"\n{NARANJA}[Error de Negocio]: {e}{RESET}")
                        continuar()
                        limpiado_consola()
                    except ValueError as e:
                        print(f"\n{NARANJA}[Error de Formato]: {e}{RESET}")
                        continuar()
                        limpiado_consola()
            case "4" | "cuatro":
                while True:
                    print(f"""{AZUL}--- GESTIÓN DE PEDIDOS ---{RESET}
{VERDE}1.{AZUL} Listar todos los pedidos{RESET}
{VERDE}2.{AZUL} Crear nuevo pedido{RESET}
{VERDE}3.{AZUL} Cambiar estado de pedido{RESET}
{VERDE}4.{AZUL} Eliminar pedido (Baja lógica){RESET}
{ROJO}0.{AZUL} Volver{RESET}""")
                    try:
                        seleccion = input(f"{AMARILLO}Seleccione: {RESET}").strip()
                        match seleccion:
                            case "1":
                                pedidos = self.pedido_servicio.listar_pedidos_activos()
                                if not pedidos:
                                    print(f"{NARANJA}No hay pedidos registrados.{RESET}")
                                else:
                                    for p in pedidos:
                                        print(p)
                                        print(f"{AZUL}  Detalles:{RESET}")
                                        for d in p.detalles:
                                            print(f"{AZUL}   - {d.producto.nombre if d.producto else 'Producto Eliminado'} x {d.cantidad} (Subtotal: ${d.subtotal:.2f}){RESET}")
                                        print(f"{AZUL}-{RESET}" * 40)
                            case "2":
                                print(f"\n{AZUL}--- CREAR PEDIDO ---{RESET}")
                                id_usu = input_int_id(f"{AMARILLO}Ingrese el ID del usuario cliente: {RESET}", "ID Usuario")
                                usu = self.usuario_servicio.buscar_por_id(id_usu)
                                
                                print(f"\n{AZUL}Formas de pago disponibles:{RESET}")
                                print(f"{VERDE}1. {AZUL}TARJETA\n{VERDE}2. {AZUL}TRANSFERENCIA\n{VERDE}3. {AZUL}EFECTIVO{RESET}")
                                op_pago = input_int(f"{AMARILLO}Seleccione forma de pago (1-3): {RESET}", "Opción")
                                forma_pago = FormaPago.TARJETA if op_pago == 1 else (FormaPago.TRANSFERENCIA if op_pago == 2 else FormaPago.EFECTIVO)
                                
                                items = []
                                while True:
                                    print(f"\n{AZUL}Productos disponibles:{RESET}")
                                    for prod in self.producto_servicio.productos:
                                        if not prod.eliminado and prod.disponible:
                                            print(f"{AZUL}ID: {MORADO}{prod.id}{AZUL} | {MORADO}{prod.nombre}{AZUL} - Precio: {MORADO}${prod.precio}{AZUL} - Stock: {MORADO}{prod.stock}{RESET}")
                                    
                                    id_prod = input_int_id(f"{AMARILLO}Ingrese el ID del producto (0 para terminar): {RESET}", "ID Producto")
                                    if id_prod == 0:
                                        break
                                    
                                    prod_encontrado = None
                                    for prod in self.producto_servicio.productos:
                                        if prod.id == id_prod and not prod.eliminado:
                                            prod_encontrado = prod
                                            break
                                    
                                    if not prod_encontrado:
                                        print(f"{AZUL}Producto no encontrado.{RESET}")
                                        continue
                                    
                                    cant = input_int(f"{AMARILLO}Ingrese la cantidad para '{prod_encontrado.nombre}': {RESET}", "Cantidad")
                                    items.append((cant, prod_encontrado))
                                
                                if items:
                                    nuevo_ped = self.pedido_servicio.crear_pedido(usu, forma_pago, items)
                                    print(f"{AZUL}¡Pedido creado con éxito! ID: {MORADO}{nuevo_ped.id}{AZUL} | Total: {MORADO}${nuevo_ped.total:.2f}{RESET}")
                                else:
                                    print(f"{AZUL}No se agregaron items, pedido cancelado.")
                            case "3":
                                id_ped = input_int_id(f"{AMARILLO}Ingrese el ID del pedido a actualizar: {RESET}", "ID Pedido")
                                print(f"\n{AZUL}Nuevos estados:{RESET}")
                                print(f"{VERDE}1. {AZUL}PENDIENTE\n{VERDE}2. {AZUL}CONFIRMADO\n{VERDE}3. {AZUL}TERMINADO\n{ROJO}4. {AZUL}CANCELADO{RESET}")
                                op_est = input_int(f"{AMARILLO}Seleccione nuevo estado (1-4): {RESET}", "Opción")
                                nuevo_estado = (Estado.PENDIENTE if op_est == 1 else 
                                                Estado.CONFIRMADO if op_est == 2 else 
                                                Estado.TERMINADO if op_est == 3 else Estado.CANCELADO)
                                self.pedido_servicio.cambiar_estado(id_ped, nuevo_estado)
                                print(f"{AZUL}¡Estado del pedido actualizado con éxito!{RESET}")
                            case "4":
                                id_ped = input_int(f"{AMARILLO}Ingrese el ID del pedido a eliminar: {RESET}", "ID Pedido")
                                if input(f"{AMARILLO}¿Confirma la baja lógica del pedido? (S/N): {RESET}").strip().lower() == "s":
                                    self.pedido_servicio.eliminar_pedido(id_ped)
                                    print(f"{AZUL}Pedido eliminado correctamente.{RESET}")
                            case "0":
                                break
                    except FoodStoreError as e:
                        print(f"\n{NARANJA}[Error de Negocio]: {e}{RESET}")
                    except ValueError as e:
                        print(f"\n{NARANJA}[Error de Formato]: {e}{RESET}")

            case "9":
                return False

            case _:
                print(f"{NARANJA}Opción no válida.{RESET}")
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
        print(f"\n{AZUL}=== FOOD STORE CLIENTE ({MORADO}{self.usuario.nombre} {self.usuario.apellido}{AZUL}) ==={RESET}")
        print(f"{VERDE}1.{AZUL} Ver categorías{RESET}")
        print(f"{VERDE}2.{AZUL} Ver productos disponibles{RESET}")
        print(f"{VERDE}3.{AZUL} Mis pedidos{RESET}")
        print(f"{VERDE}4.{AZUL} Mis datos{RESET}")
        print(f"{VERDE}9.{AZUL} Cerrar sesión{RESET}")
        print(f"{ROJO}0.{AZUL} Salir{RESET}")
        
        opcion = input(f"{AMARILLO}Seleccione una opción: {RESET}").strip()
        
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
                        print(f"\n{AZUL}--- MIS PEDIDOS ({MORADO}{self.usuario.nombre}{AZUL}) ---{RESET}")
                        mis_pedidos = self.pedido_servicio.listar_pedidos_por_usuario(self.usuario)
                        if not mis_pedidos:
                            print(f"{NARANJA}No tenés pedidos registrados.{RESET}")
                            break
                        for p in mis_pedidos:
                            print(f"{AZUL}ID: {MORADO}{p.id}{AZUL} | Fecha: {MORADO}{p.fecha}{AZUL} | Estado: {MORADO}{p.estado.name}{AZUL} | Pago: {MORADO}{p.forma_pago.name}{AZUL} | Total: {MORADO}${p.total:.2f}{RESET}")
                        
                        id_elegido = input_int(f"{AMARILLO}Ingrese el ID de un pedido para ver sus detalles (0 para volver): {RESET}", "ID")
                        if id_elegido == 0:
                            break
                        
                        encontrado = False
                        for p in mis_pedidos:
                            if p.id == id_elegido:
                                encontrado = True
                                print(f"\n{AZUL}Detalles del Pedido #{MORADO}{p.id}:{RESET}")
                                for d in p.detalles:
                                    prod_nombre = d.producto.nombre if d.producto else "Producto eliminado"
                                    prod_precio = d.producto.precio if d.producto else 0.0
                                    print(f"{AZUL} - {MORADO}{prod_nombre}{AZUL}: {MORADO}{d.cantidad}{AZUL} un. x {MORADO}${prod_precio}{AZUL} = {MORADO}${d.subtotal:.2f}{RESET}")
                                print(f"{AZUL}TOTAL: {MORADO}${p.total:.2f}{RESET}")
                        if not encontrado:
                            print(f"{NARANJA}El ID ingresado no corresponde a ninguno de tus pedidos.{RESET}")

                case "4":
                    print(f"\n{AZUL}--- MIS DATOS ---{RESET}")
                    print(f"{AZUL}Nombre: {MORADO}{self.usuario.nombre} {self.usuario.apellido}{RESET}")
                    print(f"{AZUL}Mail: {MORADO}{self.usuario.mail}{RESET}")
                    print(f"{AZUL}Celular: {MORADO}{self.usuario.celular}{RESET}")
                    print(f"{AZUL}Rol: {MORADO}{self.usuario.rol.name}{RESET}")

                case "9":
                    print(f"{ROJO}Cerrando sesión de cliente...{RESET}")
                    return False

                case _:
                    print(f"{NARANJA}Opción no válida.{RESET}")
        except FoodStoreError as e:
            print(f"\n{NARANJA}[Error de Negocio]: {e}{RESET}")
        except ValueError as e:
            print(f"\n{NARANJA}[Error de Formato]: {e}{RESET}")

        return True


def crear_menu(usuario: Usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio) -> Menu:
    """Instancia el menú correcto según el rol de forma polimórfica."""
    if usuario.rol == Rol.ADMIN:
        return MenuAdministrador(usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio)
    return MenuCliente(usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio)