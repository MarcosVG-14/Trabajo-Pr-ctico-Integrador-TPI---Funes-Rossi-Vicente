from entidades.pedido import Pedido
from entidades.detalle_pedido import DetallePedido
from entidades.producto import Producto
from entidades.categoria import Categoria
from datetime import datetime
from excepciones.excepciones import EntidadNoEncontradaError, DatoInvalidoError
from consola.estetica import *

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

    def agregar_categoria(self, categoria: Categoria) -> str:
        '''Metodo para guardar en la lista de datos una categoria'''
        if self._categorias:
            for i in self._categorias:
                if i.id == categoria.id:
                    return f"{NARANJA}Esta categoria ya esta en la lista.{BLANCO}"
        self._categorias.append(categoria)
        return f"{AZUL}Se agrego la categoria en la lista.{BLANCO}"

    def listar_categoria(self) -> None:
        '''Funcion que permite tanto al administrador como al cliente ver todas las categorias cargadas'''
        encontrado = False
        for i in self._categorias:
            if i and not i.eliminado:
                encontrado = True
                print(f"{AZUL}ID: {MORADO}{i.id}{AZUL} | {MORADO}{i.nombre}{AZUL}: {MORADO}{i.descripcion}{BLANCO}")
        if not encontrado:
            raise EntidadNoEncontradaError("No hay categorias cargadas.")

    def crear_categoria(self, nombre: str, descripcion: str) -> str:
        '''Funcion que permite al administrador crear una nueva categoria y guardarla en la lista de datos'''
        categoria = Categoria(nombre, descripcion)
        if self._categorias:
            for i in self._categorias:
                if i.id == categoria.id:
                    return f"{NARANJA}Esta categoria ya esta en la lista.{BLANCO}"
        self.agregar_categoria(categoria)
        return f"{AZUL}Se creo la categoria en la lista. ID generado: {MORADO}{categoria.id}{BLANCO}"

    def editar_categoria(self, _id: int, pedido_servicio=None) -> None:
        '''Funcion que permite al administrador editar una categoria y realizar los cambios en la lista de datos y si esta asignada a un producto.'''
        encontrado = False
        for i in self._categorias:
            if _id == i.id and not i.eliminado:
                encontrado = True
                print(f"{AZUL}Se encontro la categoria con ese ID{BLANCO}")
                nombre_nuevo = input_str(f"{AMARILLO}Escriba el nuevo nombre de la categoria: {BLANCO}", "Nombre")
                descripcion_nueva = input_str(f"{AMARILLO}Escriba la nueva descripción de la categoria: {BLANCO}", "Descripción")
                nombre_viejo = i.nombre
                i.nombre = nombre_nuevo.capitalize()
                i.descripcion = descripcion_nueva.capitalize()
                
                if pedido_servicio is not None:
                    for pedido in pedido_servicio.pedidos:
                        for f in pedido.detalles:
                            if f.producto and f.producto.categoria:
                                if f.producto.categoria.nombre == nombre_viejo:
                                    f.producto.categoria = i
        if encontrado:
            print(f"{AZUL}¡Categoria editada!{BLANCO}")
        else:
            raise EntidadNoEncontradaError("No se encontro ninguna categoria con ese ID")

    def eliminar_categoria(self, _id: int, pedido_servicio=None) -> None:
        '''Funcion que permite al administrador eliminar de la lista datos una categoria y tambien eliminarla si esta asignada en un producto'''
        encontrado = False
        for i in self._categorias:
            if _id == i.id and not i.eliminado:
                encontrado = True
                print(f"{AZUL}Se encontro la categoria con ese ID{BLANCO}")
                while True:
                    opcion = input(f"{AMARILLO}¿Usted esta seguro de eliminar esta categoria?(S/N): {BLANCO}").strip().lower()
                    match opcion:
                        case "s":
                            id_viejo = i.id
                            i.eliminado = True
                            
                            if pedido_servicio is not None:
                                for pedido in pedido_servicio.pedidos:
                                    for f in pedido.detalles:
                                        if f.producto and f.producto.categoria:
                                            if f.producto.categoria.id == id_viejo:
                                                f.producto.categoria = None
                                                
                            print(f"{AZUL}Eliminacion completada.{BLANCO}")
                            break
                        case "n":
                            print(f"{ROJO}Se cancelo la eliminacion, regresando...{BLANCO}")
                            break
                        case _:
                            print(f"{NARANJA}Escriba S o N.{BLANCO}")
        if not encontrado:
            raise EntidadNoEncontradaError("No se encontro ninguna categoria con ese ID")


def input_seleccion(mensaje):
    '''Input para validar la seleccion del menu principal'''
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
    '''Input para validar el ingreso de una cadena de texto'''
    while True:
        input_salid = input(mensaje)
        if not isinstance(input_salid, str):
            raise DatoInvalidoError(f"{que_es} debe de ser una cadena de texto")
        if not input_salid.strip():
            raise DatoInvalidoError(f"{que_es} no puede estar vacio")
        return input_salid.capitalize()

def input_int_id(mensaje, que_es):
    '''Input para validar el ingreso de un ID'''
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