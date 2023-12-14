def producto():
    producto_nombre= input('Ingresar nombre: ')
    producto_precio= input('Ingresar precio: ')

producto()


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