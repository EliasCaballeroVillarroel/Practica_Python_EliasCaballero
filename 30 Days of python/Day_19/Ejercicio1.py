"""


Ejercicios: Nivel 1
Escriba una función que cuente el número de líneas y el número de palabras en un texto. Todos los archivos están en la carpeta de datos:

Lea el archivo obama_speech.txt y cuente el número de líneas y palabras
Lea el archivo michelle_obama_speech.txt y cuente el número de líneas y palabras
Lea el archivo donald_speech.txt y cuente el número de líneas y palabras
Lea el archivo melina_trump_speech.txt y cuente el número de líneas y palabras
"""


from countries_data import countries

from collections import Counter


obama_lines = len(open("obama_speech.txt", "r").readlines()) #Al usar len y readlines() contamos el número de líneas en el archivo obama_speech.txt
obama_words = len(open("obama_speech.txt", "r").read().split()) #Al usar len y read().split() contamos el número de palabras en el archivo obama_speech.txt
print ("Obama speech: Lines:", obama_lines, "Words:", obama_words)  
michelle_lines = len(open("michelle_obama_speech.txt", "r").readlines())
michelle_words = len(open("michelle_obama_speech.txt", "r").read().split())
print ("Michelle Obama speech: Lines:", michelle_lines, "Words:", michelle_words)
donald_lines = len(open("donald_speech.txt", "r").readlines())
donald_words = len(open("donald_speech.txt", "r").read().split())
print ("Donald speech: Lines:", donald_lines, "Words:", donald_words)
melina_lines = len(open("melina_trump_speech.txt", "r").readlines())
melina_words = len(open("melina_trump_speech.txt", "r").read().split())
print ("Melina Trump speech: Lin    es:", melina_lines, "Words:", melina_words)
#2
#Read the countries_data data file in data directory, create a function that finds the ten most spoken languages

def most_spoken_languages(countries_data, amount=10):
	language_counter = Counter()

	for country in countries_data:
		language_counter.update(country["languages"])

	return language_counter.most_common(amount)


print("Los idiomas mas hablados son:")
for language, number in most_spoken_languages(countries):
	print(f"{language}: {number}")

print("Los 3 idiomas mas hablados son:")
for language, number in most_spoken_languages(countries, amount=3):
	print(f"{language}: {number}")


