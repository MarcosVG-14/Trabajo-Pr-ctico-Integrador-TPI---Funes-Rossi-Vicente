from enums.enums import Rol
from entidades.usuario import Usuario
from excepciones.excepciones import CredencialesInvalidasError, EntidadNoEncontradaError, DatoInvalidoError

class UsuarioServicio:
    def __init__(self) -> None:
        self.__usuarios: list[Usuario] = []

    def agregar_usuario(self, usuario: Usuario) -> None:
        """Método auxiliar para registrar usuarios en la colección."""
        self.__usuarios.append(usuario)

    def autenticar(self, mail: str, contrasenia: str) -> Usuario:
        """
        Verifica si las credenciales coinciden con algún usuario activo.
        """
        for usuario in self.__usuarios:
            if usuario.mail.lower() == mail.strip().lower() and not usuario.eliminado:
                if usuario.verificar_contrasenia(contrasenia):
                    return usuario
        
        raise CredencialesInvalidasError("Mail o contraseña incorrectos")

    def usuarios_activos(self) -> list[Usuario]:
        '''Función para listar usuarios activos'''
        usuarios_no_eliminados = []
        for usuario in self.__usuarios:
            if not usuario.eliminado:
                usuarios_no_eliminados.append(usuario)
        return usuarios_no_eliminados

    def crear_usuario(self, nombre: str, apellido: str, mail: str, celular: str, contrasenia: str, rol: int) -> None:
        '''Función para crear un usuario'''
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatoInvalidoError("El nombre no puede estar vacío.")
        if not isinstance(apellido, str) or not apellido.strip():
            raise DatoInvalidoError("El apellido no puede estar vacío.")
        if not isinstance(mail, str) or "@" not in mail or "." not in mail:
            raise DatoInvalidoError("El mail debe contener '@' y '.'")
        if not isinstance(celular, str) or not celular.strip():
            raise DatoInvalidoError("El celular no puede estar vacío.")
        if not isinstance(contrasenia, str) or not contrasenia.strip():
            raise DatoInvalidoError("La contraseña no puede estar vacía.")
        
        for usuario in self.__usuarios:
            if usuario.mail.lower() == mail.lower() and not usuario.eliminado:
                raise ValueError("Ya existe un usuario registrado con ese mail.")
        
        if rol == 1:
            rol_enum = Rol.ADMIN
        elif rol == 2:
            rol_enum = Rol.USUARIO
        else:
            raise DatoInvalidoError("El rol seleccionado es inválido (debe ser 1 o 2).")
        
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            mail=mail,
            celular=celular,
            contrasenia=contrasenia,
            rol=rol_enum
        )
        self.__usuarios.append(nuevo_usuario)

    def buscar_por_id(self, _id: int) -> Usuario:
        '''Busca un usuario activo por su ID y lo retorna, o lanza excepción.'''
        for usuario in self.__usuarios:
            if usuario.id == _id and not usuario.eliminado:
                return usuario
        raise EntidadNoEncontradaError("No se encontró un usuario activo con ese ID.")

    def eliminar_usuario(self, _id: int) -> None:
        for usuario in self.__usuarios:
            if usuario.id == _id and not usuario.eliminado:
                usuario.eliminado = True