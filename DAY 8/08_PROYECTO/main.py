'''
Modulo principal
'''
import os
import numeradores as nm


def preguntar():

    """
    Función encargada de preguntar las opciones al usuario
    """

    while True:
        print('[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmeticos')
        try:
            mi_rublo = input('Elija una opción: ').upper()
            ['P', 'F', 'C'].index(mi_rublo)
        except ValueError:
            print('Esa no es una opción valida')
        else:
            break

    nm.decorador(mi_rublo)


def inicio():

    """
    Funcion encargada de dar inicio
    """

    os.system('cls')

    while True:
        preguntar()
        try:
            otro_turno = input('Quieres sacar otro turno? [S] [N]:').upper()
            ['S', 'N'].index(otro_turno)
        except ValueError:
            print('Esta no es una opción valida')
        else:
            if otro_turno == 'N':
                print('Gracias por su visita')
                break


inicio()
