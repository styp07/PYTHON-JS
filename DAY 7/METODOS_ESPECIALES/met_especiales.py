class CD:
    
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones
        
    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'
    
    def __len__(self):
        return self.canciones
    
    # def __del__(self):
    #     print(f'Libro eliminado')
    
queen = CD('Queen', 'Bohemian', 23)

# queen.__str__()
# queen.__len__()