# PROGRAMACIÓN ORIENTADA A OBJETOS

### Programación orientada a objetos:

- Es un paradigma de la progrmación y se basa en abstraer el mundo real y representarlo en la programación.

### Programación funcional vs POO

*Programación funcional*

```python
def producto():
    producto_nombre= input('Ingresar nombre: ')
    producto_precio= input('Ingresar precio: ')

producto()
```
*Programación orientada a objetos*

```python
class Product:
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio= precio

    def traer_Data(self):
        self.nombre= input('Ingrsar nombre: ')
        self.precio= input('Ingrse precio : ')

    def actulizarDatos(self):
        print(self.nombre)
        print(self.precio)


product1= Product('', '')

product1.traer_Data()

product1.actulizarDatos()
```

### Ejemplos de clases

```python

# Primer ejemplo
class Product:
    def __init__(self, id_product, name_pro):
        self.id_product=id_product
        self.name_pro= name_pro

    # def __str__(self):
    #     print(self.id_product)
     
product1= Product('1233', 'Celular')

print(f'Código: {product1.id_product}')

#segundo ejemplo
class Car:
    def reiniciar(self):
        self.velocimetro=0

car1= Car()# instaciación d ela clase car
car1.reiniciar()# se llama al métdo reiniciar 
car1.velocimetro=0# se asigna un atributo

print(car1.velocimetro)

# tercer ejemplo
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


#ejemplo 4
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

# ejemplo 5
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
```

### Clases anidadas

```python
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
```

### Herencia

```python
class Product:
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio= precio

    def traer_Data(self):
        self.nombre= input('Ingrsar nombre: ')
        self.precio= input('Ingrse precio : ')

    def actulizarDatos(self):
        print(self.nombre)
        print(self.precio)

class ProductDigital(Product):# herencia de la clase Product
    def __init__(self, link):
        self.link= link

    def traer_Data2(self):
        self.link= input('Ingrese enlace: ')

    def actualizar(self):
        print(self.link)

    
libro= ProductDigital('')
libro.traer_Data()
libro.traer_Data2()
libro.actulizarDatos()
libro.actualizar()
```

### Múltiple herencia

```python
class A:
    def metodo1(self):
        print('metodo 1')


class B(A):
    def metodo2(self):
        print('metodo 2')

# herencia de las clase A  Y B
class C(B):
    def metodo3(self):
        print('metodo 3')

objeto= C()

objeto.metodo1()
objeto.metodo2()
objeto.metodo3()
```

### Superclase
- Te permite heredar todos a los atributos de la clase padre.
```python
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
```
### Herencias constructoras

```python
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
```
### Instanciamiento

```python
class Estudiante:
    def __init__(self, nombre):
        self.nombre= nombre

    def hola(self):
        print(f'hola {self.nombre}')

    def len_name(self):
        return len(self.nombre)


estudiante1= Estudiante('Elmer')

estudiante1.hola()
print(estudiante1.len_name())

```

### Ejercicios

```python
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

vehiculo1= Vehiculo('25', 'rojo')
vehiculo1.mostrar()
carro1=Car('36', 'azul')
carro1.mostrar()
```