#Dia 2 30 days of python 
#Ejercicio 1 Simple 
nombre = 'Elias'
apellido = "Caballero"
nombre_completo = nombre + ' ' + apellido
print(nombre_completo)
pais = 'Argentina'
ciudad = 'Buenos Aires'
print('Yo vivo en ' + ciudad + ', ' + pais)
edad = 23
año = 2026
is_married = False 
ingeniero = True
amigos = ['Santiago', 'Federico', 'Matias']
print(amigos)
#Ejercicio 2 
#Verificar tipo de dato usando type()
print(type(nombre))
print(type(apellido))
print(type(nombre_completo))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(año))
print(type(is_married))
print(type(ingeniero))
print(type(amigos))
print("La longitud del nombre completo es: ", len(nombre))
print("La longitud del apellido es: ", len(apellido))
print("La longitud del nombre es : ", len(nombre), "y la longitud del apellido es: ", len(apellido), "por lo tanto la diferencia es de: ", len(nombre) - len(apellido))
num_one = 5
num_two = 4
multi = num_one * num_two
suma = num_one + num_two
resta = num_one - num_two
division = num_one / num_two
div_modulo = num_one % num_two
expo = num_one ** num_two
div_piso = num_one // num_two
#Ejercicio radio de circulo 
radio = 30
pi = 3.14
area_circulo = pi * radio ** 2
print("El area del circulo es: ", area_circulo)
#Calculo de la circunferemcia 
circunferencia = 2 * pi * radio
print("La circunferencia del circulo es: ", circunferencia)
#Nueva area con entrada de usuario 
radio_usuario = float(input("Ingrese el radio del circulo: "))
area_circulo_usuario = pi * radio_usuario ** 2
print("El area del circulo con radio ", radio_usuario, " es: ", area_circulo_usuario)
print("Usuario por favor ingrese los siguientes datos")
nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
edad_usuario = int(input("Ingrese su edad: "))
print("Hola ", nombre_usuario, " ", apellido_usuario, " tienes ", edad_usuario, " años")

