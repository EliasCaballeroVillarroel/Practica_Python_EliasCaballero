"""
Ejercicios: Nivel 2
#Conjunto de ejercicios para practicar los conceptos de conjuntos en Python.
Concatena A y B
Encuentra la intersección entre A y B
¿Es A un subconjunto de B?
¿Son A y B conjuntos disjuntos?
Combina A con B y viceversa
¿Cuál es la diferencia simétrica entre A y B?
Elimina un conjunto por completo
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

"""
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.union(B)) #Concatena A y B
print(A.intersection(B)) #Encuentra la intersección entre A y B
print(A.issubset(B)) #¿Es A un subconjunto de B?
print(A.isdisjoint(B)) #¿Son A y B conjuntos disjuntos?
print(A.symmetric_difference(B)) #¿Cuál es la diferencia simétrica entre A y B?
print(A.difference(B)) #¿Cuál es la diferencia entre A y B?
A.clear() #Elimina un conjunto por completo
print(A)
