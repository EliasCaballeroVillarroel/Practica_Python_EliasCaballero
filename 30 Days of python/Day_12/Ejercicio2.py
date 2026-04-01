"""
Ejercicio 2: Generador de colores Hexadecimal o RGB
"""
import random
def generate_colours(tipo):
    tipo = tipo.lower() # convierte el tipo de color a minúsculas para evitar problemas de mayúsculas/minúsculas
    if tipo == "hex":
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))
    elif tipo == "rgb":
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    else :
        return "Tipo de color no válido. Por favor, elija 'hex' o 'rgb'."
print (generate_colours(input("¿egbQué tipo de color desea generar? (hex/rgb): ")))