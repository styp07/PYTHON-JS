'''
Modulo encargado de los númeradores
'''

def numeros_perfumeria():

    """
    Función encargada de de enumerar por perfumeria
    """

    for i in range(1, 100000):
        yield f'P - {i}'


def numeros_farmacia():

    """
    Función encargada de de enumerar por farmacia
    """

    for i in range(1, 100000):
        yield f'F - {i}'


def numeros_cosmeticos():

    """
    Función encargada de de enumerar por cosmetico
    """

    for i in range(1, 100000):
        yield f'C - {i}'


def decorador(rublo):

    """
    Decorador de los nímeradores
    """

    print(f'\n {"*" * 23}')
    print('Su número es: ')
    if rublo == 'P':
        print(next(p))
    elif rublo == 'F':
        print(next(f))
    else:
        print(next(c))
    print('Espere, ya sera atendido')
    print(f'\n {"*" * 23}')


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmeticos()
