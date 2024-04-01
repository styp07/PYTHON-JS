def abrir_leer(directory):
    file = open(directory)
    return file.read()

def sobrescribir(directory):
    file = open(directory, 'w')
    file.write("contenido eliminado")
    
    file.close()
    
    file = open(directory, 'r')
    return file.read()

def registro_error(directory):
    file = open(directory, 'a')
    file.write("se ha registrado un error de ejecución")
    
    file.close()
    
    file = open(directory, 'r')
    return file.read()