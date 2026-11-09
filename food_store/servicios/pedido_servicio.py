from entidades.pedido import Pedido
from entidades.usuario import Usuario
from entidades.producto import Producto
from enums.enums import Estado, FormaPago
from excepciones.excepciones import EntidadNoEncontradaError, OperacionNoPermitidaError, DatoInvalidoError

class PedidoServicio:
    def __init__(self) -> None:
        self.__pedidos: List[Pedido] = []

    @property
    def pedidos(self) -> List[Pedido]:
        return self.__pedidos

    def agregar_pedido(self, pedido: Pedido) -> None:
        self.__pedidos.append(pedido)

    def buscar_por_id(self, _id: int) -> Pedido:
        """Busca un pedido activo por su ID."""
        for pedido in self.__pedidos:
            if pedido.id == _id and not pedido.eliminado:
                return pedido
        raise EntidadNoEncontradaError("No se encontró un pedido activo con ese ID.")

    def listar_pedidos_activos(self) -> List[Pedido]:
        """Devuelve una lista con todos los pedidos no eliminados."""
        return [p for p in self.__pedidos if not p.eliminado]

    def listar_pedidos_por_usuario(self, usuario: Usuario) -> List[Pedido]:
        """Devuelve los pedidos activos pertenecientes a un usuario específico."""
        return [p for p in self.__pedidos if not p.eliminado and p.usuario.id == usuario.id]

    def crear_pedido(self, usuario: Usuario, forma_pago: FormaPago, items: List[tuple[int, Producto]]) -> Pedido:
        """
        Crea un pedido validando el usuario, descontando stock de los productos
        y calculando el total mediante la interfaz Calculable.
        Items es una lista de tuplas: (cantidad, producto)
        """
        if usuario is None or usuario.eliminado:
            raise OperacionNoPermitidaError("No se puede crear un pedido sin un usuario válido o eliminado.")
        
        if not items:
            raise DatoInvalidoError("El pedido debe contener al menos un detalle.")

        nuevo_pedido = Pedido(usuario, forma_pago)

        try:
            for cantidad, producto in items:
                nuevo_pedido.agregar_detalle(cantidad, producto)
            
            for detalle in nuevo_pedido.detalles:
                detalle.producto.stock -= detalle.cantidad

            self.__pedidos.append(nuevo_pedido)
            return nuevo_pedido

        except Exception as e:
            raise e

    def cambiar_estado(self, pedido_id: int, nuevo_estado: Estado) -> None:
        """
        Actualiza el estado de un pedido respetando las transiciones válidas:
        PENDIENTE -> CONFIRMADO -> TERMINADO
        PENDIENTE o CONFIRMADO -> CANCELADO
        Si pasa a CANCELADO, se devuelve el stock.
        """
        pedido = self.buscar_por_id(pedido_id)
        estado_actual = pedido.estado

        transicion_valida = False

        if estado_actual == Estado.PENDIENTE:
            if nuevo_estado in (Estado.CONFIRMADO, Estado.CANCELADO, Estado.TERMINADO):
                transicion_valida = True
        elif estado_actual == Estado.CONFIRMADO:
            if nuevo_estado in (Estado.TERMINADO, Estado.CANCELADO):
                transicion_valida = True
        elif estado_actual in (Estado.TERMINADO, Estado.CANCELADO):
            transicion_valida = False

        if not transicion_valida:
            raise OperacionNoPermitidaError(
                f"Transición de estado inválida: de {estado_actual.name} a {nuevo_estado.name}."
            )

        if nuevo_estado == Estado.CANCELADO and estado_actual not in (Estado.CANCELADO, Estado.TERMINADO):
            for detalle in pedido.detalles:
                detalle.producto.stock += detalle.cantidad

        pedido.estado = nuevo_estado

    def eliminar_pedido(self, pedido_id: int) -> None:
        """
        Realiza la baja lógica de un pedido y sus detalles.
        Si no estaba TERMINADO ni CANCELADO, se devuelve el stock de sus productos.
        """
        pedido = self.buscar_por_id(pedido_id)

        if pedido.estado not in (Estado.TERMINADO, Estado.CANCELADO):
            for detalle in pedido.detalles:
                detalle.producto.stock += detalle.cantidad
            pedido.estado = Estado.CANCELADO

        pedido.eliminado = True
        for detalle in pedido.detalles:
            detalle.eliminado = True