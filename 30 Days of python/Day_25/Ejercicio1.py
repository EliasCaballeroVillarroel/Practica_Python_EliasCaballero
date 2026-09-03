import pandas as pd 
import numpy as np 
#Creacion de serie de pandas 
"""numeros = [1,2,3,4,5]
frutas = ['manzana', 'banana', 'cereza', 'durazno', 'kiwi']
serie_frutas = pd.Series(frutas, index=numeros)
print(serie_frutas) # 1 manzana 2 banana 3 cereza 4 durazno 5 kiwi dtype: object
"""
"""#Crear a traves de un diccionario
dct= {"Nombre": "Elias", "Apellido" : "Caballero Villarroel" , "Edad": 23, "Pais": "Argentina"}
s= pd.Series(dct)
print(s) # Nombre Elias Apellido Caballero Villarroel Edad 23 Pais Argentina dtype
#Para hacer una serie constante hago de la siguiente forma 
s = pd.Series(10, index=[0,1,2,3,4])
print(s) # 0 10 1 10 2 10 3

#Crear una usand linspace 
s= pd.Series(np.linspace(1,25,10))
print(s)
#Como crear un data frame o tabla 
data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df= pd.DataFrame(data, columns=["Nombre", "Pais", "Ciudad"])
print(df)

#Crear dataframe de diccionario 
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

#Crear data frame de una lista de diccionarios 
data = [
    {'Nombre': 'Asabeneh', 'Pais': 'Finland', 'Ciudad': 'Helsinki'},
    {'Nombre': 'David', 'Pais': 'UK', 'Ciudad': 'London'},
    {'Nombre': 'John', 'Pais': 'Sweden', 'Ciudad': 'Stockholm'}]
df = pd.DataFrame(data,columns= ["Nombre", "Pais", "Ciudad"])
print(df)"""
"""
#Como leer CSV 
df = pd.read_csv('weight-height.csv')
#print(df)

#Leer las primeras 5 filas 
print(df.head(5))
#Leer las ultimas 5 filas
print(df.tail(5))
#Saber el tamaño, cantidad de columnas y filas
print(df.shape)

print(df.columns) #Muestra las columnas del data frame
#Si tomo una columna especifica convierto el DF en una Serie 
heights = df["Height"]
print(heights)

#Si pongo describe me da un analisis estadistico veloz de la columna
print(heights.describe())

"""

#Crear un data frame y unirlo con otro 

data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)

weights = [74, 78, 69]
df['Weight'] = weights
print(df)


heights = [173, 175, 169]
df['Height'] = heights
print(df)

df['Height'] = df['Height'] * 0.01
print(df)

