"""
EJERCICIOS NIVEL 2
"""
calificacion = input ("¿Cuál es tu calificación? ")
calificacion = int(calificacion)
if calificacion >= 80 and calificacion <= 100:
    print ("Tu calificación es A")
elif calificacion >= 70 and calificacion < 80:
    print ("Tu calificación es B")
elif calificacion >= 60 and calificacion < 70:  
    print ("Tu calificación es C")
elif calificacion >= 50 and calificacion < 60:
    print ("Tu calificación es D")
elif calificacion >= 0 and calificacion < 50:
    print ("Tu calificación es F")
else:
    print ("Calificación no válida")
#-------------------------------------------------------------------------------
mes = input ("¿Cuál es el mes? ")
mes = mes.lower() #Esto convierte el texto a minúscula para evitar problemas con mayúsculas
if mes == "enero" or mes == "febrero" or mes == "marzo":
    print ("El mes ", mes, " pertenece a la estación de invierno")
elif mes == "abril" or mes == "mayo" or mes == "junio":
    print ("El mes ", mes, " pertenece a la estación de primavera")
elif mes == "julio" or mes == "agosto" or mes == "septiembre":
    print ("El mes ", mes, " pertenece a la estación de verano")
elif mes == "octubre" or mes == "noviembre" or mes == "diciembre":
    print ("El mes ", mes, " pertenece a la estación de otoño")
else:
    print ("Mes no válido")
#-------------------------------------------------------------------------------
frutas = ['banana', 'naranja', 'mango', 'limon']
fruta = input ("¿Cuál es tu fruta favorita? ")
fruta = fruta.lower() #Esto convierte el texto a minúscula para evitar problemas con mayúsculas
if fruta in frutas:
    print ("Tu fruta favorita esta en la lista")
else:
    print ("Tu fruta favorita no estaba en la lista asi que la agregamos")
    frutas.append(fruta)
    print ("Lista de frutas actualizada: ", frutas)




