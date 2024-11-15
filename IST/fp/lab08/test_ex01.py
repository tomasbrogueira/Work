#! /usr/bin/env python3
''' tests for ex01.py '''
import unittest
import sys
from io import StringIO
SKIP = False
try :
    import ex01
except ImportError:
    SKIP = True
class TestEx01(unittest.TestCase):
    ''' test class for ex01.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex01.py")
        self.unit = ex01
        self.stdout = sys.stdout
        sys.stdout = StringIO()
    def tearDown(self):
        sys.stdout = self.stdout
    def test_exemplo(self):
        ''' Test sequence for '50' '''
        park = self.unit.Estacionamento(50)
        self.assertEqual(50, park.lotacao_maxima())
        park.entrar()
        park.entrar()
        park.entrar()
        self.assertEqual(3, park.lotacao())
        park.sair()
        self.assertEqual(repr(park), "Lotacao: 2 de 50 lugares")
    def test_excede(self):
        ''' Test sequence for '20' '''
        park = self.unit.Estacionamento(20)
        for _ in range(19):
            park.entrar()
        self.assertTrue(park.entrar())
        self.assertFalse(park.entrar())
    def test_esvazia(self):
        ''' Test sequence for 'cheio' '''
        park = self.unit.Estacionamento(20)
        park.entrar()
        self.assertEqual(1, park.lotacao())
        park.sair()
        park.sair()
        self.assertEqual(0, park.lotacao())
if __name__ == '__main__':
    unittest.main()
