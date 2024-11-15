#! /usr/bin/env python3
''' tests for ex06.py '''
import unittest
tarifario = {'local':1, 'nacional':12, 'movel':20, 'internacional':41}
SKIP = False
try :
    import ex06
except ImportError:
    SKIP = True
class TestEx06(unittest.TestCase):
    ''' test class for ex06.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex06.py")
        self.unit = ex06
    def test_zero(self):
        ''' Test sequence for '.consulta_custo()' '''
        cnt = self.unit.CartaoTelefonico(tarifario)
        self.assertEqual(0, cnt.consulta_custo())
    def test_nulo(self):
        ''' Test sequence for '.consulta_chamadas()' '''
        cnt = self.unit.CartaoTelefonico(tarifario)
        self.assertEqual(0, cnt.consulta_chamadas())
    def test_local(self):
        ''' Test sequence for 'local' '''
        cnt = self.unit.CartaoTelefonico(tarifario)
        cnt.chamada('local', 5)
        self.assertEqual(5, cnt.consulta_custo())
    def test_nacional(self):
        ''' Test sequence for 'nacional' '''
        cnt = self.unit.CartaoTelefonico(tarifario)
        cnt.chamada('nacional', 5)
        self.assertEqual(60, cnt.consulta_custo())
    def test_movel(self):
        ''' Test sequence for 'movel' '''
        cnt = self.unit.CartaoTelefonico(tarifario)
        cnt.chamada('movel', 5)
        self.assertEqual(100, cnt.consulta_custo())
    def test_inter(self):
        ''' Test sequence for 'internacional' '''
        cnt = self.unit.CartaoTelefonico(tarifario)
        cnt.chamada('internacional', 5)
        self.assertEqual(205, cnt.consulta_custo())
    def test_multi(self):
        ''' Test sequence for 'todos' '''
        cnt = self.unit.CartaoTelefonico(tarifario)
        cnt.chamada('local', 5)
        cnt.chamada('nacional', 5)
        cnt.chamada('movel', 5)
        cnt.chamada('internacional', 5)
        self.assertEqual(370, cnt.consulta_custo())
        self.assertEqual(4, cnt.consulta_chamadas())
    def test_terif(self):
        ''' Test sequence for 'chamada regional' '''
        cnt = self.unit.CartaoTelefonico(tarifario)
        self.assertRaises(ValueError, cnt.chamada, 'regional', 3)
    def test_duracao(self):
        ''' Test sequence for 'chamada nacional' '''
        cnt = self.unit.CartaoTelefonico(tarifario)
        self.assertRaises(ValueError, cnt.chamada, 'nacional', 0)
if __name__ == '__main__':
    unittest.main()
