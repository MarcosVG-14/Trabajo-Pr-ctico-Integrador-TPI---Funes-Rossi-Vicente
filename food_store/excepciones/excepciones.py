

class FoodStoreError(Exception):
    """Excepción base para todos los errores de negocio del sistema."""
    pass


class EntidadNoEncontradaError(FoodStoreError):
    """ID inexistente o eliminado."""
    pass


class DatoInvalidoError(FoodStoreError):
    """Texto vacío, formato incorrecto."""
    pass


class PrecioInvalidoError(DatoInvalidoError):
    """Subclase de DatoInvalidoError para precios inválidos."""
    pass


class StockInsuficienteError(FoodStoreError):
    """Cantidad pedida mayor al stock."""
    pass


class DuplicadoError(FoodStoreError):
    """Mail o nombre de categoría repetido."""
    pass


class OperacionNoPermitidaError(FoodStoreError):
    """Transición de estado inválida, categoría con productos activos, o admin intentando eliminarse."""
    pass


class CredencialesInvalidasError(FoodStoreError):
    """Mail o contraseña incorrectos, o usuario eliminado."""
    pass