import random as rd

name = input('Hola ¿Cómo te llamas?: ')

print(f'Un gusto {name}, vamos a jugar un juego, tienes que adivinar un número al azar. Tienes 8 intentos')

continuee = 'y'
while continuee != 'n':
    contador = 8
    number_random = rd.randint(1, 100)
    while contador > 0:
        numbre_user = int(input('Dime el número que creas que es, recuerda que es del 1 al 100: '))
        if (numbre_user < 1) or (numbre_user > 100):
            print('Ese número no esta en el rango correcto')
            contador -= 1
            print(f'Tu contador lamentablemente quedo en: {contador}')
        elif numbre_user < number_random:
            print(f'El número es mayor que {numbre_user}')
            contador -= 1
            print(f'Tu contador lamentablemente quedo en: {contador}')
        elif numbre_user > number_random:
            print(f'El número es menor que {numbre_user}')
            contador -= 1
            print(f'Tu contador lamentablemente quedo en: {contador}')
        else:
            print(f'Felicidades {name}!!!, encontraste el número correcto')
            break
    if contador < 1:
        print(f'El número correcto era el: {number_random}, al quedarte sin vidas perdiste')
    continuee = input('¿Deseas seguir jugando? y/n: ')

print('Gracias por jugar')
