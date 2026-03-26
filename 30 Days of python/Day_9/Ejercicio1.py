"""
EJERCICIOS NIVEL 1 
"""


#-------------------------------------------------------------------------------
edad = input ("¿Cuál es tu edad? ")
edad = int(edad)
if edad >= 18:
    print ("Ya tienes edad para conducir")
else:
    print ("Aún no tienes edad para conducir te faltan ", (18 - int(edad)) ," años")
#-------------------------------------------------------------------------------
my_age = input ("Mi edad es: ")
my_age = int(my_age)
your_age = input ("Tu edad es: ")
your_age = int(your_age)
if my_age > your_age:
    if (my_age - your_age)==1:
        print ("Soy mayor que tú por un año")
    else:
        print ("Soy mayor que tú por ", (my_age - your_age), " años")
elif my_age < your_age:
    if (your_age - my_age)==1:
        print ("Eres mayor que yo por un año")
    else:
        print ("Eres mayor que yo por ", (your_age - my_age), " años")
else:
    print ("Tenemos la misma edad")
