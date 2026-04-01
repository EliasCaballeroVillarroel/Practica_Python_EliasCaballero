"""
Ejercicio 1
"""
import math

def add_two_numbers(a, b):
    return a + b

def area_de_circulo(radio):
    return math.pi * radio ** 2

def add_all_nums(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError("Los argumentos deben ser números")
    return sum(args)

def convert_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def check_season(mes):
    if mes in ["diciembre", "enero", "febrero"]:
        return "Invierno"
    elif mes in ["marzo", "abril", "mayo"]:
        return "Primavera"
    elif mes in ["junio", "julio", "agosto"]:
        return "Verano"
    elif mes in ["septiembre", "octubre", "noviembre"]:
        return "Otoño"
    else:
        raise ValueError("Mes no válido")
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        raise ValueError("No se puede calcular la pendiente de una línea vertical")
    return (y2 - y1) / (x2 - x1)
def solve_quadratic(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        raise ValueError("La ecuación no tiene soluciones reales")
    raiz_discriminante = math.sqrt(discriminante)
    x1 = (-b + raiz_discriminante) / (2*a)
    x2 = (-b - raiz_discriminante) / (2*a)
    return x1, x2