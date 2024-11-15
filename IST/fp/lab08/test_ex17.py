#! /usr/bin/env python3
''' tests for ex17.py '''
import unittest
SKIP = False
try :
    import ex17
except ImportError:
    SKIP = True
class TestEx17(unittest.TestCase):
    ''' test class for ex17.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex17.py")
        self.unit = ex17
    def test_x(self):
        ''' Test sequence for '.valor_x()' '''
        vec = self.unit.Vetor3D(23, 34, 45)
        self.assertEqual(23, vec.valor_x())
    def test_y(self):
        ''' Test sequence for '.valor_y()' '''
        vec = self.unit.Vetor3D(23, 34, 45)
        self.assertEqual(34, vec.valor_y())
    def test_z(self):
        ''' Test sequence for '.valor_z()' '''
        vec = self.unit.Vetor3D(23, 34, 45)
        self.assertEqual(45, vec.valor_z())
    def test_nulo(self):
        ''' Test sequence for '.nulo()' '''
        vec = self.unit.Vetor3D(0, 0, 0)
        self.assertTrue(vec.nulo())
    def test_nao_nulo(self):
        ''' Test sequence for 'not .nulo()' '''
        vec = self.unit.Vetor3D(23, 34, 45)
        self.assertFalse(vec.nulo())
    def test_iguais(self):
        ''' Test sequence for '.iguais()' '''
        vec = self.unit.Vetor3D(23, 34, 45)
        vec2 = self.unit.Vetor3D(23, 34, 45)
        self.assertTrue(vec.iguais(vec2))
    def test_nao_iguais(self):
        ''' Test sequence for 'not .iguais()' '''
        vec = self.unit.Vetor3D(23, 34, 45)
        vec2 = self.unit.Vetor3D(32, 21, 10)
        self.assertFalse(vec.iguais(vec2))
    def test_norma(self):
        ''' Test sequence for '.norma()' '''
        vec = self.unit.Vetor3D(23, 34, 45)
        self.assertEqual(102, vec.norma())

if __name__ == '__main__':
    unittest.main()
