# servicios
from servicios.categoriaservicio import *
from servicios.productoservicio import *
from servicios.categoriaservicio import Categoriaservicio
from servicios.productoservicio import Productoservicio
# entidades
from entidades.pedido import Pedido
from entidades.detalle_pedido import DetallePedido
from entidades.producto import Producto
from entidades.categoria import Categoria
from entidades.usuario import Usuario
#enums
from enums.enums import FormaPago, Rol, Estado
#otros
from datetime import datetime

admin = Usuario(
    nombre="Ana",
    apellido="Pérez",
    mail="admin@foodstore.com",
    celular="261111222",
    contrasenia="admin123",
    rol=Rol.ADMIN
)

normal = Usuario(
    nombre="Ana",
    apellido="Pérez",
    mail="admin@foodstore.com",
    celular="261111222",
    contrasenia="admin123",
    rol=Rol.USUARIO
)

categoria1 = Categoria("sal", "tra")
producto1 = Producto("Mesa", 55000.5, "Madera de roble, 4 patas.", 5, "De frente", True)
producto2 = Producto("Silla", 35000.5, "Madera de roble, 4 patas.", 9, "De frente", True)
productoservicio1 = Productoservicio()
producto1.agregar_categoria(categoria1)
productoservicio1.agregar_producto(producto1)
productoservicio1.agregar_producto(producto2)
detalle_pedido1 = DetallePedido(30, 300.2, None)
detalle_pedido1.agregar_producto(producto1)
pedido1 = Pedido(datetime.date, Estado.PENDIENTE, 90000.2, FormaPago.EFECTIVO)
pedido1.agregar_detalle(detalle_pedido1)

sesion_activa = admin
sesion_activa.rol.value

while True:
    print("""--- PRODUCTOS ---
1. Listar
2. Crear
3. Editar
4. Eliminar
0. Volver""")
    seleccion = input_seleccion("Seleccione: ")
    match seleccion:
        case 1 | "1" | "uno" | "i" | "listar":
            listar_producto(productoservicio1)
        case 2 | "2" | "dos" | "ii" | "crear":
            pass
        case 3 | "3" | "tres" | "iii" | "editar":
            pass
        case 4 | "4" | "cuatro" | "iv" | "eliminar":
            pass
        case 0 | "0" | "cero" | "o" | "zero" | "volver":
            print("Regresando...")
            break
        case 5 | "5":
            if sesion_activa.rol.value == "Usuario":
                sesion_activa = admin
                print("super israel")
            elif sesion_activa.rol.value == "Admin":
                sesion_activa = normal
                print("super gay")
            else:
                print("ele")

        case _:
            print("Ingrese una opcion mostrada en pantalla.")

