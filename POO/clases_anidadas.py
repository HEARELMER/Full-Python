class Car:
    def __init__ (self, valor) :
        self.valor=valor
        self.valor2= self.Funcion()

    @staticmethod
    def modelo():
        print('Toyota')

    class Funcion:
        @staticmethod
        def mostrar():
            print('hola desde metodo mostrar')


car1= Car('sentai')# isntancia de la clase car

car1.modelo()# muestra toyota

valor1= car1.valor2

valor1.mostrar()# muestra hola desde....


class Zoologico:
    def __init__(self):
        self.animales=[]

    def add_animals(self, nombre, especie):
        animal= self.Animal(nombre, especie)
        self.animales.append(animal)

    class Animal:
        def __init__(self,nombre, especie):
            self.nombre= nombre
            self.especie= especie
        def mostrarInfo(self):
            print(f'El nombre es: {self.nombre}, la espcie es: {self.especie}')
        def obtenerNombre(self):
            self.nombre= 'Gato'
            self.especie= 'Felino'

zoologico1= Zoologico()
zoologico1.add_animals('gato', 'mamdifetr')
zoologico1.add_animals('gato', 'mamdifetr')
zoologico1.add_animals('gato', 'mamdifetr')


# print(zoologico1.animales)
for animal in zoologico1.animales:
    print(animal)
    animal.mostrarInfo()
    # print()