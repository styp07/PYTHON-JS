'''
Este módulo nos explica los decoradores
'''


def decorar_saludo(funcion):

    """
    Esta función recibe funciones
    """

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')

    return otra_funcion


@decorar_saludo
def mayusculas(texto):

    """
    Funcion encargada de volver texto en mayusculas
    """

    print(texto.upper())


@decorar_saludo
def minuscula(texto):

    """
    Funcion encargada de volver texto en minusculas
    """

    print(texto.lower())


mayusculas('Cr')
minuscula('Cr')
