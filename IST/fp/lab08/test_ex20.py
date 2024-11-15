#! /usr/bin/env python3
''' tests for ex20.py '''
import unittest
import sys
from io import StringIO
SKIP = False
try :
    import ex20
except ImportError:
    SKIP = True
class TestEx20(unittest.TestCase):
    ''' test class for ex20.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex20.py")
        self.unit = ex20
        self.stdout = sys.stdout
        sys.stdout = StringIO()
    def tearDown(self):
        sys.stdout = self.stdout
    def test_super(self):
        ''' Test sequence for 'SuperHeroi' '''
        sup = self.unit.SuperHeroi("Sr. Incrível")
        self.unit.realiza_operacao_voar(sup) # no raise
        self.unit.realiza_operacao_saltar(sup) # no raise
        self.unit.realiza_operacao_correr(sup) # no raise
        self.unit.realiza_operacao_nadar(sup) # no raise
        self.unit.realiza_operacao_andar(sup) # no raise
    def test_heroi(self):
        ''' Test sequence for 'Heroi' '''
        her = self.unit.Heroi("Sr. Incrível")
        self.assertRaises(AttributeError, self.unit.realiza_operacao_voar, her)
        self.assertRaises(AttributeError, self.unit.realiza_operacao_saltar, her)
        self.unit.realiza_operacao_correr(her) # no raise
        self.unit.realiza_operacao_nadar(her) # no raise
        self.unit.realiza_operacao_andar(her) # no raise
    def test_comum(self):
        ''' Test sequence for 'Comum' '''
        com = self.unit.Comum("Sr. Incrível")
        self.assertRaises(AttributeError, self.unit.realiza_operacao_voar, com)
        self.unit.realiza_operacao_saltar(com) # no raise
        self.unit.realiza_operacao_correr(com) # no raise
        self.unit.realiza_operacao_nadar(com) # no raise
        self.unit.realiza_operacao_andar(com) # no raise
if __name__ == '__main__':
    unittest.main()
