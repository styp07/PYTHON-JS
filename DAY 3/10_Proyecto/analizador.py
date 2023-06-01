texto = input('Hola escribre una frase para analizarla: ').lower()
letras = [input('Escribe una letra: ').lower(), input('Escribre una segunda letra: ').lower(),
          input('Escribre una tercer letra: ').lower()]

lista_texto = texto.split()

letra_repetida_a = texto.count(letras[0])
letra_repetida_b = texto.count(letras[1])
letra_repetida_c = texto.count(letras[2])

letra_inicio = texto[0]
letra_fin = texto[-1]

lista_texto.reverse()
texto_reversa = ' '.join(lista_texto)

respuesta = 'python' in texto

print(f'''
Tu texto contiene:

- {letra_repetida_a} veces repetida la letra {letras[0]}
- {letra_repetida_b} veces repetida la letra {letras[1]}
- {letra_repetida_c} veces repetida la letra {letras[2]}

- Hay {len(lista_texto)} palabras en el texto

- la primer letra de tu texto es: {letra_inicio}
- La ultima letra de tu texto es: {letra_fin}

- El texto en reversa es:
    {texto_reversa}
    
- ¿Aparece la palabra python?
    {respuesta}

''')

