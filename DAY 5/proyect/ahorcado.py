from random import choice

palabras = ['arroz', 'papa', 'castillo', 'dinosaurio']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminadox = False

def elegir_palabra(lista_palabra):
    palabra_elegida = choice(lista_palabra)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

def pedir_letra():
    l_elegida = ''
    validacion = False
    abc = 'abcdefghijklmnñopqrstuvwxyz'
    
    while not validacion:
        l_elegida = input(f'Elige una letra: ').lower()
        if l_elegida in abc and len(l_elegida) == 1:
            validacion = True
        else:
            print(f'{l_elegida} No es una opción valida, elige nuevamente')
            
    return l_elegida

def mostrar_palabra_oculta(palabra_elegida):
    
    list_ocult = []
    
    for l in palabra_elegida:
        if l in letras_correctas:
            list_ocult.append(l)
        else:
            list_ocult.append('-')
            
    print(' '.join(list_ocult))
    
def chequear_letra(letra_elegida, palabra_elegida, vidas, coincidencias):
    
    fin = False
    
    if letra_elegida in palabra_elegida and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_elegida and letra_elegida in letras_correctas:
        print('Ya has encontrado la letra')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
        
    if vidas == 0:
        fin = perder(palabra_elegida)
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_elegida)
        
    return vidas, fin, coincidencias

    
def ganar(palabra_elegida):
    mostrar_palabra_oculta(palabra_elegida)
    print(f'Ganaste!!! la palabra era {palabra_elegida}')
    return True
    
def perder(palabra_elegida):
    print(f'Perdiste, la palabra era {palabra_elegida}')
    return True

palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminadox:
    print(f'\n  {"*"*20} \n')
    mostrar_palabra_oculta(palabra)
    print('\n')
    print(f'Letras incorrectas {"-".join(letras_incorrectas)}')
    print(f'Vidas: {intentos}')
    print(f'\n  {"*"*20} \n')
    
    letra = pedir_letra()
    
    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
    
    juego_terminadox  = terminado