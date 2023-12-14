# crandof clae
class Vehiculo:
    def __init__(self, velocidad, color):#cosntructro
        # isntaicnado varibles
        self.velocidad= velocidad
        self.color= color
    
    # instnacia de un metodo
    def mostrar(self):
        print(f'Velocidad: {self.velocidad}, color : {self.color}')


class Car(Vehiculo):
    pass

# iantnaciar unobjeto 

# vehiculo1= Vehiculo('25', 'rojo')
# vehiculo1.mostrar()
# carro1=Car('36', 'azul')
# carro1.mostrar()