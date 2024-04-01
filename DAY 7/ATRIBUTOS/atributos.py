class Pajaro:
    
    alas = True
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        pass
    
loro = Pajaro('Verde', 'loro')
guacamaya = Pajaro('Rojo', 'loro')

print(f'Mi pajaro es un/a {loro.especie} y es de color {loro.color}')
print(f'Mi pajaro es un/a {guacamaya.especie} y es de color {guacamaya.color}')