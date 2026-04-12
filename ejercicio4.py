class Cancion:
    def __init__ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
    
    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor

titulo=input("Ingrese el titulo de la cancion: ")
autor=input("ingrese el autor de la cancion: ")

tema = Cancion(titulo, autor)

print("Titulo de la cancion: ", tema.get_titulo())
print("Autor: ", tema.get_autor())

nuevo_titulo = input("Ingrese nuevamente el titulo: ")
nuevo_autor = input("Ingrese nuevamente el autor: ")

tema.set_titulo(nuevo_titulo)
tema.set_autor(nuevo_autor)

print("Titulo de la cancion: ", tema.get_titulo())
print("Titulo del autor: ", tema.get_autor())
