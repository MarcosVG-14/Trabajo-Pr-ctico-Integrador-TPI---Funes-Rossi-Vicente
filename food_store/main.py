import getpass
from entidades.usuario import Usuario
from enums.enums import Rol
from servicios.usuario_servicio import UsuarioServicio
from servicios.categoriaservicio import Categoriaservicio
from servicios.productoservicio import Productoservicio
from servicios.pedido_servicio import PedidoServicio
from excepciones.excepciones import CredencialesInvalidasError
from consola.menu import crear_menu
from consola.estetica import *

def inicializar_datos(usuario_servicio: UsuarioServicio) -> None:
    """Carga los usuarios iniciales requeridos en memoria."""
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

def main() -> None:
    usuario_servicio = UsuarioServicio()
    categoria_servicio = Categoriaservicio()
    producto_servicio = Productoservicio()
    pedido_servicio = PedidoServicio()

    inicializar_datos(usuario_servicio)
    
    ejecutando_sistema = True

    while ejecutando_sistema:
        print(f"\n{AZUL}=== FOOD STORE INICIO DE SESIÓN ==={BLANCO}")
        intentos = 0
        sesion_activa: Usuario | None = None
        
        while intentos < 3:
            mail = input(f"{AMARILLO}Mail: {BLANCO}").strip()
            contrasenia = getpass.getpass(f"{AMARILLO}Contraseña: {BLANCO}")
            
            try:
                sesion_activa = usuario_servicio.autenticar(mail, contrasenia)
                print(f"\n{AZUL}¡Bienvenido/a, {MORADO}{sesion_activa.nombre} {sesion_activa.apellido} {AZUL}[{MORADO}{sesion_activa.rol.name}{AZUL}]!{BLANCO}")
                break
            except CredencialesInvalidasError as e:
                intentos += 1
                print(f"{NARANJA}Error: {e}. Intentos restantes: {3 - intentos}{BLANCO}")
        
        if sesion_activa is None:
            print(f"\n{AZUL}Has superado el número máximo de intentos. El programa finalizará.{BLANCO}")
            ejecutando_sistema = False
            break
        
        menu = crear_menu(sesion_activa, categoria_servicio, producto_servicio, usuario_servicio, pedido_servicio)
        mantiene_sesion = True

        while mantiene_sesion:
            resultado = menu.mostrar()
            if resultado == "salir":
                opcion_salida = input(f"{AMARILLO}¿Está seguro de que desea salir del programa? (S/N): {BLANCO}").strip().lower()
                if opcion_salida == "s":
                    print(f"{AZUL}¡Gracias por utilizar Food Store! Hasta luego.{BLANCO}")
                    ejecutando_sistema = False
                    break
            if resultado is False:
                print(f"{ROJO}Cerrando sesión...")
                break

if __name__ == "__main__":
    main()