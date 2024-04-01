file = open('DAY 6/write_file/prueba.txt', 'w')
file.write('hola')
file.close()

file = open('DAY 6/write_file/prueba1.txt', 'w')
file.writelines(['hola','adios'])
file.close()

file = open('DAY 6/write_file/prueba2.txt', 'a')
file.write('hola')
file.write('adios')
file.close()