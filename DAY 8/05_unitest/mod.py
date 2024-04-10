'''
Este módulo contiene una sencilla función de suma,
y ejecuta un ejemplo mostrando el resultado en pantalla
'''


def todo_mayuscula(texto):

    """
    Esta función recibe un texto
    y lo vuelve en mayuscula
    """

    return texto.upper()


TEXTO = todo_mayuscula('Hola')


print(TEXTO)
