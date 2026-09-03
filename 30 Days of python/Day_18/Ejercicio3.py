"""
Ejercicio 3
Limpia el siguiente texto y, tras limpiarlo, calcula las tres palabras más frecuentes:
El siguiente texto contiene varias direcciones de correo electrónico. Escribe un patrón que encuentre o extraiga las direcciones de email válidas:
"""
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
import re
#Limpiar el texto eliminando signos de puntuación y convirtiendo a minúsculas
cleaned_paragraph = re.sub(r'[^\w\s]', '', paragraph).lower()
print (cleaned_paragraph)
#Dividir el texto en palabras
words = cleaned_paragraph.split()
#Contar la frecuencia de cada palabra
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
#Ordenar las palabras por frecuencia
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
#Obtener las tres palabras más frecuentes
top_three = sorted_words[:3]
print(top_three)