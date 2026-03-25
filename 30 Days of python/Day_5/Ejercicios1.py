"""
Agregue una empresa de TI a it_companies

Inserte una empresa de TI en el medio de la lista de empresas

Cambie uno de los nombres de it_companies a mayúsculas (¡IBM excluido!)

Únase a it_companies con una cadena '#; '

Compruebe si existe una determinada empresa en la lista it_companies.

Ordene la lista usando el método sort()

Invierta la lista en orden descendente utilizando el método reverse()

Elimina las primeras 3 empresas de la lista

Elimina las últimas 3 empresas de la lista

Elimine la empresa o empresas de TI intermedias de la lista

Eliminar la primera empresa de TI de la lista

Eliminar la empresa o empresas de TI intermedias de la lista

Eliminar la última empresa de TI de la lista

Eliminar todas las empresas de TI de la lista

Destruir la lista de empresas de TI

Únase a las siguientes listas:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
"""
lst=[]
lst=[12,14,19,22,25,28]
print(len(lst))
print(lst[0],lst[len(lst)//2],lst[-1])
mixed_data_types=['Elias', 23, 1.75, 'Pareja', 'Marcelo T de Alvear 563']
print(mixed_data_types)
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies)) 
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])
it_companies[0] = 'Meta'
print(it_companies)
it_companies.insert(len(it_companies)//2, 'Tesla')
print(it_companies)
it_companies[1] = it_companies[1].upper() #Cambiamos a mayusculas el segundo elemento de la lista
print(it_companies)
it_companies_str = '#; '.join(it_companies) #Uno la lista con el separador '#; '
print(it_companies_str)
print("Se encuentra 'Google' en la lista:", 'Google' in it_companies) #Compruebo si Google esta en la lista
it_companies.sort() #Ordeno la lista
print(it_companies)
it_companies.sort(reverse=True) #Ordeno la lista
print(it_companies)
del it_companies[0:3] #Elimino las primeras 3 empresas
print(it_companies)
del it_companies[-3:] #Elimino las ultimas 3 empresas
print(it_companies)
it_companies.clear() #Elimino todas las empresas
print(it_companies)
del it_companies #Destruyo la lista
#Unión de listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
lenguajes = ["Python" , "SQL"]
redux_index = full_stack.index("Redux") #Busco el indice de Redux
full_stack.insert(redux_index,lenguajes)
print(full_stack)
