from entidades.pedido import Pedido
from entidades.detalle_pedido import DetallePedido
from entidades.producto import Producto
from entidades.categoria import Categoria
from datetime import datetime
from excepciones.excepciones import EntidadNoEncontradaError, DatoInvalidoError

class Productoservicio:
    def __init__(self):
        self._productos = []
    
    @property
    def productos(self):
        return self._productos
    
    def __len__(self) -> int:
        return len(self._productos)

    def __iter__(self):
        return iter(self._productos)

    def __contains__(self, producto: "Producto") -> bool:
        return producto in self._productos

    def agregar_producto(self, producto):
        if self._productos:
            for i in self._productos:
                if i.id == producto.id:
                    return("Este producto ya esta en la lista.")
        self.productos.append(producto) 
        return("Se agrego el producto en la lista.")

def input_seleccion(mensaje):
    while True:
        input_salid = input(mensaje)
        if isinstance(input_salid, str):
            if not input_salid.strip():
                raise DatoInvalidoError("La seleccion no puede estar vacía.")
            return input_salid.lower()
        elif (isinstance(input_salid, int) or isinstance(input_salid, float)):
            if not 0 > input_salid:
                raise DatoInvalidoError("La seleccion no puede ser menor a cero")
            return input_salid
        else:
            raise DatoInvalidoError("Escriba una opcion mostrada en pantalla")

def input_str(mensaje, que_es):
    while True:
        input_salid = input(mensaje)
        if not isinstance(input_salid, str):
            raise DatoInvalidoError(f"{que_es} debe de ser una cadena de texto")
        if not input_salid.strip():
            raise DatoInvalidoError(f"{que_es} no puede estar vacio")
        return input_salid.capitalize()

def input_int(mensaje, que_es):
    while True:
        try:
            input_salid = int(input(mensaje))
        except:
            raise DatoInvalidoError(f"{que_es} debe de ser un valor numerico.")
        if not (isinstance(input_salid, int) or isinstance(input_salid, float)):
            raise DatoInvalidoError(f"{que_es} debe de ser un valor numerico.")
        if 0 > input_salid:
            raise DatoInvalidoError(f"{que_es} no puede ser menor a cero. ")
        return input_salid

def input_float(mensaje, que_es):
    while True:
        try:
            input_salid = float(input(mensaje))
        except:
            raise DatoInvalidoError(f"{que_es} debe de ser un valor numerico.")
        if not (isinstance(input_salid, int) or isinstance(input_salid, float)):
            raise DatoInvalidoError(f"{que_es} debe de ser un valor numerico.")
        if 0 > input_salid:
            raise DatoInvalidoError(f"{que_es} no puede ser menor a cero. ")
        return input_salid

def input_bool(mensaje):
    while True:
        print(mensaje)
        input_salid = input("(S/N): ").lower()
        match input_salid:
            case "n":
                return False
            case "s":
                return True

def listar_producto_admin(productoservicio):
    encontrado = False
    while True:
        opcion = input_str("¿Quiere filtar el listado por categoria?(S/N): ","Opcion").lower()
        match opcion:
            case "s":
                catego = input_int("Ingrese el ID de la categoria que desea filtar: ","ID de la categoria")
                for i in productoservicio.productos:
                    if i.categoria:
                        if i and i.categoria.id == catego:
                            encontrado = True
                            print(f"ID: {i.id} | {i.nombre}: {i.precio}$ | Stock: {i.stock} | Categoria: {i.categoria.nombre}")
                if not encontrado:
                    raise EntidadNoEncontradaError("No hay categorias cargadas o no se encontro una categoria con ese ID.")
                if encontrado:
                    break 
            case "n":
                for i in productoservicio.productos:
                    if i:
                        encontrado = True
                        if i.categoria:
                            print(f"ID: {i.id} | {i.nombre}: {i.precio}$ | Stock: {i.stock} | Categoria: {i.categoria.nombre}")
                        else:
                            print(f"ID: {i.id} | {i.nombre}: {i.precio}$ | Stock: {i.stock} | Sin categoria.")
                if not encontrado:
                    raise EntidadNoEncontradaError("No hay categorias cargadas.")
                if encontrado:
                    break
            case _:
                print("Escriba N o S")

