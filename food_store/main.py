from funciones_basicas import *
from entidades.pedido import Pedido
from entidades.detalle_pedido import DetallePedido
from entidades.producto import Producto
from entidades.categoria import Categoria
from entidades.usuario import Usuario
from enums import FormaPago, Rol, Estado
from servicios.categoriaservicio import Categoriaservicio
from datetime import datetime

# --- CATEGORÍAS ---
# 1. Listar
# 2. Crear
# 3. Editar
# 4. Eliminar
# 0. Volver
# Seleccione:

admin = Usuario(
    nombre="Ana",
    apellido="Pérez",
    mail="admin@foodstore.com",
    celular="261111222",
    contrasenia="admin123",
    rol=Rol.ADMIN
)

categoria1 = Categoria("Nombre de categoria", "Descripcion de categoria")
producto1 = Producto("Mesa", categoria1)
producto2 = Producto("Silla", None)
categoriaservicio1 = Categoriaservicio()
producto1.agregar_categoria(categoria1)
categoriaservicio1.agregar_categoria(categoria1)
detalle_pedido1 = DetallePedido()
detalle_pedido1.agregar_producto(producto1)
detalle_pedido1.agregar_producto(producto2)
pedido1 = Pedido(detalle_pedido1)

# print(admin.rol.value)

while True:
    print("""--- CATEGORÍAS ---
1. Listar
2. Crear
3. Editar
4. Eliminar
0. Volver""")
    seleccion = input_seleccion("Seleccione: ")
    match seleccion:
        case 1 | "1" | "uno" | "i" | "listar":
            listar(categoriaservicio1)
        case 2 | "2" | "dos" | "ii" | "crear":
            nombre = input_str("Escriba el nombre de la categoria: ", "Nombre")
            descripcion = input_str("Escriba la descripción de la categoria: ", "Descripción")
            crear_categoria(nombre, descripcion, categoriaservicio1)
        case 3 | "3" | "tres" | "iii" | "editar":
            nombre = input_str("Escriba el nombre de la categoria que desea buscar: ","Nombre")
            editar_categoria(nombre, categoriaservicio1, pedido1)
        case 4 | "4" | "cuatro" | "iv" | "eliminar":
            pass
        case 0 | "0" | "cero" | "o" | "zero" | "volver":
            print("Regresando...")
            break