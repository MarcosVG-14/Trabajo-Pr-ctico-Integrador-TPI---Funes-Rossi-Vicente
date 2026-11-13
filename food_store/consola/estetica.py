import os

# AMARILLO: CUANDO HAY UN INPUT O SE REQUIERE QUE EL USUARIO INGRESE ALGO
# AZUL: TEXTO NUESTRO, INFORMACION DADA AL USUARIO
# NARANJA: ERRORES
# ROJO: MARCA LA ULTIMA OPCION, LA DE REGRESAR
# VERDE: MARCA LAS OTRAS OPCIONES EN LAS QUE PUEDE ACCEDER EL USUARIO
# MORADO: NOMBRADO DE LA INFORMACION DEL USUARIO

# Definición de colores ANSI
RESET = "\033[0m"
NEGRITA = "\033[1m"

# Colores de texto
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
BLANCO = "\033[37m"
NARANJA = "\033[38;5;208m"
MORADO = "\033[38;5;56m"


'''Función que regula la ejecución del programa para mantener un orden y tempo'''
def continuar():
    print()
    input("""-- Presione cualquier tecla para continuar --
""")

'''Función que limpia la consola para que se vea mejor'''
def limpiado_consola():
    if os.name == 'nt':
        os.system('cls') 
