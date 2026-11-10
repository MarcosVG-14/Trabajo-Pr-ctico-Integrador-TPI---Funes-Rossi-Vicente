from entidades.pedido import Pedido
from entidades.detalle_pedido import DetallePedido
from entidades.producto import Producto
from entidades.categoria import Categoria
from datetime import datetime
from excepciones.excepciones import EntidadNoEncontradaError, DatoInvalidoError

class Categoriaservicio:
    def __init__(self):
        self._categorias = []
    
    @property
    def categorias(self):
        return self._categorias
    
    def __len__(self) -> int:
        return len(self._categorias)

    def __iter__(self):
        return iter(self._categorias)

    def __contains__(self, categoria: "Categoria") -> bool:
        return categoria in self._categorias

    def agregar_categoria(self, categoria):
        if self._categorias:
            for i in self._productos:
                if i.id == producto.id:
                    return ("Esta categoria ya esta en la lista.")
        self.categorias.append(categoria)
        return ("Se agrego la categoria en la lista.")

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

def listar_categoria(categoriaservicio):
    encontrado = False
    for i in categoriaservicio.categorias:
        if i and not i.eliminado:
            encontrado = True
            print(f"ID: {i.id} | {i.nombre}: {i.descripcion}")
    if not encontrado:
        raise EntidadNoEncontradaError("No hay categorias cargadas.")

def crear_categoria(nombre, descripcion, categoriaservicio):
    categoria = Categoria(nombre, descripcion)
    if categoriaservicio.categorias:
        for i in categoriaservicio.categorias:
            if i.id == categoria.id:
                return ("Esta categoria ya esta en la lista.")
    categoriaservicio.agregar_categoria(categoria)
    return (f"Se creo la categoria en la lista. ID generado: {categoria.id}")

def editar_categoria(_id, categoriaservicio, pedido=None):
    encontrado = False
    for i in categoriaservicio.categorias:
        if _id == i.id and not i.eliminado:
            encontrado = True
            print("Se encontro la categoria con ese ID")
            nombre_nuevo = input_str("Escriba el nuevo nombre de la categoria: ", "Nombre")
            descripcion_nueva = input_str("Escriba la nueva descripción de la categoria: ", "Descripción")
            nombre_viejo = i.nombre
            i.nombre = nombre_nuevo.capitalize()
            i.descripcion = descripcion_nueva.capitalize()
            if pedido:
                for f in pedido.detalles:
                    if f.producto and f.producto.categoria:
                        if f.producto.categoria.nombre == nombre_viejo:
                            f.producto.categoria = i
    if encontrado:
        print("¡Categoria editada!")
    else:
        raise EntidadNoEncontradaError("No se encontro ninguna categoria con ese ID")

def eliminar_categoria(_id, categoriaservicio, pedido=None):
    encontrado = False
    for i in categoriaservicio.categorias:
        if _id == i.id and not i.eliminado:
            encontrado = True
            print("Se encontro la categoria con ese ID")
            while True:
                opcion = input("¿Usted esta seguro de eliminar esta categoria?(S/N): ").strip().lower()
                match opcion:
                    case "s":
                        id_viejo = i.id
                        i.eliminado = True
                        if pedido is not None:
                            for f in pedido.detalles:
                                if f.producto and f.producto.categoria:
                                    if f.producto.categoria.id == id_viejo:
                                        f.producto.categoria = None
                        print("Eliminacion completada.")
                        break
                    case "n":
                        print("Se cancelo la eliminacion, regresando...")
                        break
                    case _:
                        print("Escriba S o N.")
    if not encontrado:
        raise EntidadNoEncontradaError("No se encontro ninguna categoria con ese ID")

categoriaservicio1 = Categoriaservicio()