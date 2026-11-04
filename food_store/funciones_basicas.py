from entidades.pedido import Pedido
from entidades.detalle_pedido import DetallePedido
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
            if len(i.categorias) > 1:
                print(f"El producto {i.nombre} posee las siguientes categorias:")
                for f in i.categorias:
                    print(f"{f.nombre}: {f.descripcion}")
            else:
                print(f"El producto {i.nombre} posee las siguiente categoria: {i.categoria.nombre}: {i.categoria.descripcion}")
        else:
            print("Un producto listado no posee categoria.")

def crear_categoria(nombre, descripcion, lista):
    categoria = Categoria(nombre, descripcion)
    lista.append(categoria)

def buscar_categoria(nombre, categorias):
    encontrado = False
    for i in categorias:
        if nombre.capitalize() == i.nombre:
            encontrado = True
            print("Se encontro una categoria con ese nombre")
            nombre_nuevo = input_str("Escriba el nuevo nombre de la categoria: ", "Nombre")
            descripcion_nueva = input_str("Escriba la nueva descripción de la categoria: ", "Descripción")
            i.nombre = nombre_nuevo.capitalize()
            i.descripcion = descripcion_nueva.capitalize()
            print("¡Categoria editada!")
            return i
    if not encontrado:
        raise KeyError("No se encontro ninguna categoria con ese nombre")

# def aplicacion_de_datos(catego, pedido):
#     for i in pedido.detalle_pedido.productos:
#         if i.categorias:
#             for f in i.categorias:
#                 if f.nombre == catego.nombre:
#                     f = catego