# class Animal:

#     def __init__(self, edad, color):
#         self.edad = edad
#         self.color = color 

#     def nacer(self):
#         print('Este animal ha nacido')
    
#     pass

# class Pajaro(Animal):
    
#     def __init__(self, edad, color, altura_vuelo):
#         super().__init__(edad, color)
#         self.altura_vuelo = altura_vuelo
    
#     pass


class Padre:
    
    def hablar(self):
        print('Hola')
        
class Madre:
    def reir(self):
        print('Ja Ja Ja')
        
    def hablar(self):
        print('Que tal?')
    
class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

nieto = Nieto()

nieto.reir()