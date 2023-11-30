def suma(num1, num2, *args, **kwargs):
    w = 0
    
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')
    
    for i in args:
        print(f'arg = {i}')    

        
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        w += valor
        
    return w
    
print(suma(2,3,200,65,15,15,15, x=2, y=3, z=5))