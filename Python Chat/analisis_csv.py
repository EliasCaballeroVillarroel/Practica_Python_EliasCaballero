import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("marcha.csv")

print(df) #Muestra el archivo csv completo 

print("\nPromedio asimetria:", df["asimetria"].mean())

print("\nPacientes con asimetria mayor a 11:")
print(df[df["asimetria"] > 11]) #Busca el DF y la columna asimetria en este
#Recordar que asimetria es una columna en el csv

print("\nPaciente con mayor asimetria:")
print(df.loc[df["asimetria"].idxmax()])

print("\nPromedio de edad:", df["edad"].mean())

print("\nVer el paciente 3:")
print(df.loc[2])  # Los índices de pandas comienzan desde 0

print("\nOrdenados por asimetria:")
print(df.sort_values("asimetria", ascending=False))

df["riesgo"] = df["asimetria"] > 11

print("\nDataframe con columna riesgo:")
print(df)

print("\nCantidad pacientes en riesgo:")
print(df["riesgo"].sum())

df["nivel"] = df["asimetria"].apply(lambda x: "Alto" if x > 11 else "Bajo")
print(df)
df["grupo_edad"]=df["edad"].apply(lambda x: "Anciano" if x > 68 else "Adulto")
df=df.drop(columns=["riesgo"])
print("\nDataframe sin columna nivel:")
print(df)
df_promedio=df.groupby("grupo_edad")["asimetria"].mean()
print("\nPromedio asimetria por grupo de edad:")
print(df_promedio) #Agrupa por grupo de edad y luego calcula el promedio de asimetria para cada grupo

print("\nCuantos pacientes hay por nivel de asimetria:")
print(df.groupby('nivel').size()) #Agrupa por nivel y luego cuenta el número de pacientes en cada nivel

'''
df_promedio.plot(kind="bar")

plt.title("Asimetria promedio por grupo de edad")
plt.ylabel("Asimetria")
plt.show()
'''
#df.plot(x="edad", y="asimetria", kind="scatter")
#plt.title("Asimetria vs Edad")
#plt.xlabel("Edad del paciente")
#plt.ylabel("Asimetria")
#plt.show()

print("\nResumen estadistico:")
print(df["asimetria"].describe())

df["asimetria"].plot(kind="box")
plt.show()
