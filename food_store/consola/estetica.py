import os

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
NARAJNA = "\033[38;5;208m"


'''Función que regula la ejecución del programa para mantener un orden y tempo'''
def continuar():
    print()
    input("""-- Presione cualquier tecla para continuar --
""")

'''Función que limpia la consola para que se vea mejor'''
def limpiado_consola():
    if os.name == 'nt':
        os.system('cls') 
