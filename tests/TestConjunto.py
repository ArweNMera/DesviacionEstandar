# tests/TestConjunto.py

import unittest
from src.logica.Conjunto import Conjunto


class TestConjunto(unittest.TestCase):

    # Pruebas para el promedio
    def test_conjunto_Vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento(self):
        conjunto = Conjunto([5])
        self.assertEqual(5, conjunto.promedio())

    def test_conjunto_dosElementos_retornaPromedioElementos(self):
        conjunto = Conjunto([5, 7])
        self.assertEqual(6, conjunto.promedio())

    def test_conjunto_nElementos_retornaPromedioNElementos(self):
        conjunto = Conjunto([2, 4, 8, 9, 10, 15])
        self.assertEqual((2 + 4 + 8 + 9 + 10 + 15) / 6, conjunto.promedio())

    # Pruebas para la desviación estándar
    def test_conjunto_Vacio_lanzaExcepcion(self):
        conjunto = Conjunto([])
        with self.assertRaises(ValueError):
            conjunto.desviacion_estandar()

    def test_conjunto_unElemento_retornaCero(self):
        conjunto = Conjunto([5])
        self.assertEqual(0, conjunto.desviacion_estandar())

    def test_conjunto_tresElementos_retornaDesviacionEstandar(self):
        conjunto = Conjunto([4, 6, 8])
        resultadoEsperado = 1.632993161855452  # Calculado manualmente
        self.assertAlmostEqual(resultadoEsperado, conjunto.desviacion_estandar(), places=6)

    def test_conjunto_numerosPositivosYNegativos_retornaDesviacionEstandar(self):
        conjunto = Conjunto([3.5, 8, -4.2])
        resultadoEsperado = 5.037415563119203
        self.assertAlmostEqual(resultadoEsperado, conjunto.desviacion_estandar(), places=6)

    def test_conjunto_ceros_retornaCero(self):
        conjunto = Conjunto([0, 0, 0, 0])
        self.assertEqual(0, conjunto.desviacion_estandar())

    def test_conjunto_conElementoNoNumerico_lanzaExcepcion(self):
        conjunto = Conjunto([5, "4.5"])
        with self.assertRaises(TypeError):
            conjunto.desviacion_estandar()


if __name__ == '__main__':
    unittest.main()
