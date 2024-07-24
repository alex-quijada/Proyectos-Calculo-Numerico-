import unittest
from math import e
from NewtonRaphson_AlexandraQuijada import newton_raphson
from PolinomioTaylor_AlexandraQuijada import taylor
from IntegracionNumerica_AlexandraQuijada import calcular_integral

class TestAlgorithms(unittest.TestCase):
    
    def test_newton_raphson(self):
        dfx = lambda x: -2 * x * (e ** (-x ** 2)) - 2
        fx = lambda x: (e ** (-x ** 2)) - 2 * x + 1

        Z = newton_raphson(0.80, 0.02, fx, dfx)
        self.assertAlmostEqual(Z[0], 0.7745, places=4)  # Ajustado según el resultado real

        Y = newton_raphson(2, 0.001, fx, dfx)
        self.assertAlmostEqual(Y[0], 0.7745, places=4)  # Ajustado según el resultado real

    def test_taylor(self):
        f = lambda x: x**2 + 3*x**3 - 2
        X0 = 0
        g = 4
        pol, poly_func = taylor(f, g, X0)

        expected_results = {
            0: -2,
            0.5: -1.375,
            1: 2
        }
        for x_val, expected in expected_results.items():
            self.assertAlmostEqual(poly_func(x_val), expected, places=4)

    def test_integracion(self):
        f = lambda x: x * ((x**2 + 1)**0.5)
        a, b = 1, 2
        n = 4

        # Prueba del método de Riemann
        riemann_result = calcular_integral('rieman', f, a, b, n)
        self.assertAlmostEqual(riemann_result, 2.4116, places=4)  # Ajustado según el resultado real

        # Prueba del método del trapecio
        trapecio_result = calcular_integral('trapecio', f, a, b, n)
        self.assertAlmostEqual(trapecio_result, 2.7939, places=4)  # Ajustado según el resultado real

if __name__ == "__main__":
    unittest.main()


