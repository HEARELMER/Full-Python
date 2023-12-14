class Product:
    def __init__(self, id_product, name_pro):
        self.id_product=id_product
        self.name_pro= name_pro

    # def __str__(self):
    #     print(self.id_product)
     
product1= Product('1233', 'Celular')

print(f'Código: {product1.id_product}')


class Car:
    def reiniciar(self):
        self.velocimetro=0

car1= Car()# instaciación d ela clase car
car1.reiniciar()# se llama al métdo reiniciar 
car1.velocimetro=0# se asigna un atributo

print(car1.velocimetro)

import math

##clase carro
class Car:
    def __init__(self, x:float=0, y:float=0)->None:# método constructor
        self.move(x,y)#necetia el métdo 
        return
    
    def move(self, x:float, y:float)->None:#funcion move 
        self.x=x
        self.y=y

    def reset(self)->None:# sis e ejcuta este métdo se pasara este valor al metodo move
        self.move(0,0)

    def calcularDistancia(self, other:'Car')->float:
        return math.hypot(self.x - other.x,self.y - other.y)

car1= Car(12 ,44)
car2= Car(12,4)

# print(car1.x, car1.y)

# car1.reset()
print(car1.calcularDistancia(car2))

# print(car1.x, car1.y)


#objeto 4
class Product:
    cantidad=500
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio
        self.calcularIgv()
    def calcularIgv(self):
        self.igv= self.precio*0.18#con el self  se crea un nuevo atributo
        
product1= Product('Samsung', 125,)
# product1.calcularIgv()

print(f'Producto: {product1.nombre} , precio: {product1.precio}, igv: {product1.igv}')


class Product:
    cantidad= 5000
    def __init__(self, nombre, precio):
        self.nombre= nombre
        self.precio= precio
        # self.descuento(25)
    def descuento(self, porcentaje):
        self.precio= self.precio-self.precio* porcentaje/100


product1= Product('Iphone', 1354)
precio1=product1.precio
product1.descuento(25)
print(f'Nombre:{product1.nombre}, precio {precio1}, descuento{product1.precio}')