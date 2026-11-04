class Categoriaservicio:
    def __init__(self):
        self._categorias = []
    
    @property
    def categorias(self):
        return self._categorias
    
    def __len__(self) -> int:
        return len(self._categorias)

    def __iter__(self):
        return iter(self._categorias)

    def __contains__(self, categoria: "Categoria") -> bool:
        return producto in self._categorias

    def agregar_categoria(self, categoria):
        self.categorias.append(categoria) 