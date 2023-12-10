# Guía de Métodos y Operaciones en Python: Listas, Conjuntos y Diccionarios

# Método count => devuelve la cantidad de veces que se repite el elemento

saludo = 'hohola'
c = saludo.count('ho')
print(c)  # Devuelve 2

# Método extend
# Diferencia con append: permite agregar varios elementos iterables a la lista

a = [2, 4, 5, 2, 4]
a.extend('hola')  # Agrega cada letra como un elemento
print(a)

# Método insert
# Permite agregar elementos indicando el (índice, elemento_agregado)

a = [2, 3, 42, 4, 3]
a.insert(1, 'hola')
print(a)

# Método pop
# Elimina el último elemento o el elemento en el índice especificado

a = [2, 3, 51, 424]
print(a.pop())  # Elimina el último elemento
print(a)

# Pero si se le indica el índice, eliminará el elemento en ese índice

a = [2, 3, 51, 424]
print(a.pop(0))
print(a)

# Método append
# Permite agregar elementos, pero solo como un elemento más y no como un iterable

a = [2, 3, 51, 424]
a.append('aquí el elemento')
print(a)

# Funciones min, max, len, sum
# Operaciones comunes en listas

c = ['hola', 'a', 'zc']
print(min(c))  # Mínimo (también funciona con cadenas)
print(max(c))  # Máximo
print(len(c))  # Longitud
# Sumatoria (No funciona con cadenas)
print(sum(c))

# Método sorted y método sort
a = [223, 32, 51, 424]

# Utilizando el método sorted para mostrar una nueva lista ordenada
sorted_list = sorted(a)
print('Lista ordenada (sorted): ', sorted_list)

# La lista original no se modifica
print('Lista original: ', a)

# Utilizando el método sort para ordenar la lista original
a.sort()
print('Lista ordenada (sort): ', a)

# La lista original se modifica directamente
print('Lista original modificada: ', a)

# Más cosas con sorted
from operator import itemgetter

f = [(5, 3), (2, 8), (-2, -25), (-5, -10), (-2, -3), (2, 3)]

# Ordena la lista de tuplas según el orden natural de los elementos de las tuplas
sorted_f = sorted(f)
print("Orden natural:", sorted_f)

# Ordena la lista de tuplas según el primer elemento de cada tupla
sorted_f_key_0 = sorted(f, key=itemgetter(0))
print("Ordenado por el primer elemento:", sorted_f_key_0)

# Ordena la lista de tuplas primero por el primer elemento y luego por el segundo elemento
sorted_f_key_01 = sorted(f, key=itemgetter(0, 1))
print("Coordenadas ordenadas por x y luego por y:")
for item in sorted_f_key_01:
    print(item)

# Ordena la lista de tuplas según el segundo elemento de cada tupla
sorted_f_key_1 = sorted(f, key=itemgetter(1))
print("Ordenado por el segundo elemento:", sorted_f_key_1)

# Ordena la lista de tuplas según el segundo elemento de cada tupla en orden descendente
sorted_f_key_1_reverse = sorted(f, key=itemgetter(1), reverse=True)
print("Ordenado por el segundo elemento en orden descendente:", sorted_f_key_1_reverse)

# Método set
# Es un conjunto desordenado que no permite datos duplicados
set1 = set()  # Aquí se está creando un conjunto vacío
set1.add('hola mundo')
print(set1)

set1.add((13, 3, 5))  # No se puede agregar una lista
set1.add(22)
set1.add(22)
set1.add('zola')

set1.update('actualizado')  # Este lo agrega como si estuviera iterando
set1.add('actualizado')  # Este lo agrega como un elemento completo

set1.remove('hola mundo')

print(set1)

# También se puede crear con llaves
set2 = set({2, 4, 4, 'hola', 22})
print(set2)

# Diferencia de conjuntos: devuelve elementos del set1 que no se repiten en el set2
print(set1 - set2)

# Intersección de conjuntos: solo devuelve los elementos que se repiten en ambos conjuntos
print(set1 & set2)

# También puedes usar llaves para crear conjuntos
set3 = {1, 22, 3, 5, 6, 7, 8, 9, 10, 11}

print(set1 & set2 & set3)
print(set1 and set2 and set3)  # Este devuelve el último conjunto

# Conjuntos inmutables
set4 = frozenset()
print(type(set4))

set5 = frozenset([22, 4, 3, 5, 34, 4])  # Esto sí permite listas
set6 = set5 & set1
print(type(set6))

## Diccionarios

dic = dict(a=2, d=3)  # Una forma de crear un diccionario
dic1 = {'a': 2, 'd': 3}  # Segunda forma
dic2 = dict(zip(['a', 'd', 'b'], [2, 3]))  # Tercera forma

print(dic2 == dic == dic1)  # Retorna True

# Esto creará una lista de tuplas
list_1 = list(zip(['e', 'l', 'm', 'e'], [1, 2, 3], [4, 6]))
print(list_1)  # Resultado: [('e', 1, 4)]

# También se puede hacer iteraciones
list_2 = list(zip('Nicoll', range(1, 9), range(-9, 5)))
print(list_2)

