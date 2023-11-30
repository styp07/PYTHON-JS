def chequear_3_cifras(list):
    
    list_3_cifras = []
    
    for n in list:
        if n in range(100, 1000):
            list_3_cifras.append(n)
        else:
            pass
        
    return list_3_cifras
        
lista = [50, 60, 120]
result = chequear_3_cifras(lista)

print(result)