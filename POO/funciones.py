# def circulo(r):
#     area=3.14*(r**2)
#     perimetro=2*3.14*r
#     return area,perimetro

# a,b = circulo(15)
# print(f"El area del circulo es: {a}\n"
#       f"El perimetro del circulo es: {b}")


# def lista(numeros):
#     total=0
#     for i in numeros:
#         total=total+i
#     return total

# lista_numeros=[1,2,3,4,5,6,7,8,9]
# resultado=lista(lista_numeros)
# print(resultado)


# def eliminar_duplicados(numeros):
#     lista=[]
#     for i in numeros:
#         if i not in lista:
#             lista.append(i)
#     return lista

# lis_numeros1=[1,1,2,4,3,6,7,8,9,1,5,3,4,6,0,1,
#               1,2,4,6,3,7,8,9,1,5,3,4,6,0,1,1]
# resultado=eliminar_duplicados(lis_numeros1)
# print(resultado)


# numero5=10
# def incrementar():
#     global numero5
#     numero5=numero5+1
#     print(numero5)
# incrementar()

#palabra palindrome oso

palabra = input("Escribe tu palabra")
l=len(palabra)
palindrome=True
# ana
def palindrome():
    global palindrome,palabra,l
    for i in range(l):
        if palabra[i]!=palabra[l-i-1]:# 0 =! (4-0-1) =3 (antna)
            print([l-i-1])
            palindrome=False
            break
        else:
            palindrome=True
    return palindrome

def resultado(palindrome):
    if palindrome:
        print("la palabra es un palindrome")
    else:
        print("la palabra no es un palindrome")

resultado(palindrome())



def factorial(numero):
    if numero==1:
        return 1
    else:
        return numero*factorial(numero-1)



