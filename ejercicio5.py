class Persona:
    def __init__ (self, nombre):
        self.nombre = nombre

class Libro:
    def __init__(self, titulo, autor, ISBN, paginas, edicion, editorial, ciudad, pais, fecha):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.paginas = paginas
        self.edicion = edicion
        self.editorial = editorial
        self.ciudad = ciudad
        self.pais = pais
        self.fecha = fecha
        
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_ISBN(self):
        return self.ISBN
    
    def get_paginas(self):
        return self.paginas
    
    def get_edicion(self):
        return self.edicion
        
    def get_editorial(self):
        return self.editorial
    
    def get_ciudad(self):
        return self.ciudad
    
    def get_pais(self):
        return self.pais
    
    def get_fecha(self):
        return self.fecha
    
    def set_titulo(self, modificacion):
        self.titulo = modificacion

    def set_autor(self, modificacion):
        self.autor = modificacion
        
    def set_ISBN(self, modificacion):
        self.ISBN = modificacion

    def set_paginas(self, modificacion):
        self.paginas = modificacion

    def set_edicion(self, modificacion):
        self.edicion = modificacion

    def set_editorial(self, modificacion):
        self.editorial = modificacion

    def set_ciudad(self, modificacion):
        self.ciudad = modificacion

    def set_pais(self, modificacion):
        self.pais = modificacion

    def set_fecha(self, modificacion):
        self.fecha = modificacion   
    
titulo = input("Ingrese el titulo: ")
autor = input("Ingrese autor: ")
ISBN = input("Ingrese ISBN: ")
paginas = int(input("Ingrese cantidad de paginas: "))
edicion = input("Ingrese la edicion: ")
editorial = input("Ingrese la editorial: ")
ciudad =input("Ingrese la ciudad: ")
pais = input("Ingrese el pais: ")
fecha = input("Ingrese la fecha: ")
    
libro1 = Libro(titulo, autor, ISBN, paginas, edicion, editorial, ciudad, pais, fecha)

print("Titulo: ", libro1.get_titulo(), libro1.get_edicion())
print("Autor: ", libro1.get_autor())
print("ISBN: ", libro1.get_ISBN())
print(libro1.get_editorial(), libro1.get_ciudad(), libro1.get_pais())
print(libro1.get_fecha())
print(libro1.get_paginas(), "páginas")
