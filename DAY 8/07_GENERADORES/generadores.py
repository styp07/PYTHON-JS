'''
Modulo encargado de explicar los generadores
'''


def funcion():

    """
    Esta función devuelve 4
    """

    return 4


def generador():

    """
    Esta función devuelve 4?
    """

    for i in range(1,5):
        yield i


print(funcion())
print(generador())

g = generador()

print(next(g))

print(next(g))
print(next(g))
print(next(g))
