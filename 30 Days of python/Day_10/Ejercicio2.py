#Ejercicios nivel 2 
contador_par = 0
contador_impar = 0
for i in range(101):
    if i % 2 == 0:
        contador_par += i
    else :
        contador_impar += i 
print("Números pares:", contador_par)
print("Números impares:", contador_impar)