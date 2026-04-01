"""
Ejercicio 3:
Ordena los países por nombre, capital y población.
Ordena y obtiene los diez idiomas más usados.
Ordena y obtiene los diez países con mayor población.
"""
import Data.countries_data as data
def ordenar_paises (clave):
    paises_ordenados = sorted(data.countries, key=lambda x: x[clave])
    return paises_ordenados 
paises_ordenados_por_nombre = ordenar_paises('name')
print("Países ordenados por nombre:")
for pais in paises_ordenados_por_nombre:
    print(pais['name'])
paises_ordenados_por_capital = ordenar_paises('capital')
print("\nPaíses ordenados por capital:")
for pais in paises_ordenados_por_capital:
    print(pais['capital'])
paises_ordenados_por_poblacion = ordenar_paises('population')
print("\nPaíses ordenados por población:")
for pais in paises_ordenados_por_poblacion:
    print(pais['name'] + ": " + str(pais['population']))

# Extraer todos los idiomas y contar frecuencia
idiomas_contador = {}
for pais in data.countries:
    for idioma in pais['languages']:
        idiomas_contador[idioma] = idiomas_contador.get(idioma, 0) + 1

# Ordenar idiomas por frecuencia (descendente)
idiomas_ordenados = sorted(idiomas_contador.items(), key=lambda x: x[1], reverse=True)
print("\nDiez idiomas más usados:")
for idioma, frecuencia in idiomas_ordenados[:10]:
    print(idioma + ": " + str(frecuencia) + " países")

paises_ordenados_por_poblacion = sorted(data.countries, key=lambda x: x['population'], reverse=True)
print("\nDiez países con mayor población:")
for pais in paises_ordenados_por_poblacion[:10]:
    print(pais['name'] + ": " + str(pais['population']))
