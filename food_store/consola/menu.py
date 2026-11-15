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
        print(f"{AZUL}\n=== FOOD STORE ADMINISTRADOR ({MORADO}{self.usuario.nombre} {MORADO}{self.usuario.apellido}{AZUL}) ==={BLANCO}")
        print(f"{VERDE}1.{AZUL} Categorías{BLANCO}")
        print(f"{VERDE}2.{AZUL} Productos{BLANCO}")
        print(f"{VERDE}3.{AZUL} Usuarios{BLANCO}")
        print(f"{VERDE}4.{AZUL} Pedidos{BLANCO}")
        print(f"{VERDE}9.{AZUL} Cerrar sesión{BLANCO}")
        print(f"{ROJO}0.{AZUL} Salir{BLANCO}")
        
        opcion = input(f"{AMARILLO}Seleccione una opción: {BLANCO}").strip()
        
        match opcion:
            case "0":
                return "salir"
            case "1":
                limpiado_consola()
                while True:
                    print(f"""{AZUL}--- CATEGORÍAS ---{BLANCO}
{VERDE}1.{AZUL} Listar{BLANCO}
{VERDE}2.{AZUL} Crear{BLANCO}
{VERDE}3.{AZUL} Editar{BLANCO}
{VERDE}4.{AZUL} Eliminar{BLANCO}
{ROJO}0.{AZUL} Volver{BLANCO}""")
                    try:
                        seleccion = input_seleccion(f"{AMARILLO}Seleccione: {BLANCO}")
                        match seleccion:
                            case 1 | "1" | "uno" | "i" | "listar":
                                self.categoria_servicio.listar_categoria()
                                continuar()
                                limpiado_consola()
                            case 2 | "2" | "dos" | "ii" | "crear":
                                nombre = input_str(f"{AMARILLO}Escriba el nombre de la categoria: {BLANCO}", "Nombre")
                                descripcion = input_str(f"{AMARILLO}Escriba la descripción de la categoria: {BLANCO}", "Descripción")
                                res = self.categoria_servicio.crear_categoria(nombre, descripcion)
                                print(res)
                                continuar()
                                limpiado_consola()
                            case 3 | "3" | "tres" | "iii" | "editar":
                                _id = input_int_id(f"{AMARILLO}Escriba el ID de la categoria que desea buscar: {BLANCO}","ID")
                                self.categoria_servicio.editar_categoria(_id, self.pedido_servicio)
                                continuar()
                                limpiado_consola()
                            case 4 | "4" | "cuatro" | "iv" | "eliminar":
                                _id = input_int_id(f"{AMARILLO}Escriba el ID de la categoria que desea buscar: {BLANCO}","ID")
                                self.categoria_servicio.eliminar_categoria(_id, self.pedido_servicio)
                                continuar()
                                limpiado_consola()
                            case 0 | "0" | "cero" | "o" | "zero" | "volver":
                                limpiado_consola()
                                print(f"{ROJO}Regresando...{BLANCO}")
                                break
                    except FoodStoreError as e:
                        limpiado_consola()
                        print(f"{NARANJA}\n[Error de Negocio]: {e}{BLANCO}")
                    except ValueError as e:
                        limpiado_consola()
                        print(f"{NARANJA}\n[Error de Formato]: {e}{BLANCO}")

            case "2" | "dos":
                limpiado_consola()
                while True:
                    print(f"""{AZUL}--- PRODUCTOS ---{BLANCO}
{VERDE}1.{AZUL} Listar{BLANCO}
{VERDE}2.{AZUL} Crear{BLANCO}
{VERDE}3.{AZUL} Editar{BLANCO}
{VERDE}4.{AZUL} Eliminar{BLANCO}
{VERDE}5.{AZUL} Asignar una categoria a un producto{BLANCO}
{ROJO}0.{AZUL} Volver{BLANCO}""")
                    try:
                        seleccion = input_seleccion(f"{AMARILLO}Seleccione: {BLANCO}")
                        match seleccion:
                            case 1 | "1" | "uno" | "i" | "listar":
                                listar_producto_admin(self.producto_servicio)
                                continuar()
                                limpiado_consola()
                            case 2 | "2" | "dos" | "ii" | "crear":
                                nombre = input_str(f"{AMARILLO}Escriba el nombre del nuevo producto: {BLANCO}", "Nombre")
                                precio = input_float(f"{AMARILLO}Escriba el precio del nuevo producto: {BLANCO}", "Precio")
                                descripcion = input_str(f"{AMARILLO}Escriba la descripcion del nuevo producto: {BLANCO}", "Descripcion")
                                stock = input_int(f"{AMARILLO}Escriba el stock inicial del nuevo producto: {BLANCO}", "Stock")
                                imagen = input_str(f"{AMARILLO}Ingrese el url de la imagen del producto: {BLANCO}", "Imagen")
                                disponible = input_bool(f"{AMARILLO}¿El producto esta disponible?: {BLANCO}")
                                res = crear_producto(nombre, precio, descripcion, stock, imagen, disponible, self.producto_servicio)
                                print(res)
                                continuar()
                                limpiado_consola()
                            case 3 | "3" | "tres" | "iii" | "editar":
                                _id = input_int(f"{AMARILLO}Escriba el ID del producto que desea buscar: {BLANCO}","ID")
                                editar_producto(_id, self.producto_servicio, self.pedido_servicio)
                                continuar()
                                limpiado_consola()
                            case 4 | "4" | "cuatro" | "iv" | "eliminar":
                                _id = input_int(f"{AMARILLO}Escriba el ID del producto que desea buscar: {BLANCO}","ID")
                                eliminar_producto(_id, self.producto_servicio, self.pedido_servicio)
                                continuar()
                                limpiado_consola()
                            case 5 | "5" | "cinco" | "v" | "asignar":
                                _id = input_int(f"{AMARILLO}Escriba el ID del producto que desea buscar: {BLANCO}", "ID del producto")
                                asignar_categoria(_id, self.producto_servicio, self.pedido_servicio, self.categoria_servicio)
                                continuar()
                                limpiado_consola()
                            case 0 | "0" | "cero" | "o" | "zero" | "volver":
                                limpiado_consola()
                                print(f"{ROJO}Regresando...{BLANCO}")
                                break
                            case _:
                                print(f"{NARANJA}Ingrese una opcion mostrada en pantalla.{BLANCO}")
                    except FoodStoreError as e:
                        limpiado_consola()
                        print(f"{NARANJA}\n[Error de Negocio]: {e}{BLANCO}")
                    except ValueError as e:
                        limpiado_consola()
                        print(f"{NARANJA}\n[Error de Formato]: {e}{BLANCO}")
            case "3" | "tres":
                limpiado_consola()
                while True:
                    print(f"""{AZUL}--- USUARIOS ---{BLANCO}
{VERDE}1.{AZUL} Listar{BLANCO}
{VERDE}2.{AZUL} Crear{BLANCO}
{VERDE}3.{AZUL} Editar{BLANCO}
{VERDE}4.{AZUL} Eliminar{BLANCO}
{VERDE}5.{AZUL} Mis datos{BLANCO}
{ROJO}0.{AZUL} Volver{BLANCO}""")
                    try:
                        seleccion = input(f"{AMARILLO}Seleccione: {BLANCO}").strip()
                        limpiado_consola()
                        match seleccion:
                            case "1" | "uno" | "i" | "listar":
                                usuarios = self.usuario_servicio.usuarios_activos()
                                if not usuarios:
                                    print(f"{NARANJA}No hay usuarios cargados.{BLANCO}")
                                    continuar()
                                    limpiado_consola()
                                else:
                                    for usuario in usuarios:
                                        print(f"""{AZUL}Id: {MORADO}{usuario.id}{BLANCO}
{AZUL}Nombre: {MORADO}{usuario.nombre}{BLANCO}
{AZUL}Apellido: {MORADO}{usuario.apellido}{BLANCO}
{AZUL}Mail: {MORADO}{usuario.mail}{BLANCO}
{AZUL}Rol: {MORADO}{usuario.rol.name}{BLANCO}
-------------------------""")
                                    continuar()
                                    limpiado_consola()
                            case "2" | "dos" | "ii" | "crear":
                                nombre = input_str(f"{AMARILLO}Ingrese el nombre: {BLANCO}", "Nombre").strip()
                                apellido = input_str(f"{AMARILLO}Ingrese el apellido: {BLANCO}", "Apellido").strip()
                                mail = input_str(f"{AMARILLO}Ingrese el mail: {BLANCO}", "Mail").strip()
                                celular = input(f"{AMARILLO}Ingrese el celular: {BLANCO}").strip()
                                contrasenia = input(f"{AMARILLO}Ingrese la contraseña: {BLANCO}").strip()
                                rol = input_int(f"{AMARILLO}Ingrese rol (1 = Admin | 2 = Usuario): {BLANCO}", "Rol")
                                self.usuario_servicio.crear_usuario(nombre, apellido, mail, celular, contrasenia, rol)
                                print(f"{AZUL}Usuario creado exitosamente.{BLANCO}")
                                continuar()
                                limpiado_consola()
                            case "3" | "tres" | "iii" | "editar":
                                _id = input_int(f"{AMARILLO}Escriba el ID del usuario que desea buscar: {BLANCO}", "ID")
                                usuario_a_editar = self.usuario_servicio.buscar_por_id(_id)
                                editando = True
                                while editando:
                                    print(f"""{CYAN}- Usted accedió al Usuario de ID {_id}{BLANCO}
{AZUL}- {MORADO}{usuario_a_editar.nombre} {usuario_a_editar.apellido}{BLANCO}
{AZUL}¿Qué valor le gustaría actualizar?{BLANCO}

{VERDE}1.{AZUL} Nombre{BLANCO}
{VERDE}2.{AZUL} Apellido{BLANCO}
{VERDE}3.{AZUL} Mail{BLANCO}
{VERDE}4.{AZUL} Celular{BLANCO}
{VERDE}5.{AZUL} Contraseña{BLANCO}
{VERDE}6.{AZUL} Rol{BLANCO}
{ROJO}8.{AZUL} Salir / Volver{BLANCO}

{AMARILLO}Seleccione una opción: {BLANCO}""", end="")
                                    opcion_editar = input().strip()
                                    if opcion_editar == "8":
                                        editando = False
                                        continuar()
                                        limpiado_consola()
                                        break
                                    match opcion_editar:
                                        case "1" | "uno" | "i" | "nombre":
                                            nuevo_nombre = input_str(f"{AMARILLO}Ingrese el nuevo nombre: {BLANCO}", "Nombre")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{BLANCO} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_nombre(usuario_a_editar, nuevo_nombre)
                                                print(f"{AZUL}Nombre de usuario cambiado.{BLANCO}")
                                            else:
                                                print(f"{AZUL}Acción cancelada.{BLANCO}")
                                            continuar()
                                            limpiado_consola()
                                        case "2" | "dos" | "ii" | "apellido":
                                            nuevo_apellido = input_str(f"{AMARILLO}Ingrese el nuevo apellido: {BLANCO}", "Apellido")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO): {BLANCO}").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_apellido(usuario_a_editar, nuevo_apellido)
                                                print(f"{AZUL}Apellido de usuario cambiado.{BLANCO}")
                                            else:
                                                print(f"{AZUL}Acción cancelada.{BLANCO}")
                                            continuar()
                                            limpiado_consola()
                                        case "3" | "tres" | "iii" | "mail":
                                            nuevo_mail = input_str(f"{AMARILLO}Ingrese el nuevo mail: {BLANCO}", "Mail")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{BLANCO} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                try: 
                                                    self.usuario_servicio.cambio_mail(usuario_a_editar, nuevo_mail)
                                                    print(f"{AZUL}Mail de usuario cambiado.{BLANCO}")
                                                except TypeError as e:
                                                    print(e)
                                            else:
                                                print(f"{AZUL}Acción cancelada.{BLANCO}")
                                            continuar()
                                            limpiado_consola()
                                        case "4" | "cuatro" | "iv" | "celular":
                                            nuevo_celular = input_str(f"{AMARILLO}Ingrese el nuevo celular: {BLANCO}", "Celular")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{BLANCO} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_celular(usuario_a_editar, nuevo_celular)
                                                print(f"{AZUL}Celular de usuario cambiado.{BLANCO}")
                                            else:
                                                print(f"{AZUL}Acción cancelada.{BLANCO}")
                                            continuar()
                                            limpiado_consola()
                                        case "5" | "cinco" | "v" | "contraseña":
                                            nueva_contrasenia = input_str(f"{AMARILLO}Ingrese la nueva contraseña: {BLANCO}", "Contraseña")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{BLANCO} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_contrasenia(usuario_a_editar, nueva_contrasenia)
                                                print(f"{AZUL}Contraseña de usuario cambiada.{BLANCO}")
                                            else:
                                                print(f"{AZUL}Acción cancelada.{BLANCO}")
                                            continuar()
                                            limpiado_consola()
                                        case "6" | "seis" | "vi" | "rol":
                                            nuevo_rol = input_int(f"{AMARILLO}Ingrese el nuevo rol (1 = Admin | 2 = Usuario): {BLANCO}", "Rol")
                                            confirmacion = input(f"{AMARILLO}¿Estás seguro de hacer este cambio? (SI/NO):{BLANCO} ").strip()
                                            if confirmacion.lower() in ["si", "s"]:
                                                self.usuario_servicio.cambio_rol(usuario_a_editar, nuevo_rol)
                                                print(f"{AZUL}Rol de usuario cambiado.{BLANCO}")
                                            else:
                                                print(f"{AZUL}Acción cancelada.{BLANCO}")
                                            continuar()
                                            limpiado_consola()
                                        case _:
                                            print(f"{NARANJA}Error... Comando incorrecto{BLANCO}")
                                            continuar()
                                            limpiado_consola()
                                        
                            case "4" | "cuatro" | "iv" | "eliminar":
                                _id = input_int(f"{AMARILLO}Escriba el ID del usuario: {BLANCO}", "ID")
                                usuario_a_borrar = self.usuario_servicio.buscar_por_id(_id)
                                if usuario_a_borrar.id == self.usuario.id:
                                    raise OperacionNoPermitidaError(f"{NARANJA}No puedes borrarte a tí mismo.{BLANCO}")
                                confirmacion = input(f"{ROJO}¿Dar baja lógica a {usuario_a_borrar.nombre}? (S/N):{BLANCO} ").strip().lower()
                                if confirmacion in ["si", "s"]:
                                    self.usuario_servicio.eliminar_usuario(_id)
                                    print(f"{AZUL}Usuario {_id} eliminado.{BLANCO}")
                                else:
                                    print(f"{AZUL}Usuario {_id} no ha sido eliminado.{BLANCO}")
                                continuar()
                                limpiado_consola()
                            case "5" | "cinco" | "v" | "datos":
                                print(f"""{AZUL}Id: {MORADO}{self.usuario.id}{BLANCO}
{AZUL}Nombre: {MORADO}{self.usuario.nombre}{BLANCO}
{AZUL}Apellido: {MORADO}{self.usuario.apellido}{BLANCO}
{AZUL}Mail: {MORADO}{self.usuario.mail}{BLANCO}
{AZUL}Rol: {MORADO}{self.usuario.rol.name}{BLANCO}
{AZUL}-------------------------{BLANCO}""")
                                continuar()
                                limpiado_consola()
                            case 0 | "0" | "cero" | "o" | "zero" | "volver":
                                print(f"{ROJO}Volviendo...{BLANCO}")
                                break
                    except FoodStoreError as e:
                        print(f"\n{NARANJA}[Error de Negocio]: {e}{BLANCO}")
                        continuar()
                        limpiado_consola()
                    except ValueError as e:
                        print(f"\n{NARANJA}[Error de Formato]: {e}{BLANCO}")
                        continuar()
                        limpiado_consola()
            case "4" | "cuatro":
                limpiado_consola()
                while True:
                    print(f"""{AZUL}--- GESTIÓN DE PEDIDOS ---{BLANCO}
{VERDE}1.{AZUL} Listar todos los pedidos{BLANCO}
{VERDE}2.{AZUL} Crear nuevo pedido{BLANCO}
{VERDE}3.{AZUL} Cambiar estado de pedido{BLANCO}
{VERDE}4.{AZUL} Eliminar pedido (Baja lógica){BLANCO}
{ROJO}0.{AZUL} Volver{BLANCO}""")
                    try:
                        seleccion = input(f"{AMARILLO}Seleccione: {BLANCO}").strip()
                        match seleccion:
                            case "1":
                                pedidos = self.pedido_servicio.listar_pedidos_activos()
                                if not pedidos:
                                    limpiado_consola()
                                    print(f"{NARANJA}No hay pedidos registrados.{BLANCO}")
                                else:
                                    for p in pedidos:
                                        print(p)
                                        print(f"{AZUL}  Detalles:{BLANCO}")
                                        for d in p.detalles:
                                            print(f"{AZUL}   - {d.producto.nombre if d.producto else 'Producto Eliminado'} x {d.cantidad} (Subtotal: ${d.subtotal:.2f}){BLANCO}")
                                        print(f"{AZUL}-{BLANCO}" * 40)
                                        continuar()
                                        limpiado_consola()
                            case "2":
                                print(f"\n{AZUL}--- CREAR PEDIDO ---{BLANCO}")
                                id_usu = input_int_id(f"{AMARILLO}Ingrese el ID del usuario cliente: {BLANCO}", "ID Usuario")
                                usu = self.usuario_servicio.buscar_por_id(id_usu)
                                
                                print(f"\n{AZUL}Formas de pago disponibles:{BLANCO}")
                                print(f"{VERDE}1. {AZUL}TARJETA\n{VERDE}2. {AZUL}TRANSFERENCIA\n{VERDE}3. {AZUL}EFECTIVO{BLANCO}")
                                op_pago = input_int(f"{AMARILLO}Seleccione forma de pago (1-3): {BLANCO}", "Opción")
                                forma_pago = FormaPago.TARJETA if op_pago == 1 else (FormaPago.TRANSFERENCIA if op_pago == 2 else FormaPago.EFECTIVO)
                                
                                items = []
                                while True:
                                    print(f"\n{AZUL}Productos disponibles:{BLANCO}")
                                    for prod in self.producto_servicio.productos:
                                        if not prod.eliminado and prod.disponible:
                                            print(f"{AZUL}ID: {MORADO}{prod.id}{AZUL} | {MORADO}{prod.nombre}{AZUL} - Precio: {MORADO}${prod.precio}{AZUL} - Stock: {MORADO}{prod.stock}{BLANCO}")
                                    
                                    id_prod = input_int_id(f"{AMARILLO}Ingrese el ID del producto (0 para terminar): {BLANCO}", "ID Producto")
                                    if id_prod == 0:
                                        break
                                    
                                    prod_encontrado = None
                                    for prod in self.producto_servicio.productos:
                                        if prod.id == id_prod and not prod.eliminado:
                                            prod_encontrado = prod
                                            break
                                    
                                    if not prod_encontrado:
                                        limpiado_consola()
                                        print(f"{NARANJA}Producto no encontrado.{BLANCO}")
                                        continue
                                    
                                    cant = input_int(f"{AMARILLO}Ingrese la cantidad para '{prod_encontrado.nombre}': {BLANCO}", "Cantidad")
                                    items.append((cant, prod_encontrado))
                                
                                if items:
                                    nuevo_ped = self.pedido_servicio.crear_pedido(usu, forma_pago, items)
                                    print(f"{AZUL}¡Pedido creado con éxito! ID: {MORADO}{nuevo_ped.id}{AZUL} | Total: {MORADO}${nuevo_ped.total:.2f}{BLANCO}")
                                    continuar()
                                    limpiado_consola()
                                else:
                                    limpiado_consola()
                                    print(f"{NARANJA}No se agregaron items, pedido cancelado.")
                            case "3":
                                id_ped = input_int_id(f"{AMARILLO}Ingrese el ID del pedido a actualizar: {BLANCO}", "ID Pedido")
                                print(f"\n{AZUL}Nuevos estados:{BLANCO}")
                                print(f"{VERDE}1. {AZUL}PENDIENTE\n{VERDE}2. {AZUL}CONFIRMADO\n{VERDE}3. {AZUL}TERMINADO\n{ROJO}4. {AZUL}CANCELADO{BLANCO}")
                                op_est = input_int(f"{AMARILLO}Seleccione nuevo estado (1-4): {BLANCO}", "Opción")
                                nuevo_estado = (Estado.PENDIENTE if op_est == 1 else 
                                                Estado.CONFIRMADO if op_est == 2 else 
                                                Estado.TERMINADO if op_est == 3 else Estado.CANCELADO)
                                self.pedido_servicio.cambiar_estado(id_ped, nuevo_estado)
                                print(f"{AZUL}¡Estado del pedido actualizado con éxito!{BLANCO}")
                                continuar()
                                limpiado_consola()
                            case "4":
                                id_ped = input_int(f"{AMARILLO}Ingrese el ID del pedido a eliminar: {BLANCO}", "ID Pedido")
                                if input(f"{AMARILLO}¿Confirma la baja lógica del pedido? (S/N): {BLANCO}").strip().lower() == "s":
                                    self.pedido_servicio.eliminar_pedido(id_ped)
                                    print(f"{AZUL}Pedido eliminado correctamente.{BLANCO}")
                                    continuar()
                                    limpiado_consola()
                            case "0":
                                limpiado_consola()
                                print(f"{ROJO}Regresando...{BLANCO}")
                                break
                    except FoodStoreError as e:
                        limpiado_consola()
                        print(f"\n{NARANJA}[Error de Negocio]: {e}{BLANCO}")
                    except ValueError as e:
                        limpiado_consola()
                        print(f"\n{NARANJA}[Error de Formato]: {e}{BLANCO}")

            case "9":
                return False

            case _:
                limpiado_consola()
                print(f"{NARANJA}Opción no válida.{BLANCO}")
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
        print(f"\n{AZUL}=== FOOD STORE CLIENTE ({MORADO}{self.usuario.nombre} {self.usuario.apellido}{AZUL}) ==={BLANCO}")
        print(f"{VERDE}1.{AZUL} Ver categorías{BLANCO}")
        print(f"{VERDE}2.{AZUL} Ver productos disponibles{BLANCO}")
        print(f"{VERDE}3.{AZUL} Mis pedidos{BLANCO}")
        print(f"{VERDE}4.{AZUL} Mis datos{BLANCO}")
        print(f"{VERDE}9.{AZUL} Cerrar sesión{BLANCO}")
        print(f"{ROJO}0.{AZUL} Salir{BLANCO}")
        
        opcion = input(f"{AMARILLO}Seleccione una opción: {BLANCO}").strip()
        
        try:
            match opcion:
                case "0":
                    return "salir"

                case "1" | "uno":
                    self.categoria_servicio.listar_categoria()
                    continuar()
                    limpiado_consola()
                case "2" | "dos":
                    listar_producto_cliente(self.producto_servicio)
                    continuar()
                    limpiado_consola()
                case "3":
                    while True:
                        print(f"\n{AZUL}--- MIS PEDIDOS ({MORADO}{self.usuario.nombre}{AZUL}) ---{BLANCO}")
                        mis_pedidos = self.pedido_servicio.listar_pedidos_por_usuario(self.usuario)
                        if not mis_pedidos:
                            print(f"{NARANJA}No tenés pedidos registrados.{BLANCO}")
                            break
                        for p in mis_pedidos:
                            print(f"{AZUL}ID: {MORADO}{p.id}{AZUL} | Fecha: {MORADO}{p.fecha}{AZUL} | Estado: {MORADO}{p.estado.name}{AZUL} | Pago: {MORADO}{p.forma_pago.name}{AZUL} | Total: {MORADO}${p.total:.2f}{BLANCO}")
                        
                        id_elegido = input_int(f"{AMARILLO}Ingrese el ID de un pedido para ver sus detalles (0 para volver): {BLANCO}", "ID")
                        if id_elegido == 0:
                            break
                        
                        encontrado = False
                        for p in mis_pedidos:
                            if p.id == id_elegido:
                                encontrado = True
                                print(f"\n{AZUL}Detalles del Pedido #{MORADO}{p.id}:{BLANCO}")
                                for d in p.detalles:
                                    prod_nombre = d.producto.nombre if d.producto else "Producto eliminado"
                                    prod_precio = d.producto.precio if d.producto else 0.0
                                    print(f"{AZUL} - {MORADO}{prod_nombre}{AZUL}: {MORADO}{d.cantidad}{AZUL} un. x {MORADO}${prod_precio}{AZUL} = {MORADO}${d.subtotal:.2f}{BLANCO}")
                                print(f"{AZUL}TOTAL: {MORADO}${p.total:.2f}{BLANCO}")
                                continuar()
                                limpiado_consola()
                        if not encontrado:
                            limpiado_consola()
                            print(f"{NARANJA}El ID ingresado no corresponde a ninguno de tus pedidos.{BLANCO}")

                case "4":                    
                    print(f"\n{AZUL}--- MIS DATOS ---{BLANCO}")
                    print(f"{AZUL}Nombre: {MORADO}{self.usuario.nombre} {self.usuario.apellido}{BLANCO}")
                    print(f"{AZUL}Mail: {MORADO}{self.usuario.mail}{BLANCO}")
                    print(f"{AZUL}Celular: {MORADO}{self.usuario.celular}{BLANCO}")
                    print(f"{AZUL}Rol: {MORADO}{self.usuario.rol.name}{BLANCO}")
                    continuar()
                    limpiado_consola()
                case "9":
                    limpiado_consola()
                    print(f"{ROJO}Cerrando sesión de cliente...{BLANCO}")
                    return False
                case _:
                    limpiado_consola()
                    print(f"{NARANJA}Opción no válida.{BLANCO}")
        except FoodStoreError as e:
            limpiado_consola()
            print(f"\n{NARANJA}[Error de Negocio]: {e}{BLANCO}")
        except ValueError as e:
            limpiado_consola()
            print(f"\n{NARANJA}[Error de Formato]: {e}{BLANCO}")

        return True


def crear_menu(usuario: Usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio) -> Menu:
    """Instancia el menú correcto según el rol de forma polimórfica."""
    if usuario.rol == Rol.ADMIN:
        return MenuAdministrador(usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio)
    return MenuCliente(usuario, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio)