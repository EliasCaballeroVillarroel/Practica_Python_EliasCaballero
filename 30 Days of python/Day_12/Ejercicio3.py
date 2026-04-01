"""
Ejercicio 3: Lista mezclada
"""
from random import shuffle, choices
import string
def numeros_lista ():
    numeros = ''.join(choices(string.digits, k=10)) # genera una cadena de 10 dígitos aleatorios utilizando la función choices() de la biblioteca random.
    numeros = list(int(numeros[i]) for i in range(len(numeros))) # convierte la cadena de dígitos en una lista de enteros utilizando una comprensión de listas.
    return numeros
def shuffle_list(lista):
    shuffle(lista) # la función shuffle() de la biblioteca random se utiliza para mezclar los elementos de la lista de forma aleatoria.
    return lista 
lista = numeros_lista() # se llama a la función numeros_lista() para generar una lista de números aleatorios y se asigna a la variable lista.
print("Lista original: " + str(lista)) # se imprime la lista original antes de mezclarla.
print("Lista mezclada: " + str(shuffle_list(lista))) # se llama a la función shuffle_list() para mezclar la lista y se imprime la lista mezclada.
