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

def listar_producto(productoservicio):
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
