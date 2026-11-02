from entidades.pedido import Pedido
from entidades.detallepedido import DetallePedido
from entidades.producto import Producto
from entidades.categoria import Categoria

def input_seleccion(mensaje):
    while True:
        input_salid = input(mensaje)
        if isinstance(input_salid, str):
            if not input_salid.strip():
                raise ValueError("La seleccion no puede estar vacía.")
            return input_salid.lower()
        elif (isinstance(input_salid, int) or isinstance(input_salid, float)):
            if not 0 > input_salid:
                raise ValueError("La seleccion no puede ser menor a cero")
            return input_salid
        else:
            raise TypeError("Escriba una opcion mostrada en pantalla")

def input_str(mensaje, que_es):
    while True:
        input_salid = input(mensaje)
        if not isinstance(input_salid, str):
            raise TypeError(f"{que_es} debe de ser una cadena de texto")
        if not input_salid.strip():
            raise ValueError(f"{que_es} no puede estar vacio")
        return input_salid.capitalize()

def listar(pedido):
    for i in pedido.detalle_pedido.productos:
        if i.categorias:
            if i.categorias > 1:
                print(f"El producto {i.nombre} posee las siguientes categorias:")
                for f in i.categorias:
                    print(f" {f.nombre} {f.descripcion}")
            else:
                print(f"El producto {i.nombre} posee las siguiente categoria: {i.categoria.nombre}: {i.categoria.descripcion}")
        else:
            print("Un producto listado no posee categoria.")

def crear_categoria(nombre, descripcion, lista):
    categoria = Categoria(nombre, descripcion)
    lista.append(categoria)