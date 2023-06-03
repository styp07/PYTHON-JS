name = ['Ana', 'Hugo', 'Carolos']
age = [65, 20, 30]
city = ['Lima', 'Madrid', 'Bogotá']

combined = list(zip(name, age, city))

print(combined)

for name, age, city in combined:
    print(f'{name} tiene {age} años y vive en {city}')


spanish = ['uno', 'dos', 'tres']
portuguese = ['um', 'dois', 'três']
english = ['one', 'two', 'three']

zipp = list(zip(spanish, portuguese, english))

for spanish, portuguese, english in zipp:
    print(zipp)
