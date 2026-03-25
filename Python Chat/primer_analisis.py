import pandas as pd

datos = [12, 15, 18, 200, 20, 19]

df = pd.DataFrame(datos, columns=["asimetria"]) 

print("Promedio:", df["asimetria"].mean())
print("Máximo:", df["asimetria"].max()) 
#df es el DataFrame que contiene los datos, y "asimetria" es el nombre de la columna que contiene los valores.
#Un dataframe es una estructura de datos bidimensional que se utiliza para almacenar y manipular datos en forma de tabla, con filas y columnas. En este caso, el DataFrame se ha creado a partir de una lista de datos y se le ha dado el nombre de columna "asimetria".
# mean es una funcion de pandas que calcula el promedio de los valores en la columna "asimetria".
# max es una funcion de pandas que calcula el valor máximo de los valores en la columna "asimetria".
   