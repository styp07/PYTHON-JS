precio_cafe = [('capuchino', 1.5), ('Expresso', 1.2), ('Moka', 1.9)]

for cafe, precio in precio_cafe:
    print(f'El precio de: {cafe} es de: ${precio}')
    
def cafe_mas_caro(list_precio):
    
    precio_mayor = 0
    cafe_mas_caro = ''
    
    for cafe, precio in list_precio:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
        
    return(cafe_mas_caro, precio_mayor)

cafe_caro, precio_caro = cafe_mas_caro(precio_cafe)

print(f'El cafe mas caro es {cafe_caro}, con un precio de ${precio_caro}')