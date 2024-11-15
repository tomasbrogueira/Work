#! /usr/bin/env python3
''' tests for ex18.py '''
import unittest
SKIP = False
try :
    import ex18
except ImportError:
    SKIP = True
class TestEx18(unittest.TestCase):
    ''' test class for ex18.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex18.py")
        self.unit = ex18
    def test_obter(self):
        ''' Test sequence for '.obter()' default '''
        num = self.unit.Numero()
        self.assertEqual(0, num.obter())
    def test_valor(self):
        ''' Test sequence for '.obter()' 1234 '''
        num = self.unit.Numero(1234)
        self.assertEqual(1234, num.obter())
    def test_alterar(self):
        ''' Test sequence for '.alterar()' '''
        num = self.unit.Numero(12)
        num.alterar(34)
        self.assertEqual(34, num.obter())
    def test_str(self):
        ''' Test sequence for 'str()' '''
        num = self.unit.Numero(321)
        self.assertEqual("321", str(num))
    def test_eq(self):
        ''' Test sequence for 'eq' '''
        num = self.unit.Numero(135)
        num2 = self.unit.Numero(135)
        self.assertTrue(num == num2)
    def test_not_eq(self):
        ''' Test sequence for 'ne' '''
        num = self.unit.Numero(135)
        num2 = self.unit.Numero(153)
        self.assertFalse(num == num2)
    def test_mesmo(self):
        ''' Test sequence for '.mesmo()' '''
        num = self.unit.Numero(135)
        num2 = num
        self.assertTrue(num.mesmo(num2))
    def test_nao_mesmo(self):
        ''' Test sequence for 'not .mesmo()' '''
        num = self.unit.Numero(135)
        num2 = self.unit.Numero(135)
        self.assertTrue(num.mesmo(num2))
    def test_memoria(self):
        ''' Test sequence for Memoria '.obter()' default '''
        num = self.unit.NumeroComMemoria()
        self.assertEqual(0, num.obter())
    def test_alterar_memoria(self):
        ''' Test sequence for Memoria '.alterar()' '''
        num = self.unit.NumeroComMemoria(12)
        num.alterar(34)
        self.assertEqual(34, num.obter())
    def test_desfazer(self):
        ''' Test sequence for '.desfazer()' '''
        num = self.unit.NumeroComMemoria(12)
        num.alterar(34)
        num.desfazer()
        self.assertEqual(12, num.obter())
    def test_desfazer_desfazer(self):
        ''' Test sequence for '.desfazer().desfazer()' '''
        num = self.unit.NumeroComMemoria(12)
        num.alterar(34)
        num.desfazer()
        num.desfazer()
        self.assertEqual(34, num.obter())
    def test_anterior(self):
        ''' Test sequence for '.anterior()' '''
        num = self.unit.NumeroComMemoria(12)
        num.alterar(34)
        self.assertEqual(12, num.anterior())

if __name__ == '__main__':
    unittest.main()
