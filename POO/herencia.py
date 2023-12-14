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