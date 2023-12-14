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