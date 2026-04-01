"""
Ejercicio 1 : Comprension de listas 
"""
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
notpositive_numbers = [number for number in numbers if number <= 0] # se crea una nueva lista negative_numbers utilizando una comprensión de listas. La comprensión de listas itera sobre cada número en la lista numbers y agrega solo aquellos números que son menores o iguales a cero a la nueva lista.
print(notpositive_numbers) # se imprime la lista notpositive_numbers, que contiene solo los números no positivos 

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flat_list = [number for sublist in list_of_lists for innerlist in sublist for number in innerlist] # se crea una nueva lista flat_list utilizando una comprensión de listas anidada. La comprensión de listas itera sobre cada sublista en list_of_lists, luego sobre cada innerlist dentro de cada sublista, y finalmente sobre cada número dentro de cada innerlist, agregando todos los números a la nueva lista flat_list.
print(flat_list) # se imprime la lista flat_list, que contiene todos los números de las
"""
Crear la siguiente lista de tuplas 
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
"""
list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)] # se crea una nueva lista de tuplas utilizando una comprensión de listas. La comprensión de listas itera sobre los números del 0 al 10 (inclusive) y para cada número i, crea una tupla que contiene el número i, el número 1, el número i nuevamente, el número i elevado al cuadrado, el número i elevado al cubo, el número i elevado a la cuarta potencia y el número i elevado a la quinta potencia. Estas tuplas se agregan a la nueva lista list_of_tuples.
print(list_of_tuples) # se imprime la lista list_of_tuples, que contiene las tuplas generadas.


"""
countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]] 
Ordenar pero agregando la abreviacion del país al inicio de cada tupla, por ejemplo:
[('FIN', 'Finlandia', 'Helsinki'), ('SWE', 'Suecia', 'Estocolmo'), ('NOR', 'Noruega', 'Oslo')]
"""
countries = [[('Finlandia', 'Helsinki')], [('Suecia', 'Estocolmo')], [('Noruega', 'Oslo')]]
abbreviations = ['FIN', 'SWE', 'NOR'] # se crea una lista de abreviaturas para los países.
sorted_countries = [(abbreviations[i], country[0][0], country[0][1]) for i, country in enumerate(countries)] # se crea una nueva lista sorted_countries utilizando una comprensión de listas. La comprensión de listas itera sobre cada país en la lista countries utilizando la función enumerate() para obtener tanto el índice como el país. Para cada país, se crea una tupla que contiene la abreviatura correspondiente (obtenida de la lista abbreviations utilizando el índice), el nombre del país (obtenido de la primera posición de la tupla dentro de la lista countries) y la capital del país (obtenida de la segunda posición de la tupla dentro de la lista countries). Estas tuplas se agregan a la nueva lista sorted_countries.
print(sorted_countries) # se imprime la lista sorted_countries, que contiene las tuplas
