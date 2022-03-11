def creciente(lista):
    bandera = True

    #Iteramos para saber si está ordenada de manera creciente
    for i in range (len(lista)-1):
        if lista[i] > lista[i+1]:
            bandera = False
    return bandera

def decreciente(lista):
    bandera = True

    #Iteramos para saber si está ordenada de manera decreciente
    for i in range (len(lista)-1):
        if lista[i] < lista[i+1]:
            bandera = False
    return bandera


n = int(input())

#Creamos nuestra lista vacía
if 3 <= n <= 1000:
    nums = input()
    lista = [int (i) for i in nums.split()]

    print(lista)

    if creciente(lista):
        print('CRECIENTE')

    elif decreciente(lista):
        print('DECRECIENTE')

    else:
        print('DESORDENADO')


