import unittest
import sys
sys.path.insert(0, "PruebaFib")

import fibonacci

class pruebaFibonacci(unittest.TestCase):
    def SerieFibonacci_imp(self):
        """ Prueba con n impar """
        data = 5
        result = fib(data)
        self.assertEqual(result,5, "Incorrecta serie de fibonacci con n impar")

    def SerieFibonacci_par(self):
        """ Prueba con n par """
        data = 8
        result = fib(data)
        self.assertEqual(result,21, "Incorrecta serie de fibonacci con n par")
  
if __name__ == '__main__':
    unittest.main()

