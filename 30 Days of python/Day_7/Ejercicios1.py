"""
Ejercicios: Nivel 1
# Conjuntos
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

Encuentra la longitud del conjunto it_companies
Agrega 'Twitter' a it_companies
Inserta varias empresas IT a it_companies de una sola vez
Elimina una empresa de it_companies
¿Cuál es la diferencia entre remove() y discard()?
"""
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}


print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Netflix', 'Tesla', 'SpaceX']) #Update es para insertar varios mientras que add lo hago para uno 
print(it_companies)
it_companies.remove('IBM') #Remove elimina un elemento del conjunto pero si el elemento no existe lanza un error
print(it_companies)
it_companies.discard('Oracle') #Discard elimina un elemento del conjunto pero si el elemento no existe no lanza un error
print(it_companies)

