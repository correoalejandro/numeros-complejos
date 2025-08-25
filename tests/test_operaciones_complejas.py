import math
import unittest
from numeros_complejos.operaciones_complejas import (
    suma, resta, producto, division, modulo, conjugado,
    fase, cartesiano_a_polar, polar_a_cartesiano
)

TOL = 1e-9

class TestComplejos(unittest.TestCase):
    # ---- suma ----
    
    def test_suma_basica(self):
        self.assertEqual(suma((1,2), (3,4)), (4,6))
    
    def test_suma_con_negativos(self):
        self.assertEqual(suma((-1,5), (1,-2)), (0,3))

    # ---- resta ----
    
    def test_resta_basica(self):
        self.assertEqual(resta((5,7), (2,3)), (3,4))
    
    def test_resta_con_negativos(self):
        self.assertEqual(resta((-2,1), (1,-3)), (-3,4))

    # ---- producto ----
    
    def test_producto_basico(self):
        self.assertEqual(producto((1,2), (3,4)), ( -5, 10 ))
    
    def test_producto_por_conjugado(self):
        z = (2,-3)
        self.assertEqual(producto(z, conjugado(z)), (13, 0))

    # ---- division ----
    
    def test_division_basica(self):
        a = division((1,2), (3,4))
        
        self.assertAlmostEqual(a[0], 0.44, places=2)
        self.assertAlmostEqual(a[1], 0.08, places=2)
        
    def test_division_por_cero(self):
        with self.assertRaises(ZeroDivisionError):
            division((1,2), (0,0))

    def test_division_por_si_mismo(self):
        z = (3, 4)
        a = division(z, z)
        self.assertAlmostEqual(a[0], 1.0, places=9)
        self.assertAlmostEqual(a[1], 0.0, places=9)

    def test_division_por_uno(self):
        z = (5, -7)
        a = division(z, (1, 0))
        self.assertEqual(a, z)

    # ---- modulo ----
    
    def test_modulo_basico(self):
        self.assertAlmostEqual(modulo((3,4)), 5.0, places=12)
    
    def test_modulo_numero_negativo_en_ambas_partes(self):
        self.assertAlmostEqual(modulo((-3, -4)), 5.0, places=12)
    
    
    # ---- conjugado ----
    
    def test_conjugado_basico(self):
        self.assertEqual(conjugado((5,-7)), (5,7))

    def test_conjugado_involucion(self):
        z = (1.2, -3.4)
        self.assertEqual(conjugado(conjugado(z)), z)

    # ---- fase ----
    def test_fase_cuadrante_I(self):
        self.assertAlmostEqual(fase((1,1)), math.pi/4, places=9)
    
    def test_fase_origen(self):
        self.assertEqual(fase((0,0)), 0.0)

    # ---- conversiones ----
    
    def test_cartesiano_a_polar_y_vuelta(self):
        # Número en forma cartesiana
        z = (3, 4)

        # Paso a forma polar
        p = cartesiano_a_polar(z)

        # El módulo debe ser 5
        self.assertAlmostEqual(p[0], 5.0, places=12)

        # El ángulo debe ser atan2(4,3)
        self.assertAlmostEqual(p[1], math.atan2(4, 3), places=12)

        # Paso de nuevo a forma cartesiana
        z = polar_a_cartesiano(p)

        # Debe volver a (3,4)
        self.assertAlmostEqual(z[0], 3.0, places=9)
        self.assertAlmostEqual(z[1], 4.0, places=9)

    def test_polar_a_cartesiano_normalizacion(self):
        # Si r es negativo, se corrige sumando π al ángulo
        z1 = polar_a_cartesiano((-2, 0.0))
        z2 = polar_a_cartesiano((2, math.pi))

        # Ambos resultados deben ser iguales
        self.assertAlmostEqual(z1[0], z2[0], delta=TOL)
        self.assertAlmostEqual(z1[1], z2[1], delta=TOL)
        
if __name__ == "__main__":
    unittest.main()
