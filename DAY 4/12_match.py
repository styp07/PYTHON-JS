serie = 'N-02'

match serie:
    case 'N-00':
        print('Samsung')
    case 'N-01':
        print('Nokia')
    case 'N-02':
        print('Motorola')
    case 'N-03':
        print('Apple')
    case _:
        print(f'No existe el producto con la serie: {serie}')

client = {'name': 'Federico',
          'edad': 45,
          'ocupacion': 'Instructor'}

movie = {'titulo': 'Avengers',
         'ficha_tecnica': {'protagonista': 'IronMan', 'director': 'Marvel'}}

element = [client, movie, 'libro']

for i in element:
    match i:
        case {'name': name,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('Es un cliente')
            print(name, edad, ocupacion)

        case {'titulo': titulo,
              'ficha_tecnica':{'protagonista': protagonissta,
                               'director': director}}:
            print('Esto es una pelicula')
            print(titulo,protagonissta,director)
        case _:
            print('¿Que es esto?')
