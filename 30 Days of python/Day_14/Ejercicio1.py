"""
Ejercicio 1 
"""
"""
Explica la diferencia entre map, filter y reduce.
1-La diferencia entre map, filter y reduce es que map se utiliza para aplicar una función a cada elemento de una secuencia y devolver una nueva secuencia con los resultados, filter se utiliza para filtrar elementos de una secuencia 
según una función de prueba y devolver una nueva secuencia con los elementos que cumplen la condición, y reduce se utiliza para aplicar una función de acumulación a los elementos de una secuencia y devolver un solo valor resultante.
2-Explica la diferencia entre funciones de orden superior, closures y decoradores.
La diferencia entre funciones de orden superior, closures y decoradores es que las funciones de orden superior son funciones que pueden tomar otras funciones como argumentos o devolver funciones como resultado, los closures son funciones que 
recuerdan el entorno en el que fueron creadas y pueden acceder a variables locales incluso después de que la función externa haya terminado de ejecutarse, y los decoradores son una forma special de funciones de orden superior que se utilizan para modificar el comportamiento de otras funciones sin cambiar su código fuente.
Imprime cada país de la lista countries usando un bucle for.
Imprime cada nombre de la lista names usando un bucle for.
Imprime cada número de la lista numbers usando un bucle for.
"""
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in countries:
    print(i)
for i in names:
    print(i)
for i in numbers:
    print(i)
    