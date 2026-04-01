"""
Ejercicio 3 
Accede al archivo de datos countries-data.py.
Crea una función llamada the_most_spoken_languages que devuelva las 10 o 20 lenguas más habladas en el mundo, ordenadas de mayor a menor.
Crea una función llamada the_most_populated_countries que devuelva los 10 o 20 países más poblados del mundo, ordenados de mayor a menor.
"""
from Data.countries_data import countries
def the_most_spoken_languages(cantidad):
    conteo_idiomas = {}

    for pais in countries:
        for idioma in pais["languages"]:
            if idioma in conteo_idiomas:
                conteo_idiomas[idioma] += 1
            else:
                conteo_idiomas[idioma] = 1

    idiomas_ordenados = sorted(conteo_idiomas.items(), key=lambda x: x[1], reverse=True)
    return idiomas_ordenados[:cantidad]
def the_most_populated_countries(cantidad):
    paises_ordenados = sorted(countries, key=lambda x: x["population"], reverse=True)
    return paises_ordenados[:cantidad]
print("10 lenguas más habladas:")
for idioma, conteo in the_most_spoken_languages(10):
    print(f"{idioma}: {conteo} países")
print("\n10 países más poblados:")
for pais in the_most_populated_countries(10):
    print(f"{pais['name']}: {pais['population']} habitantes")


