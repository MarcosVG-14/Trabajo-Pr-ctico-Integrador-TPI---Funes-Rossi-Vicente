import getpass
from entidades.usuario import Usuario
from entidades.categoria import Categoria
from enums.enums import Rol
from servicios.usuario_servicio import UsuarioServicio
from servicios.categoriaservicio import Categoriaservicio
from excepciones.excepciones import CredencialesInvalidasError, FoodStoreError
from consola.menu import crear_menu

def inicializar_datos(usuario_servicio: UsuarioServicio, categoria_servicio: Categoriaservicio) -> None:
    """Carga los usuarios y categorías iniciales requeridos en memoria."""
    admin = Usuario(
        nombre="Ana",
        apellido="Pérez",
        mail="admin@foodstore.com",
        celular="261111222",
        contrasenia="admin123",
        rol=Rol.ADMIN
    )
    cliente = Usuario(
        nombre="Juan",
        apellido="Gómez",
        mail="cliente@foodstore.com",
        celular="261333444",
        contrasenia="user123",
        rol=Rol.USUARIO
    )
    usuario_servicio.agregar_usuario(admin)
    usuario_servicio.agregar_usuario(cliente)

    cat_inicial = Categoria("Bebidas", "Gaseosas, jugos y aguas")
    categoria_servicio.agregar_categoria(cat_inicial)

def main() -> None:
    usuario_servicio = UsuarioServicio()
    categoria_servicio = Categoriaservicio()
    producto_servicio = None
    pedido_servicio = None

    inicializar_datos(usuario_servicio, categoria_servicio)
    
    ejecutando_sistema = True

    while ejecutando_sistema:
        print("\n=== FOOD STORE INICIO DE SESIÓN ===")
        intentos = 0
        sesion_activa: Usuario | None = None
        
        while intentos < 3:
            mail = input("Mail: ").strip()
            contrasenia = getpass.getpass("Contraseña: ")
            
            try:
                sesion_activa = usuario_servicio.autenticar(mail, contrasenia)
                print(f"\n¡Bienvenido/a, {sesion_activa.nombre} {sesion_activa.apellido} [{sesion_activa.rol.name}]!")
                break
            except CredencialesInvalidasError as e:
                intentos += 1
                print(f"Error: {e}. Intentos restantes: {3 - intentos}")
        
        if sesion_activa is None:
            print("\nHas superado el número máximo de intentos. El programa finalizará.")
            ejecutando_sistema = False
            break
        
        menu = crear_menu(sesion_activa, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio)
        mantiene_sesion = True

        while mantiene_sesion:
            try:
                resultado = menu.mostrar()
                if resultado == "salir":
                    opcion_salida = input("¿Está seguro de que desea salir del programa? (S/N): ").strip().lower()
                    if opcion_salida == "s":
                        print("¡Gracias por utilizar Food Store! Hasta luego.")
                        ejecutando_sistema = False
                        break
                if resultado is False:
                    print("Cerrando sesión...")
                    break
            except FoodStoreError as e:
                print(f"\n[Error de Negocio]: {e}")
            except ValueError as e:
                print(f"\n[Error de Formato]: {e}")

if __name__ == "__main__":
    main()