import math

print('Media y Desviación Estándar\n')

nDatos = int(input('Ingresa la cantidad de valores: '))

#Cremos nuestro array
datos = []

for i in range(0,nDatos):
    num = int(input(f'Numero {i}: '))
    datos.append(num)

def calcular_media(valores):
    suma = 0

    for valor in valores:
        suma += valor

    return suma / len(valores)

def desviacion_estandar(valores, media):
    suma = 0

    for valor in valores:
        suma += (valor - media) ** 2    

    raiz = suma / (len(valores) - 1)

    return math.sqrt(raiz)


media = calcular_media(datos)
dstan = desviacion_estandar(datos, media)
print('\nMedia: ', media)
print('Desviacion estandar: ', dstan)