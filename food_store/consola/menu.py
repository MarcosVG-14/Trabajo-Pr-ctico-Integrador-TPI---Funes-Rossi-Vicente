from abc import ABC, abstractmethod
from entidades.usuario import Usuario
from enums.enums import Rol, Estado, FormaPago
from servicios.categoriaservicio import input_seleccion, input_str, input_int
from servicios.productoservicio import listar_producto_admin, listar_producto_cliente, crear_producto, editar_producto, eliminar_producto, input_float, input_bool
from excepciones.excepciones import FoodStoreError, OperacionNoPermitidaError

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
                    try:
                        seleccion = input_seleccion("Seleccione: ")
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
                                print("Regresando...")
                                break
                    except FoodStoreError as e:
                        print(f"\n[Error de Negocio]: {e}")
                    except ValueError as e:
                        print(f"\n[Error de Formato]: {e}")

            case "2" | "dos":
                while True:
                    print("""--- PRODUCTOS ---
1. Listar
2. Crear
3. Editar
4. Eliminar
0. Volver""")
                    try:
                        seleccion = input_seleccion("Seleccione: ")
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
                            case 0 | "0" | "cero" | "o" | "zero" | "volver":
                                print("Regresando...")
                                break
                            case _:
                                print("Ingrese una opcion mostrada en pantalla.")
                    except FoodStoreError as e:
                        print(f"\n[Error de Negocio]: {e}")
                    except ValueError as e:
                        print(f"\n[Error de Formato]: {e}")

            case "3" | "tres":
                while True:
                    print("""--- USUARIOS ---
1. Listar
2. Crear
3. Editar
4. Eliminar
0. Volver""")
                    try:
                        seleccion = input("Seleccione: ").strip()
                        match seleccion:
                            case "1" | "uno" | "i" | "listar":
                                usuarios = self.usuario_servicio.usuarios_activos()
                                if not usuarios:
                                    print("No hay usuarios cargados.")
                                else:
                                    for usuario in usuarios:
                                        print(f"Id: {usuario.id} | {usuario.nombre} {usuario.apellido} | Mail: {usuario.mail} | Rol: {usuario.rol.name}")
                            case "2" | "dos" | "ii" | "crear":
                                nombre = input("Ingrese el nombre: ").strip()
                                apellido = input("Ingrese el apellido: ").strip()
                                mail = input("Ingrese el mail: ").strip()
                                celular = input("Ingrese el celular: ").strip()
                                contrasenia = input("Ingrese la contraseña: ").strip()
                                rol = input("Ingrese rol (1 = Admin | 2 = Usuario): ").strip()
                                self.usuario_servicio.crear_usuario(nombre, apellido, mail, celular, contrasenia, rol)
                                print("Usuario creado exitosamente.")
                            case "4" | "cuatro" | "iv" | "eliminar":
                                _id = input_int("Escriba el ID del usuario: ", "ID")
                                usuario_a_borrar = self.usuario_servicio.buscar_por_id(_id)
                                if usuario_a_borrar.id == self.usuario.id:
                                    raise OperacionNoPermitidaError("No puedes borrarte a tí mismo.")
                                if input(f"¿Dar baja lógica a {usuario_a_borrar.nombre}? (S/N): ").strip().lower() == "s":
                                    self.usuario_servicio.eliminar_usuario(_id)
                                    print(f"Usuario {_id} eliminado.")
                            case 0 | "0" | "cero" | "o" | "zero" | "volver":
                                break
                    except FoodStoreError as e:
                        print(f"\n[Error de Negocio]: {e}")
                    except ValueError as e:
                        print(f"\n[Error de Formato]: {e}")

            case "4" | "cuatro":
                while True:
                    print("""--- GESTIÓN DE PEDIDOS ---
1. Listar todos los pedidos
2. Crear nuevo pedido
3. Cambiar estado de pedido
4. Eliminar pedido (Baja lógica)
0. Volver""")
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
        print("1. Ver categorías")
        print("2. Ver productos disponibles")
        print("3. Mis pedidos")
        print("4. Mis datos")
        print("9. Cerrar sesión")
        print("0. Salir")
        
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