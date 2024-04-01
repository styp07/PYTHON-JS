class Pajaro:
    
    alas = True
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        pass
    
    def piar(self):
        print(f'Pio, mi color es {self.color}')
        
    def volar(self, metros):
        self.piar()
        print(f'{self.especie} ha volado {metros} metros')
        
    def pintar_naranja(self):
        self.color = 'naranja'
        print(f'Ahora el pajaro es {self.color}')
        
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        #cls.alas = False
        
    @staticmethod
    def mirar():
        print(f'El pajaro mira')
    
loro = Pajaro('Verde', 'loro')
guacamaya = Pajaro('Rojo', 'loro')

print(f'Mi pajaro es un/a {loro.especie} y es de color {loro.color}')
print(f'Mi pajaro es un/a {guacamaya.especie} y es de color {guacamaya.color}')

loro.volar(50)
loro.pintar_naranja()
loro.poner_huevos(3)
loro.mirar()