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

