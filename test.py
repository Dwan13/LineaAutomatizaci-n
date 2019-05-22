import listaDemultiplicacion

class pruebaMultiplicacion(unittest.TestCase):

    def listaDemultiplicacionEntero(self):
        """ Prueba con números enteros """
        data = [6, 9, 7, 2]
        result = _list(data)
        self.assertEqual(result,756, "Incorrecta multiplicacion de enteros")

    def listaDemultiplicacionFlotante(self):
        """ Prueba con números flotantes """
        data = [6.5, 9.3, 7.2, 2.5]
        result = listaDemultiplicacion(data)
        self.assertEqual(result,1088.1, "Incorrecta multiplicacion de flotantes")

    def listaDemultiplicacionNegativo(self):
        """ Prueba con números negativos """
        data = [-6, -9, -7, -2]
        result = listaDemultiplicacion(data)
        self.assertEqual(result, 756, "Incorrecta multiplicacion de negativos")
    
    def listaDemultiplicacionMixto(self):
        """ Prueba con números reales """
        data = [3.4, -5, 8]
        result = listaDemultiplicacion(data)
        self.assertEqual(result, -136, "Incorrecta multiplicacion")

if __name__ == '__main__':
    unittest.main()

