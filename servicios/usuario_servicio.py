
from usuario import Usuario
from excepciones import CredencialesInvalidasError

class UsuarioServicio:
    def __init__(self) -> None:
        self.__usuarios: list[Usuario] = []

    def agregar_usuario(self, usuario: Usuario) -> None:
        """Método auxiliar para registrar usuarios en la colección."""
        self.__usuarios.append(usuario)

    def autenticar(self, mail: str, contrasenia: str) -> Usuario:
        """
        Verifica si las credenciales coinciden con algún usuario activo.
        
        Lanza CredencialesInvalidasError si:
        - El mail no existe
        - La contraseña no coincide
        - El usuario está dado de baja (eliminado == True)
        """
        for usuario in self.__usuarios:
            if usuario.mail.lower() == mail.strip().lower() and not usuario.eliminado:
                if usuario.verificar_contrasenia(contrasenia):
                    return usuario
        
        raise CredencialesInvalidasError("Mail o contraseña incorrectos")