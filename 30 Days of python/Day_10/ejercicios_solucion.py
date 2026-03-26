import json
from collections import Counter

# Cargar datos de países
with open('Data/countries_data.py', 'r', encoding='utf-8') as f:
    content = f.read()
    # El archivo contiene una lista de diccionarios, la extraemos
    countries_data = eval(content)

# ============================================================================
# EJERCICIO 1: Iterar países y extraer aquellos que contienen "land"
# ============================================================================
print("=" * 70)
print("EJERCICIO 1: Países que contienen 'land' en su nombre")
print("=" * 70)

countries_with_land = [country['name'] for country in countries_data if 'land' in country['name'].lower()]
print(f"\nTotal de países con 'land' en el nombre: {len(countries_with_land)}")
for country in countries_with_land:
    print(f"  - {country}")

# ============================================================================
# EJERCICIO 2: Invertir lista de frutas usando un bucle
# ============================================================================
print("\n" + "=" * 70)
print("EJERCICIO 2: Invertir lista de frutas")
print("=" * 70)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(f"\nLista original: {fruits}")

fruits_reversed = []
for i in range(len(fruits) - 1, -1, -1):
    fruits_reversed.append(fruits[i])

print(f"Lista invertida: {fruits_reversed}")

# Alternativa con reverse en un bucle
print("\nAlternativa con bucle manual:")
fruits_copy = fruits.copy()
for i in range(len(fruits_copy) // 2):
    fruits_copy[i], fruits_copy[-(i+1)] = fruits_copy[-(i+1)], fruits_copy[i]
print(f"Lista invertida: {fruits_copy}")

# ============================================================================
# EJERCICIO 3: Análisis del archivo countries-data.py
# ============================================================================
print("\n" + "=" * 70)
print("EJERCICIO 3A: ¿Cuántos idiomas distintos hay?")
print("=" * 70)

all_languages = set()
for country in countries_data:
    for lang in country['languages']:
        all_languages.add(lang)

print(f"\nTotal de idiomas distintos: {len(all_languages)}")
print(f"Idiomas: {sorted(all_languages)}")

# ============================================================================
# EJERCICIO 3B: ¿Cuál es el idioma usado por más países?
# ============================================================================
print("\n" + "=" * 70)
print("EJERCICIO 3B: Idioma más usado por países")
print("=" * 70)

language_count = Counter()
for country in countries_data:
    for lang in country['languages']:
        language_count[lang] += 1

most_common_language = language_count.most_common(1)[0]
print(f"\nEl idioma más usado es: {most_common_language[0]}")
print(f"Usado por {most_common_language[1]} países")

# Top 10 idiomas
print("\nTop 10 idiomas más usados:")
for i, (language, count) in enumerate(language_count.most_common(10), 1):
    print(f"  {i}. {language}: {count} países")

# ============================================================================
# EJERCICIO 3C: Diez países con mayor población
# ============================================================================
print("\n" + "=" * 70)
print("EJERCICIO 3C: 10 países con mayor población")
print("=" * 70)

# Ordenar por población descendente
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

print("\nTop 10 países por población:")
for i, country in enumerate(sorted_by_population[:10], 1):
    population = country['population']
    population_formatted = f"{population:,}".replace(',', '.')
    print(f"  {i:2d}. {country['name']:30s} - {population_formatted} habitantes")

# Resumen
print("\n" + "=" * 70)
print("RESUMEN DE RESULTADOS")
print("=" * 70)
print(f"✓ Países con 'land': {len(countries_with_land)}")
print(f"✓ Idiomas distintos: {len(all_languages)}")
print(f"✓ Idioma más usado: {most_common_language[0]} ({most_common_language[1]} países)")
print(f"✓ País más poblado: {sorted_by_population[0]['name']} ({sorted_by_population[0]['population']:,} hab.)")
