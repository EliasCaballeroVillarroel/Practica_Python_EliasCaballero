"""
Ejercicio 1: Generador de contraseñas aleatorias y de colores RGB
"""
import random
import string 
def generate_random_paswords (cantidad, largo):
    passwords = []
    for i in range(cantidad):
        characters = string.ascii_letters + string.digits + string.punctuation #Ascii_letters: letras mayusculas y minusculas, digits: numeros, punctuation: simbolos
        password = ''.join(random.choices(characters, k=largo)) # se usa '' para unir los caracteres generados en una sola cadena, random.choice() se utiliza para seleccionar un caracter aleatorio de la variable characters, y el bucle for se ejecuta 12 veces para generar una contraseña de 12 caracteres.
        passwords.append(password)
    return passwords

for i in range(5):
    print("Opcion " + str(i + 1) + ": " + generate_random_paswords(5, 12)[i])

def generate_random_rgb_color():
    r = random.randint(0, 255) # genera un número aleatorio entre 0 y 255 para el componente rojo
    g = random.randint(0, 255) # genera un número aleatorio entre 0 y 255 para el componente verde
    b = random.randint(0, 255) # genera un número aleatorio entre 0 y 255 para el componente azul
    return (r, g, b) # devuelve una tupla con los valores RGB generados
for i in range(5):
    print("Opcion " + str(i + 1) + ": " + str(generate_random_rgb_color()))

