class Libros:
    def __init__ (self,titulo,autor,precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
    def info_libro(self):
         return f"Título: {self.titulo}, Autor: {self.autor}, Precio: ${self.precio}"

mi_libro = ("pato, elmer, 90")
print(mi_libro)

