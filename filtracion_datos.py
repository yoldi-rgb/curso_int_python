
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Hector',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
def run():
    #all_python_devs =[worker["name"] for worker in DATA if worker["language"] == "python"]
    #all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"]== "Platzi" ]
    
    #Crear las listas all... usando combinacion de filter y map ##############
    
    all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    names_devs = list(map(lambda worker: worker['name'], all_python_devs))
    all_Platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi',DATA))
    name_workers_p = list(map(lambda worker: worker['name'],all_Platzi_workers))

    #adults = list(filter(lambda worker: worker ["age"]> 18, DATA))
    #adults = list(map(lambda worker:worker["name"], adults))
    old_people = list(map(lambda worker: worker | {"old" : worker["age"] > 70},DATA))

    #Crear la lista old y adult con list comprehesion ###############
    adults = [worker['name'] for worker in DATA if worker['age']> 18]
    #old_people = [worker['name'] for  worker in DATA if  worker | {"old" : worker["age " > 70 ]} ]  revision de la linea de codigo
    for worker in old_people:
       print(worker)

    #Crear las listas all... usando combinacion de filter y map
    #Crear la lista old y adult con list comprehesion
    #for worker in name_workers_p:
    #   print(worker)












if __name__ == '__main__':
    run()