def listar_producto_cliente(productoservicio):
    encontrado = False
    while True:
        opcion = input_str("¿Quiere filtar el listado por categoria?(S/N): ","Opcion").lower()
        match opcion:
            case "s":
                catego = input_int("Ingrese el ID de la categoria que desea filtar: ","ID de la categoria")
                for i in productoservicio.productos:
                    if i.categoria:
                        if i.categoria.id == catego and i.disponible and i.stock > 0:
                            encontrado = True
                            print(f"ID: {i.id} | {i.nombre}: {i.precio}$ | Stock: {i.stock} | Categoria: {i.categoria.nombre}")
                if not encontrado:
                    raise EntidadNoEncontradaError("No hay categorias cargadas o no se encontro una categoria con ese ID.")
                if encontrado:
                    break 
            case "n":
                for i in productoservicio.productos:
                    if i.disponible and i.stock > 0:
                        encontrado = True
                        if i.categoria:
                            print(f"ID: {i.id} | {i.nombre}: {i.precio}$ | Stock: {i.stock} | Categoria: {i.categoria.nombre}")
                        else:
                            print(f"ID: {i.id} | {i.nombre}: {i.precio}$ | Stock: {i.stock} | Sin categoria.")
                if not encontrado:
                    raise EntidadNoEncontradaError("No hay categorias cargadas.")
                if encontrado:
                    break
            case _:
                print("Escriba N o S")

def crear_producto(nombre: str, precio: float, descripcion: str, stock: int, imagen: str, disponible: bool, productoservicio):
    producto = Producto(nombre, precio, descripcion, stock, imagen, disponible)
    if productoservicio.productos:
        for i in productoservicio.productos:
            if i.id == producto.id:
                return ("Este producto ya esta en la lista.")
    productoservicio.agregar_producto(producto)
    return (f"Se creo el producto en la lista. ID generado: {producto.id}")

def editar_producto(_id, productoservicio, pedido_servicio=None):
    encontrado = False
    for i in productoservicio.productos:
        if _id == i.id:
            encontrado = True
            print("Se encontro un producto con ese ID")
            nombre_nuevo = input_str("Escriba el nuevo nombre del producto: ", "Nombre")
            precio_nuevo = input_float("Escriba el nuevo precio del producto: ", "Precio")
            descripcion_nueva = input_str("Escriba la nueva descripción del producto: ", "Descripción")
            stock_nuevo = input_int("Escriba el nuevo stock del producto: ", "Stock")
            imagen_nueva = input_str("Escriba el nuevo url de la imagen del producto: ", "URL de la imagen")
            disponible_nuevo = input_bool("¿El producto sigue estando disponible?: ")
            
            i.nombre = nombre_nuevo.capitalize()
            i.precio = precio_nuevo
            i.descripcion = descripcion_nueva.capitalize()
            i.stock = stock_nuevo
            i.imagen = imagen_nueva
            i.disponible = disponible_nuevo
            
            if pedido_servicio is not None:
                for pedido in pedido_servicio.pedidos:
                    for f in pedido.detalles:
                        if f.producto and f.producto.id == i.id:
                            f._DetallePedido__producto = i 
    if encontrado:
        print("¡Producto editado con éxito!")
    else:
        raise EntidadNoEncontradaError("No se encontro ningun producto con ese ID")

def eliminar_producto(_id, productoservicio, pedido_servicio=None):
    encontrado = False
    for i in productoservicio.productos:
        if _id == i.id:
            encontrado = True
            print("Se encontro el producto con ese ID")
            while True:
                opcion = input("¿Usted esta seguro de eliminar este producto?(S/N): ")
                match opcion:
                    case "S" | "s":
                        id_viejo = i.id
                        productoservicio.productos.remove(i)
                        if pedido_servicio is not None:
                            for f in pedido_servicio.pedidos:
                                for det in f.detalles:
                                    if det.producto and det.producto.id == id_viejo:
                                        det.producto = None
                        print("Eliminacion completada.")
                        break
                    case "N" | "n":
                        print("Se cancelo la eliminacion, regresando...")
                        break
                    case _:
                        print("Escriba S o N.")
    if not encontrado:
        raise EntidadNoEncontradaError("No se encontro ningun producto con ese ID")

def asignar_categoria(_id, productoservicio, pedido_servicio, categoriaservicio):
    encontrado = False
    for i in productoservicio.productos:
        if _id == i.id:
            encontrado = True
            print("Se encontro el producto con ese ID")
            _id_catego = input_int("Ingrese el ID de la categoria para asignar: ", "ID de la categoria")
            for f in categoriaservicio.categorias:
                if _id_catego == f.id:
                    print("Se encontro la categoria con ese ID")
                    i.agregar_categoria(f)
                    print("Categoria asignada correctamente.")
                    if pedido_servicio is not None:
                        for pedido in pedido_servicio.pedidos:
                            for n in pedido.detalles:
                                if n.producto and n.producto.id == i.id:
                                    n.producto.agregar_categoria = f            
    if not encontrado:
        raise EntidadNoEncontradaError("No se encontro ningun producto con ese ID")