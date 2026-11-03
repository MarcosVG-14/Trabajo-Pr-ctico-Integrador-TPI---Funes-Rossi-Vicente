from funciones_basicas import *
from entidades.pedido import Pedido
from entidades.detallepedido import DetallePedido
from entidades.producto import Producto
from entidades.categoria import Categoria

# --- CATEGORÍAS ---
# 1. Listar
# 2. Crear
# 3. Editar
# 4. Eliminar
# 0. Volver
# Seleccione:

categorias = []
categoria1 = Categoria("Nombre de categoria", "Descripcion de categoria")
categorias.append(categoria1)
producto1 = Producto(categoria1)
producto2 = Producto(None)
detalle_pedido1 = DetallePedido()
detalle_pedido1.agregar_producto(producto1)
detalle_pedido1.agregar_producto(producto2)
pedido1 = Pedido(detalle_pedido1)

while True:
    print("""
1. Listar
2. Crear
3. Editar
4. Eliminar
0. Volver""")
    seleccion = input_seleccion("Seleccione: ")
    match seleccion:
        case 1 | "1" | "uno" | "i" | "listar":
            listar(pedido1)
        case 2 | "2" | "dos" | "ii" | "crear":
            nombre = input_str("Escriba el nombre de la categoria: ", "Nombre")
            descripcion = input_str("Escriba la descripción de la categoria: ", "Descripción")
            crear_categoria(nombre, descripcion, categorias)
            for i in categorias:
                print(f"{i.nombre}: {i.descripcion}")
        case 3 | "3" | "tres" | "iii" | "editar":
            nombre = input_str("Escriba el nombre de la categoria que desea buscar: ","Nombre")
            catego = buscar_categoria(nombre, categorias)
            # aplicacion_de_datos(catego)
        case 4 | "4" | "cuatro" | "iv" | "eliminar":
            pass
        case 0 | "0" | "cero" | "o" | "zero" | "volver":
            print("Regresando...")
            break