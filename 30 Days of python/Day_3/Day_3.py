#Ejercicios dia 3 
import numpy as np
edad = 23 
altura = 1.75
num_complejo = 1 + 2j 
#Calcular altura de triangulo = 0.5 . b . h 
b = input("Ingrese la base del triangulo: ")
h = input("Ingrese la altura del triangulo: ")
print("La altura del triangulo es: ", 0.5 * float(b) * float(h))
lado_a= input("Ingrese el lado a del triangulo: ")
lado_b= input("Ingrese el lado b del triangulo: ")
lado_c= input("Ingrese el lado c del triangulo: ")
perimetro = float(lado_a) + float(lado_b) + float(lado_c)
print("El perimetro del triangulo es: ", perimetro)
#Obtener area y perimetro de un rectangulo 
base = input("Ingrese la base del rectangulo: ")
altura = input("Ingrese la altura del rectangulo: ")
area = float(base) * float(altura)
perimetro = 2 * (float(base) + float(altura))
print("El area del rectangulo es: ", area)
print("El perimetro del rectangulo es: ", perimetro)
#Calcular radio de un circulo 
pi = 3.1416
radio = input("Ingrese el radio del circulo: ") 
area_circulo = pi * (float(radio) ** 2)
perimetro_circulo = 2 * pi * float(radio)
print("El area del circulo es: ", area_circulo)
print("El perimetro del circulo es: ", perimetro_circulo)
#Calcular  pendiente, interseccion x y la interseccion y de y=2x-2 
pendiente = 2
interseccion_y1 = -2
interseccion_x1 = -interseccion_y1 / pendiente
print("La pendiente de la recta es: ", pendiente)
print("La interseccion con el eje y es: ", interseccion_y1)
print("La interseccion con el eje x es: ", interseccion_x1)
#Encontrar pendiente y distancia euclidiana entre los puntos (2,2) y (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia_euclidiana = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("La pendiente entre los puntos es: ", pendiente)
print("La distancia euclidiana entre los puntos es: ", distancia_euclidiana)
#Comparacion de las dos pendientes calculadas 
if pendiente == 2:
    print("Las pendientes son iguales.")   
else:
    print("Las pendientes son diferentes.")
long_python = len("Python")
long_dragon = len("Dragon")
print("python es mas largo que dragon: ", long_python > long_dragon)
#Ver si en la palabra python o dragon esta la palabra 'on'
print("on esta en python: ", "on" in "Python")
print("on esta en dragon: ", "on" in "Dragon")
#Ver si jerga esta en la oracion 
print("Jerga esta presente en la oracion espero que este curso no este lleno de jerga: ", "Jerga" in "Espero que este curso no este lleno de jerga")
longitud_python = float(len("Python"))
slogitud_python = str(longitud_python)
#Comprobar si un numero es par 
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El numero es par.")
else:
    print("El numero es impar.")
diez = "10"
ndiez = 10
print("'10' es igual a 10: ", type(diez) == type(ndiez))
#Calculo de tarifa por semana 
horas_trabajadas = float(input("Ingrese las horas trabajadas por semana: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))
salario_semanal = horas_trabajadas * tarifa_por_hora
print("El salario semanal es: ", salario_semanal)
#Presentación de tabla de numeros 
tabla = np.array([
    [1, 1, 1, 1, 1],
    [2, 1, 2, 4, 8],
    [3, 1, 3, 9, 27],
    [4, 1, 4, 16, 64],
    [5, 1, 5, 25, 125]
]) 
print(tabla)
