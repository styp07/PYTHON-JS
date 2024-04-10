def suma():
    a = int(input())
    b = int(input())
    print(a+b)
    
try:
    suma()
except:
    print('Algo salio mal')
else:
    print('Hiciste todo bien')
finally:
    print('Eso fue todo')