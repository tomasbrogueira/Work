#! /usr/bin/env python3
''' tests for ex16.py '''
import unittest
SKIP = False
try :
    import ex16
except ImportError:
    SKIP = True
class TestEx16(unittest.TestCase):
    ''' test class for ex16.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex16.py")
        self.unit = ex16
    def test_ordenada(self):
        ''' Test sequence for '.ordenada()' '''
        vec = self.unit.Vetor(21, 12)
        self.assertEqual(12, vec.ordenada())
    def test_abcissa(self):
        ''' Test sequence for '.abcissa()' '''
        vec = self.unit.Vetor(21, 12)
        self.assertEqual(21, vec.abcissa())
    def test_nulo(self):
        ''' Test sequence for '.nulo()' '''
        vec = self.unit.Vetor(0, 0)
        self.assertTrue(vec.nulo())
    def test_nao_nulo(self):
        ''' Test sequence for 'not .nulo()' '''
        vec = self.unit.Vetor(21, 12)
        self.assertFalse(vec.nulo())
    def test_iguais(self):
        ''' Test sequence for '.iguais()' '''
        vec = self.unit.Vetor(21, 12)
        self.assertTrue(vec.iguais(self.unit.Vetor(21, 12)))
    def test_diferentes(self):
        ''' Test sequence for 'not .iguais()' '''
        vec = self.unit.Vetor(21, 12)
        self.assertFalse(vec.iguais(self.unit.Vetor(12, 21)))
    def test_produto(self):
        ''' Test sequence for '.produto_escalar()' '''
        vec = self.unit.Vetor(21, 12)
        self.assertEqual(1386, vec.produto_escalar(self.unit.Vetor(34, 56)))

if __name__ == '__main__':
    unittest.main()
