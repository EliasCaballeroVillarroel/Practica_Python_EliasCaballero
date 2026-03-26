person = {
    'first_name': 'Elias',
    'last_name': 'Caballero',
    'age': 23,
    'country': 'Argentina',
    'is_married': True,
    'skills': ['Data_analitics', 'Cinephile', 'Design', 'Futbol', 'Python'],
    'address': {
        'street': 'Chacabuco ',
        'zipcode': '480'
    }
}
if 'skills' in person:
    print('Skills existe en el diccionario de la persona ')
    if 'Python' in person['skills']:
        print('Python existe en las habilidades de la persona ')
    else:
        print('Python no existe en las habilidades de la persona ')
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('Es desarrollador Frontend')
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print('Es desarrollador Backend')
    elif 'React' in person['skills'] and 'Node' in person['skills']:
        print('Es desarrollador Fullstack')
    else:
        print('No se puede determinar el titulo de la persona ')
else:
    print('Skills no existe en el diccionario de la persona ')
if person['is_married'] == True and 'Argentina' in person['country']:
    print('La persona se llama {} {} y es de {}'.format(person['first_name'], person['last_name'], person['country']))
