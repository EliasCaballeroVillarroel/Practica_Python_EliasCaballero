""""
¿Qué es una expresión regular?
¿Qué es una variable de expresión regular (regex variable)?
Recrea patrones que: 
a) Encuentren citas que contengan la palabra talent en un libro, 
b) Encuentren fechas en formato DD-MM-YYYY, por ejemplo 12-01-2021,
c) Encuentren verbos en tiempo -ing en un texto.
"""
#Una expresión regular es una secuencia de caracteres que forma un patrón de búsqueda. 
#Se utiliza para buscar y manipular cadenas de texto basándose en patrones específicos.

#Se define como varible de expresion regular a una variable que contiene un patrón de búsqueda en forma de expresión regular.
import re
#a) Encuentren citas que contengan la palabra talent en un libro
text = "El talento es algo que se tiene o no se tiene."
pattern = r'\b\w*talent\w*\b' #Acá w y b son caracteres especiales de expresiones regulares. \b indica un límite de palabra, y \w* indica que puede haber cero o más caracteres alfanuméricos antes o después de la palabra "talent".
matches = re.findall(pattern, text)
print(matches)

#b) Encuentren fechas en formato DD-MM-YYYY, por ejemplo 12-01-2021
text = "La fecha de hoy es 12-01-2021 y la fecha de mañana es 13-01-2021."
patron = r'\b\d{2}-\d{2}-\d{4}\b' #Acá \d indica un dígito, {2} indica que debe haber exactamente dos dígitos, y {4} indica que debe haber exactamente cuatro dígitos.
matches = re.findall(patron, text)
print(matches)

#c) Encuentren verbos en tiempo -ing en un texto
text = "El corriendo y el saltando son actividades físicas."
busqueda = r'\b\w*ing\b' #Acá \w* indica que puede haber cero o más caracteres alfanuméricos antes de "ing", y \b indica un límite de palabra.
matches = re.findall(busqueda, text)
print(matches)