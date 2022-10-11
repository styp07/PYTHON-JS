nombre = input('¿Cúal es tu nombre?: ')
valor_venta = float(input('¿Cuantas ventas realizaste?: '))
comision_venta = round(valor_venta*0.13, 2)

print(f'Hola {nombre}, ganaste {comision_venta} por la comisión de tus ventas')