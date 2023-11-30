from random import shuffle, choice

# lista inicial

palitos = ['-','--','---','----']

# funcion encargada de mezclar

def mezclar(list):
    shuffle(list)
    return list

# función encargada de pedir intento

def probar_suerte():
    intent = ''
    
    while intent not in ('1','2','3','4'):
        intent = input(f'Elige un número del 1 al 4: ')
        
    return int(intent)

# funcion de comprobar el intento

def comprobar_intento(list, intento):
    choice(list)
    if list[intento - 1] == choice(list):
        print(f'Ganaste')
    else:
        print(f'Perdiste')
        
    print(f'la linea era: {list[intento - 1]}')

palistos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
comprobar_intento(palistos_mezclados, seleccion)