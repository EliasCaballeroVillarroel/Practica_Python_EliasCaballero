"""
Ejercicio 2
"""
def evens_and_odds(num):
    count=0
    for i in range(num + 1):
        if i % 2 == 0:
            
            count += 1
    print(f"Number of evens: {count}")
    print(f"Number of odds: {num + 1 - count}")

evens_and_odds(100)

def is_empty (param): #Llama a a la función is_empty con un argumento y devuelve True si el argumento está vacío, de lo contrario devuelve False.
    if param: #El argumento es considerado vacío si es None, False, 0, 0.0, '', [], {}, set(), etc. Si el argumento no es vacío, se evalúa como True.
        return False
    else:
        return True