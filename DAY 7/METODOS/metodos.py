class Pajaro:
    
    alas = True
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        pass
    
    def piar(self):
        print(f'Pio, mi color es {self.color}')
        
    def volar(self, metros):
        print(f'{self.especie} ha volado {metros} metros')
    
loro = Pajaro('Verde', 'loro')
guacamaya = Pajaro('Rojo', 'loro')

print(f'Mi pajaro es un/a {loro.especie} y es de color {loro.color}')
print(f'Mi pajaro es un/a {guacamaya.especie} y es de color {guacamaya.color}')

loro.piar()
loro.volar(50)