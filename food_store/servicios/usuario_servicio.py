from enums.enums import Rol
from entidades.usuario import Usuario
from excepciones.excepciones import CredencialesInvalidasError

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

    def usuarios_activos(self) -> None:
        '''Función de administrador para listar usuarios, devuelve una lista con los usuarios que no están eliminados'''
        usuarios_no_eliminados = []
        for usuario in self.__usuarios:
            if not usuario.eliminado:
                usuarios_no_eliminados.append(usuario)
        return usuarios_no_eliminados

    def crear_usuario(self, nombre:str, apellido:str, mail:str, celular:str, contrasenia:str, rol:int) -> None:
        '''Función de administrador para crear un usuario'''
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(apellido, str):
            raise TypeError("El apellido debe ser una cadena de texto.")
        if not isinstance(mail, str):
            raise TypeError("El mail debe ser una cadena de texto.")
        if not isinstance(celular, str):
            raise TypeError("El celular debe ser una cadena de texto.")
        if not isinstance(contrasenia, str):
            raise TypeError("El contraseña debe ser una cadena de texto.")
        if "@" not in mail or "." not in mail:
            raise TypeError("El mail debe contener '@' y '.'")
        for usuario in self.__usuarios:
            if usuario.mail.lower() == mail.lower():
                raise ValueError("Ya existe un usuario registrado con ese mail.")
        if rol == 1:
            rol_enum = Rol.ADMIN
        elif rol == 2:
            rol_enum = Rol.USUARIO
        else:
            raise TypeError("El rol seleccionado es inválido.")
        nuevo_usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            mail=mail,
            celular=celular,
            contrasenia=contrasenia,
            rol=rol_enum
        )
        self.__usuarios.append(nuevo_usuario)

    def buscar_por_id(self, _id:int) -> Usuario:
        '''Busca un usuario activo por su ID y lo retorna, o lanza excepción.'''
        for usuario in self.__usuarios:
            if usuario.id == _id and not usuario.eliminado:
                return usuario
        raise EntidadNoEncontradaError("No se encontró un usuario activo con ese ID.")

    def eliminar_usuario(self, _id:int) -> None:
        for usuario in self.__usuarios:
            if usuario.id == _id and not usuario.eliminado:
                usuario.eliminado = True
