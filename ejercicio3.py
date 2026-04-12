class punto:
    def __init__(self, x, y):
       self.x = x
       self.y = y
    def impresion(self):
        return f"({self.x}, {self.y})"



        
class Linea:
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b
    
    def mueve_derecha(self, d):
        self.punto_a.x += d
        self.punto_b.x += d

    def mueve_izquierda(self, d):
        self.punto_a.x -= d
        self.punto_b.x -= d

    def mueve_arriba(self, d):
        self.punto_a.y += d
        self.punto_b.y += d

    def mueve_abajo(self, d):
        self.punto_a.y -= d
        self.punto_b.y -= d

        

        

    def impresion(self):
        return f"linea: A{self.punto_a.impresion()} B{self.punto_b.impresion()}"



x1=float(input("Ingrese el valor de x1: "))
y1=float(input("Ingrese el valor de y1: "))     
x2=float(input("Ingrese el valor de x2: "))
y2=float(input("Ingrese el valor de y2: ")) 
direccion=int(input("Ingrese a qué direccion desea moverla línea: 1=derecha, 2=izquierda, 3=arriba, 4=abajo: "))
d=float(input("ingrese el valor que desea mover sobre los ejes:"))

punto_a=punto(x1, y1)
punto_b=punto(x2, y2)  
linea = Linea(punto_a, punto_b)

if direccion==1:
    linea.mueve_derecha(d)
elif direccion==2:
    linea.mueve_izquierda(d)
elif direccion==3:
    linea.mueve_arriba(d)
elif direccion==4:
    linea.mueve_abajo(d)
else:
    print("opción inválida")
        

print(linea.impresion())
