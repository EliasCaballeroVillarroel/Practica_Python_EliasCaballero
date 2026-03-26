#Para crear diccionarios usamos llaves tal y como en los conjuntos pero con la diferencia que cada elemento del diccionario es un par 
# clave-valor separados por dos puntos (:)
"""
Crea un diccionario vacío llamado dog
Añade las claves name, color, breed, legs y age al diccionario dog
Crea un diccionario student con las claves first_name, last_name, gender, age, marital status, skills, country, city y address
Obtén la longitud del diccionario student
Obtén el valor de skills y comprueba su tipo; debe ser una lista
Modifica skills añadiendo una o dos habilidades
Obtén la lista de claves del diccionario
Obtén la lista de valores del diccionario
Usa el método items() para convertir el diccionario en una lista de tuplas
Elimina un elemento del diccionario
Elimina uno de los diccionarios
"""
dog = { 
    "name": "Firulais",
    "color": "brown",
    "breed": "Labrador",
    "legs": 4,
    "age": 5
}
student = {
    "first_name": "Elias",
    "last_name": "Caballero",
    "gender": "Male",
    "age": 25,              
    "marital_status": "Dating",
    "skills": ["Python", "Data Analysis"],
    "country": "Argentina",
    "city": "Cordoba",
    "address": "Chacabuco 480"
}
print(len(student)) #Longitud del diccionario student
print(student["skills"]) #Valor de skills
print(type(student["skills"])) #Tipo de skills
student["skills"].append("Machine Learning") #Modificando skills añadiendo una habilidad
print(student["skills"])
print(student.keys()) #Lista de claves del diccionario
print(student.values()) #Lista de valores del diccionario
print(student.items()) #Convertir el diccionario en una lista de tuplas
del student["marital_status"] #Eliminar un elemento del diccionario
print(student)
del student #Eliminar el diccionario
