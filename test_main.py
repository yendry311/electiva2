# test_main.py
import unittest
from main import sumar

class TestSuma(unittest.TestCase):
    def test_suma_positiva(self):
        self.assertEqual(sumar(2, 3), 5)

    def test_suma_negativa(self):
        self.assertEqual(sumar(-1, 1), 0)

    def test_suma_cero(self):
        self.assertEqual(sumar(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
