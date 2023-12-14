def suma_numeros(*args):
    suma=0
    for num in args:
        suma=suma+num
    return suma


def productos(**kwargs):
    for key,value in kwargs.items():
        print (key,value)
