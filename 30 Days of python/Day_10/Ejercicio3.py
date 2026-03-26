from Data.countries_data import countries

# =========================================
# 1) ¿Cuántos idiomas distintos hay?
# =========================================
idiomas_distintos = []

for pais in countries:
    for idioma in pais["languages"]:
        if idioma not in idiomas_distintos:
            idiomas_distintos.append(idioma)

print("1) Cantidad de idiomas distintos:", len(idiomas_distintos))


# =========================================
# 2) ¿Cuál es el idioma usado por más países?
# =========================================
conteo_idiomas = {}

for pais in countries:
    for idioma in pais["languages"]:
        if idioma in conteo_idiomas:
            conteo_idiomas[idioma] += 1
        else:
            conteo_idiomas[idioma] = 1

idioma_mas_usado = ""
max_paises = 0

for idioma in conteo_idiomas:
    if conteo_idiomas[idioma] > max_paises:
        max_paises = conteo_idiomas[idioma]
        idioma_mas_usado = idioma

print("2) Idioma usado por más países:", idioma_mas_usado)
print("   Cantidad de países:", max_paises)


# =========================================
# 3) Diez países con mayor población
# =========================================
copia_paises = countries[:]   # copiamos la lista para no modificar la original
top_10 = []

while len(top_10) < 10:
    pais_mayor = copia_paises[0]

    for pais in copia_paises:
        if pais["population"] > pais_mayor["population"]:
            pais_mayor = pais

    top_10.append(pais_mayor)
    copia_paises.remove(pais_mayor)

print("3) Top 10 países con mayor población:")
puesto = 1
for pais in top_10:
    print(puesto, "-", pais["name"], ":", pais["population"])
    puesto += 1