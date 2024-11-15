import unittest
from ex10 import horner

class TestHorner(unittest.TestCase):
    def test_horner_constant_polynomial(self):
        x = 0
        self.assertEqual(horner([4], x), 4)

    def test_horner_linear_polynomial(self):
        x = 1
        self.assertEqual(horner([3, 4], x), 3*x + 4)

    def test_horner_quadratic_polynomial(self):
        x = 2
        self.assertEqual(horner([2, 3, 4], x), 4*x**2 + 3*x + 2)

    def test_horner_cubic_polynomial(self):
        x = 3
        self.assertEqual(horner([1, 2, 3, 4], x), 4*x**3 + 3*x**2 + 2*x + 1)

    def test_horner_quartic_polynomial(self):
        x = 4
        self.assertEqual(horner([0, 1, 2, 3, 4], x), 4*x**4 + 3*x**3 + 2*x**2 + x)

    def test_horner_quintic_polynomial(self):
        x = 5
        self.assertEqual(horner([0, 0, 1, 2, 3, 4], x), 4*x**5 + 3*x**4 + 2*x**3 + x**2)

if __name__ == '__main__':
    unittest.main()