caracter = ',:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#'

print(caracter.lstrip(',:#,:_'))

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

frutas.insert(5, 'naranja')

print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)
print(conjuntos_aislados)

