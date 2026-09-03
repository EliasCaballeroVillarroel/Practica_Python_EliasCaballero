"""
Ejercicio 2
Escribe un patrón que valide un nombre de variable válido en Python.
Limpia el siguiente texto eliminando etiquetas HTML.
"""
import re
#Un nombre de variable válido en Python debe comenzar con una letra (a-z, A-Z) o un guion bajo (_), seguido de letras, 
#dígitos (0-9) o guiones bajos. Además, no puede ser una palabra reservada de Python.
#Patrón para validar un nombre de variable válido en Python
pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
#Ejemplos de nombres de variables válidos
variable1 = "nombre_variable"
variable2 = "_variable2"
variable3 = "variable3"
#Ejemplos de nombres de variables no válidos
variable4 = "3variable"
variable5 = "variable-5"
#Validar los nombres de variables
print(re.match(pattern, variable1) is not None)  # True
print(re.match(pattern, variable2) is not None)  # True 
print(re.match(pattern, variable3) is not None)  # True
print(re.match(pattern, variable4) is not None)  # False
print(re.match(pattern, variable5) is not None)  # False
#Limpia el siguiente texto eliminando etiquetas HTML
text = '''
HTML
Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags, but use them to interpret the content of the page.

HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.
'''
clean_text = re.sub('HTML', '', text) #El patrón <.*?> coincide con cualquier etiqueta HTML, y re.sub reemplaza todas las coincidencias con una cadena vacía, eliminando así las etiquetas del texto.
print(clean_text)
