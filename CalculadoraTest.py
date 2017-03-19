from unittest import TestCase
from Calculadora import Calculadora
class CalculadoraTest(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().suma(self,""),0," Igual a cero ")
