"""Crea en countries.py funciones que usen los datos de countries_data.py:
una función para encontrar los 10 idiomas más usados
una función para encontrar los 10 países más poblados
"""
from Data.countries_data import countries
def most_spoken_languages(countries, n):
    languages = {}
    for country in countries:
        for language in country['languages']:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1
    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:n]

def most_populated_countries(countries, n):
    sorted_countries = sorted(countries, key=lambda x: x['population'], reverse=True)
    return [(country['name'], country['population']) for country in sorted_countries[:n]]
print(most_spoken_languages(countries, 10))
print(most_populated_countries(countries, 10))
