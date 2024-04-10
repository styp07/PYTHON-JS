import unittest
import mod

class ProbarCambiaTexto(unittest.TestCase):
    
    def test_mayuscula(self):
        palabra = 'Buen dia'
        resultado = mod.todo_mayuscula(palabra)
        self.assertEqual(resultado, 'BUEN DIA')
        
if __name__ == '__main__':
    unittest.main()
    