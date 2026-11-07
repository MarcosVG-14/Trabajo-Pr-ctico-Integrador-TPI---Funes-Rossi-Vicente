class Productoservicio:
    def __init__(self):
        self._productos = []
    
    @property
    def productos(self):
        return self._productos
    
    def __len__(self) -> int:
        return len(self._productos)

    def __iter__(self):
        return iter(self._productos)

    def __contains__(self, producto: "Producto") -> bool:
        return producto in self._productos

    def agregar_producto(self, producto):
        if self._productos:
            for i in self._productos:
                if i.id == producto.id:
                    return("Este producto ya esta en la lista.")
        self.productos.append(producto) 
        return("Se agrego el producto en la lista.")
########### seguir
def listar_producto(productoservicio):
    encontrado = False
    for i in productoservicio.productos:
        if i:
            encontrado = True
            print(f"ID: {i.id} | {i.nombre}: {i.precio}$ | Stock: {i.stock} | Categoria: {i.categoria.nombre}")
    if not encontrado:
        raise EntidadNoEncontradaError("No hay categorias cargadas.")