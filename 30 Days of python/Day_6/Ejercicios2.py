"""Desempaquetar hermanos y padres de family_members
Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable llamada food_stuff_tp.
Cambie la tupla about food_stuff_tp a una lista food_stuff_lt
Corte el elemento o elementos del medio de la tupla food_stuff_tp o de la lista food_stuff_lt.
Corte los primeros tres elementos y los últimos tres elementos de la lista food_stuff_lt
Elimine la tupla food_stuff_tp por completo
Comprueba si existe un elemento en la tupla:
Comprueba si 'Estonia' es un país nórdico

Comprueba si 'Islandia' es un país nórdico
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
"""

frutas = ("manzana", "banana", "naranja")
verduras = ("lechuga", "tomate", "zanahoria")
productos_animales = ("leche", "huevos", "queso")
food_stuff_tp = frutas + verduras + productos_animales
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
middle_index = len(food_stuff_tp) // 2
middle_elements_tp = food_stuff_tp[middle_index - 1: middle_index + 1]
middle_elements_lt = food_stuff_lt[middle_index - 1: middle_index + 1]
print("Elementos del medio en tupla:", middle_elements_tp)
print("Elementos del medio en lista:", middle_elements_lt)
first_three_lt = food_stuff_lt[:3]
last_three_lt = food_stuff_lt[-3:]
print("Primeros tres elementos de la lista:", first_three_lt)
print("Últimos tres elementos de la lista:", last_three_lt)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("¿Estonia es un país nórdico?", 'Estonia' in nordic_countries)
print("¿Islandia es un país nórdico?", 'Iceland' in nordic_countries)

