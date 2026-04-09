class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y
    
    def impresion(self):
        return f"({self.x}, {self.y})"
    
    def opuesto(self):
        return punto(-self.x, -self.y)
x=float(input("Ingrese el valor de x: "))
y=float(input("Ingrese el valor de y: "))
p = punto(x, y) 
print("El punto es:", p.impresion())

p_opuesto = p.opuesto()
print("Punto opuesto:", p_opuesto.impresion())
