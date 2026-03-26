"""
EJERCICIOS NIVEL 1 
"""
contador = 0
while contador <= 10:
    print(contador)
    contador += 1
for i in range(11):
    print(i)

#---------------------------------------------------------------  
    

    contador = 0
while contador <= 7:
    contador += 1 
    for i in range(contador):
        print("#", end="")
    print()  # Print a newline after each row   

#---------------------------------------------------------------  
    
contador = 0

while contador <= 8:
    print("########")
    contador += 1

#---------------------------------------------------------------  

contador = 0 
while contador <= 10:
    print(contador , "x" , contador , "=" , contador * contador)
    contador += 1

#---------------------------------------------------------------

lista = ['Python', 'Numpy','Pandas','Django', 'Flask']

for i in lista:
    print(i)

#---------------------------------------------------------------

for i in range(100):
    if i % 2 == 0:
        print(i)
    else:
        continue

for i in range(100):
    if i % 2 != 0:
        print(i)
    else:
        continue






