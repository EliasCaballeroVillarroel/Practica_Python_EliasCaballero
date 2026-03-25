"""
Convierte la lista de edades a un conjunto y compara la longitud de la lista y la del conjunto: ¿cuál es mayor?
Explica la diferencia entre estos tipos de datos: cadena, lista, tupla y conjunto
Para la frase "Soy profesor, me gusta motivar y enseñar a las personas." ¿cuántas palabras únicas tiene? Usa split() y conjuntos para obtener las palabras únicas.
"""
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)
print(len(age)) #Longitud de la lista
print(len(age_set)) #Longitud del conjunto  
#La longitud de la lista es mayor que la del conjunto porque el conjunto no permite elementos duplicados, mientras que la lista sí los permite.
#Cadena: Es una secuencia de caracteres encerrada entre comillas. Ejemplo: "Hola Mundo"
#Lista: Es una colección ordenada y mutable de elementos, que pueden ser de diferentes tipos
#Tupla: Es una colección ordenada e inmutable de elementos, que pueden ser de diferentes tipos
#Conjunto: Es una colección no ordenada de elementos únicos, que pueden ser de diferentes
#En la frase "Soy profesor, me gusta motivar y enseñar a las personas." hay 8 palabras únicas: "Soy", "profesor,", "me", "gusta", "motivar", "y", "enseñar", "a", "las", "personas."
sentence = "Soy profesor, me gusta motivar y enseñar a las personas."
unique_words = set(sentence.split())
print(unique_words)
print(f"Number of unique words: {len(unique_words)}")