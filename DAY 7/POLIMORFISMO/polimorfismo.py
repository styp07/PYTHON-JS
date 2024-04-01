class Vaca():
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(f'{self.nombre} dice muu')
        
class Oveja():
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    def hablar(self):
        print(f'{self.nombre} dice bee')
        
def animal_habla(animal):
    animal.hablar()
        
vaca = Vaca('Vaca')
oveja = Oveja('Oveja')

# animales = [vaca, oveja]

# for animal in animales:
#     animal.hablar()

animal_habla(vaca)
animal_habla(oveja)