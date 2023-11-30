def ceros(*args):
    
    cont = 0
    
    for n in args:
        
        if cont + 1 == len(args):
            return False
        elif args[cont] == 0 and args[cont+1] == 0:
            return True
        else:
            cont +=1
            
    return False

print(ceros(0,2,0,15,15,3,65,5))