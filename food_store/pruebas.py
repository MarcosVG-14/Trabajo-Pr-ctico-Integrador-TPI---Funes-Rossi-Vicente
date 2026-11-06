from servicios.categoriaservicio import *
from entidades.pedido import Pedido
from entidades.detalle_pedido import DetallePedido
from entidades.producto import Producto
from entidades.categoria import Categoria
from entidades.usuario import Usuario
from enums.enums import FormaPago, Rol, Estado
from servicios.categoriaservicio import Categoriaservicio
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

categoria1 = Categoria("Nombre de categoria", "Descripcion de categoria")
producto1 = Producto("Mesa", 55000.5, "Madera de roble, 4 patas.", 5, "De frente", True)
producto1 = Producto("Silla", 35000.5, "Madera de roble, 4 patas.", 9, "De frente", True)
categoriaservicio1 = Categoriaservicio()
producto1.agregar_categoria(categoria1)
categoriaservicio1.agregar_categoria(categoria1)
detalle_pedido1 = DetallePedido(30, 300.2, None)
detalle_pedido1.agregar_producto(producto1)
pedido1 = Pedido(datetime.date, Estado.PENDIENTE, 90000.2, FormaPago.EFECTIVO)
pedido1.agregar_producto(detalle_pedido1)

sesion_activa = admin
sesion_activa.rol.value

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
            if sesion_activa.rol.value == "Admin" or sesion_activa.rol.value == "Usuario":
                listar(categoriaservicio1)
        case 2 | "2" | "dos" | "ii" | "crear":
            if sesion_activa.rol.value == "Admin":
                nombre = input_str("Escriba el nombre de la categoria: ", "Nombre")
                descripcion = input_str("Escriba la descripción de la categoria: ", "Descripción")
                crear_categoria(nombre, descripcion, categoriaservicio1)
            else:
                print("Usted no tiene los permisos necesarios para realizar esta opcion.")
        case 3 | "3" | "tres" | "iii" | "editar":
            if sesion_activa.rol.value == "Admin":
                _id = input_int("Escriba el ID de la categoria que desea buscar: ","ID")
                editar_categoria(_id, categoriaservicio1, pedido1)
            else:
                print("Usted no tiene los permisos necesarios para realizar esta opcion.")
        case 4 | "4" | "cuatro" | "iv" | "eliminar":
            if sesion_activa.rol.value == "Admin":
                _id = input_int("Escriba el ID de la categoria que desea buscar: ","ID")
                eliminar_categoria(_id, categoriaservicio1, pedido1)
            else:
                print("Usted no tiene los permisos necesarios para realizar esta opcion.")
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
