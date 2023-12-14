class Padre:
    def __init__(self):
        self.precio= 5000
    def costo(self):
        print (f'Padre { self.precio}')

class Hijo(Padre):
    def __init__(self):
        super().__init__()
        self.hijo_costo=1500
    def costo(self):
        print(f'hijo {self.hijo_costo + self.precio}')


person1= Hijo()

person1.costo()