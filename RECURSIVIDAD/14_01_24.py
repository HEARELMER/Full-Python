def factorial(number: int):
    if number ==1:
        return 1
    
    return number * factorial(number-1) 

# print(factorial(3))

        
def fibonacci(num_element):
    
    # print(limite)
    if num_element == 1 or num_element == 0:
        return 1
    first_element= fibonacci (num_element-2) #5,3 , 1
    second_element= fibonacci( num_element-1) # 6, 5 ,4 ,3,2,1
    return first_element + second_element

# print(fibonacci(7))  

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
# 0 + 1 = 1  => primer elemnto
# 1 + 1= 2  =>segundo elemento
# 1 + 2= 3  ..........
# 2 + 3= 5  ...........
# 3 + 5= 8  ........
# 5 + 8= 13  .......
# 8 + 13= 21  => septimo elemnto

def counter(number: int):
    
    if number == 0:
        return 
    print(number)
    return counter(number-1)



# counter(4)


def counter_ascending(number: int):
    if number == 0:
        return 0
    print('aqui sinsolcuionar')
    
    counter_ascending(number -1)#
    print('solcuionado')
    print(number)
    return 


# counter_ascending(4)


# prueba de rendimiento recursividad vs la funcion sum
# suma de pagina de libros

import time
start= time.time()
def count_pages_book(books: list, index= 0):
    if index == len(books):
        return 1
    return books[index]+  count_pages_book(books, index+1)

books=[4,23,23,12, 12]
# print(count_pages_book(books))

# end = time.time()
# print(f"{(end - start) :.7f}")

#funcion sum de python

# def count_pages(books):
#     if len(books)==0:
#         return 0
    
#     return sum(books)

# print(count_pages(books))

def  multiplication(first, second ):
    if second==1:
        return first
    return (first + multiplication(first, second-1))
    
# print(multiplication(3,3))

#funcion recursiva de potencia
def  power(base, exponent):
    if exponent==1:
        return base
    return (base * power(base, exponent-1))

# print(power(2,5))


# Tabla multiplcar con recursividad 
def multiplication_table(number: int,counter=1):
    if counter==13:
        return 1
    print(f"{number} x {counter} = {number* counter}")
    multiplication_table(number, counter +1)
    
    return (number)

# multiplication_table(9)

#Tabla multiplicar con FOR
def multi(limit:int):
    for i in range(1,13):
        print(f"{i} x {limit}={i * limit } ")
        
# multi(9)


### MAS EJERCICIOS DE RECURSIVIDAD
# Número de Dígitos:
# Implementa una función recursiva para contar el número de dígitos en un número entero.
def counter_digitNumber(number:int, index =0):
    if index == len(str(number)):
        return index
    return ( counter_digitNumber(number, index +1) )
  
# print(counter_digitNumber(88956689))  
# Inversión de Cadena:
# Crea una función recursiva para invertir una cadena de caracteres.
def reversed_string(word: str, indice = -1):
    if abs(indice) == len(word):
        return word[indice]
    return  word[indice]+ reversed_string(word, indice -1)

# print(reversed_string('ELMER jesus'))
# Suma de Elementos en una Lista:
# Desarrolla una función recursiva para calcular la suma de los elementos en una lista.

def sum_elementList(listNumbers: list, index = 0):
   
    if index == len(listNumbers):
        return 0
    return listNumbers[index] + sum_elementList(listNumbers, index +1 )
# print(sum_elementList([45,42,4,5,6,7]))
    
    
# Cálculo de MCD (Máximo Común Divisor):
# Implementa una función recursiva para calcular el MCD de dos números usando el algoritmo de Euclides.
def calculate_MCD(number1, number2):
    if number2 ==0:
        return number1
    return calculate_MCD(number2,number1%number2 )
# print(calculate_MCD(48,18))

# Generación de Subconjuntos:
# Escribe una función recursiva que genere todos los subconjuntos de un conjunto dado.
def subconjuntsGenerate(conjuntElements,  index=0, actual=[]):
    if index== len(conjuntElements):
        print(actual)
        return
    
    
    subconjuntsGenerate(conjuntElements, index + 1, actual + [conjuntElements[index]])

    subconjuntsGenerate(conjuntElements, index + 1, actual)

# print(subconjuntsGenerate([1, 2, 4 , 3]))
# Impresión de Números en Orden Inverso:
# Crea una función recursiva que imprima los números naturales desde 1 hasta N en orden inverso.
def numbers_order_revers(number: int):
    
    if number == 0:
        return 1
    print(number)
    return numbers_order_revers(number-1)
    

# numbers_order_revers(4)
# Recorrido de Listas Anidadas:
# Desarrolla una función recursiva para recorrer una lista anidada y calcular la suma de todos los elementos.

def list_anid(listsAnid: list, index = 0):
    # print(len(listsAnid))
    if index == len(listsAnid):
        return 0
    
    result =0
    if type(listsAnid[index]) == int:
        result = listsAnid [index] + list_anid(listsAnid, index +1 )
    elif type(listsAnid[index]) == list:
        result= list_anid(listsAnid[index], 0) + list_anid(listsAnid, index+1)
        
    return result
    

lista=[45,[4,7,8,9],42,[4,5],6,7]
print(list_anid(lista))


# Torres de Hanoi: Nosee como hacer
# Implementa una función recursiva para resolver el problema de las Torres de Hanoi.