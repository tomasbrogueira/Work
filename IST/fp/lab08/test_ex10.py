#! /usr/bin/env python3
''' tests for ex10.py '''
import unittest
SKIP = False
try :
    import ex10
except ImportError:
    SKIP = True
class TestEx10(unittest.TestCase):
    ''' test class for ex10.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex10.py")
        self.unit = ex10
    def test_combustivel(self):
        ''' Test sequence for '.combustivel()' '''
        auto = self.unit.Automovel(60, 10, 15)
        self.assertEqual(10, auto.combustivel())
    def test_autonomia(self):
        ''' Test sequence for '.autonomia()' '''
        auto = self.unit.Automovel(60, 10, 15)
        self.assertEqual(66, auto.autonomia())
    def test_abastece(self):
        ''' Test sequence for '.abastece(45)' '''
        auto = self.unit.Automovel(60, 10, 15)
        self.assertEqual('366 Km até abastecimento', auto.abastece(45))
    def test_percorre(self):
        ''' Test sequence for '.percorre(39)' '''
        auto = self.unit.Automovel(60, 10, 15)
        self.assertEqual('36 Km até abastecimento', auto.percorre(30))
    def test_nao_percorre(self):
        ''' Test sequence for '.percorre(100)' '''
        auto = self.unit.Automovel(60, 10, 15)
        self.assertRaises(ValueError, auto.percorre, 100)
    def test_abastece_e_percorre(self):
        ''' Test sequence for 'abastece e percorre' '''
        auto = self.unit.Automovel(60, 10, 15)
        auto.abastece(45)
        auto.percorre(150)
        self.assertEqual(32.5, auto.combustivel())
    def test_capacidade(self):
        ''' Test sequence for '.abastece(54)' '''
        auto = self.unit.Automovel(60, 10, 15)
        self.assertRaises(ValueError, auto.abastece, 54)
    def test_retira(self):
        ''' Test sequence for '.abastece(-2)' '''
        auto = self.unit.Automovel(60, 10, 15)
        self.assertRaises(ValueError, auto.abastece, -2)
    def test_nullcap(self):
        ''' Test sequence for '0, 10, 15' '''
        self.assertRaises(ValueError, self.unit.Automovel, 0, 10, 15)
    def test_nullcons(self):
        ''' Test sequence for '60, 10, 0' '''
        self.assertRaises(ValueError, self.unit.Automovel, 60, 10, 0)
    def test_negquant(self):
        ''' Test sequence for '60, -1, 15' '''
        self.assertRaises(ValueError, self.unit.Automovel, 60, -1, 15)

if __name__ == '__main__':
    unittest.main()
