import datetime 
now = datetime.datetime.now() 
print("Current date and time: ")
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current second:", now.second)

time_one = now.strftime("%m/%d/%Y, %H:%M:%S,%a")
# formato mm/dd/YY H:M:S
dia_de_hoy =  "3  April, 2025"
print ("Dia de hoy ", dia_de_hoy)
objeto_dia = datetime.datetime.strptime(dia_de_hoy, "%d %B, %Y") 
print("Objeto de la fecha:", objeto_dia)
dia_hoy = datetime.date(year=2026 , month=4, day=3)
año_nuevo = datetime.date(year=2027 , month=1, day=1)
print("Dias hasta año nuevo:", (año_nuevo - dia_hoy).days)

fecha_vieja = datetime.date (year=1970, month=1, day=1)
print("Dias desde fecha vieja:", (dia_hoy - fecha_vieja).days)
"""
Para qué puedes usar el módulo datetime? Por ejemplo:
Análisis de series temporales
Obtener timestamps para eventos en una aplicación
Añadir la fecha de publicación en un blog
"""