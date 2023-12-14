class Padre:
    def __init__(self):
        self.precio= 25
        self.nombre= 'Jorge'
    def imprimir(self):
        print(f'El precio de padre es:  {self.precio}')
        print(f'El nombre es: {self.nombre}')

class Hijo(Padre):
    # def __init__(self):
    #     self.precio= 1250
    #     self.nombre='Elmer'
    def imprimir(self, precio):
        self.precio=precio
        
        print(f'El precio del hijo es: {self.precio}')
        print(f'El hijo es: {self.nombre}')
person1= Hijo()

person1.imprimir(50)