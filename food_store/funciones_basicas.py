from entidades.pedido import Pedido
from entidades.detalle_pedido import DetallePedido
from entidades.producto import Producto
from entidades.categoria import Categoria
from servicios.categoriaservicio import Categoriaservicio

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

def listar(categoriaservicio):
    encontrado = False
    for i in categoriaservicio.categorias:
        if i:
            encontrado = True
            print(f"ID: {i.id} | {i.nombre}: {i.descripcion}")
    if not encontrado:
        raise KeyError("No hay categorias cargadas.")

def crear_categoria(nombre, descripcion, categoriaservicio):
    categoria = Categoria(nombre, descripcion)
    categoriaservicio.agregar_categoria(categoria)

def editar_categoria(nombre, categoriaservicio, pedido): # CORREGIR
    encontrado = False
    for i in categoriaservicio.categorias:
        if nombre.capitalize() == i.nombre:
            encontrado = True
            print("Se encontro una categoria con ese nombre")
            nombre_nuevo = input_str("Escriba el nuevo nombre de la categoria: ", "Nombre")
            descripcion_nueva = input_str("Escriba la nueva descripción de la categoria: ", "Descripción")
            nombre_viejo = i.nombre
            descripcion_vieja = i.descripcion
            i.nombre = nombre_nuevo.capitalize()
            i.descripcion = descripcion_nueva.capitalize()
        for f in pedido.detalle_pedido.productos:
            if f.categoria:
                if f.nombre == nombre_viejo:
                    f = i
            # return i
    if encontrado:
        print("¡Categoria editada!")
    if not encontrado:
        raise KeyError("No se encontro ninguna categoria con ese nombre")

# def aplicacion_de_datos(catego, pedido):
#     for i in pedido.detalle_pedido.productos:
#         if i.categorias:
#             for f in i.categorias:
#                 if f.nombre == catego.nombre:
#                     f = catego

# def eliminar_categoria():