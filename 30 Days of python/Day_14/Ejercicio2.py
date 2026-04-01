"""
Ejercicio 2
"""
from functools import reduce


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Usa map para convertir cada país en countries a mayúsculas y genera una nueva lista.
def mayusculas (pais):
    return pais.upper()

paises_mayusculas = list(map(mayusculas, countries))
print(paises_mayusculas)

def square (num):
    return num ** 2

cuadrados = list(map(square, numbers))
print(cuadrados)

nombres_mayusculas = list(map(mayusculas, names)) 
def got_land (palabra):
    palabra = palabra.lower()
    if 'land' in palabra:
        return palabra
    else:
        return False
paises_con_land = list(filter(got_land, countries))
print(paises_con_land)

def tiene_six_characters (palabra):
    palabra = palabra.lower()
    if len(palabra) >= 6:
        return palabra
    else:
        return False
paises_con_six_characters = list(filter(tiene_six_characters, countries))
print(paises_con_six_characters)

def empieza_con_E (palabra):
    palabra = palabra.lower()
    if palabra.startswith('e'):
        return palabra
    else:
        return False
paises_con_E = list(filter(empieza_con_E, countries))
print(paises_con_E)

def sum (num1, num2):
    return num1 + num2
suma_numeros = reduce(sum, numbers)
print(suma_numeros)

def concatenar (pais1, pais2):
    return pais1 + ' ' + pais2

paises_concatenados = reduce(concatenar, countries)
print(paises_concatenados)

#Encadena dos o más iteradores de lista (por ejemplo arr.map(callback).filter(callback).reduce(callback)).
paises_mayusculas_con_land = list(filter(got_land, map(mayusculas, countries)))
print(paises_mayusculas_con_land)

