#! /usr/bin/env python3
''' tests for ex11.py '''
import unittest
import random
SKIP = False
try :
    import ex11
except ImportError:
    SKIP = True
class TestEx11(unittest.TestCase):
    ''' test class for ex11.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex11.py")
        self.unit = ex11
    def test_cardinal(self):
        ''' Test sequence for '.cardinal()' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        self.assertEqual(4, conj.cardinal())
    def test_repr(self):
        ''' Test sequence for 'repr()' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        self.assertEqual("{1, 2, 3, 4}", repr(conj))
    def test_retira(self):
        ''' Test sequence for '.retira()' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        conj.retira(3)
        self.assertEqual("{1, 2, 4}", repr(conj))
    def test_element(self):
        ''' Test sequence for '.element()' '''
        random.seed(0)
        conj = self.unit.Conjunto(1, 2, 3, 4)
        self.assertEqual(4, conj.element())
    def test_nao_vazio(self):
        ''' Test sequence for 'não vazio' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        self.assertFalse(conj.vazio())
    def test_vazio(self):
        ''' Test sequence for 'vazio' '''
        conj = self.unit.Conjunto(1)
        conj.retira(1)
        self.assertTrue(conj.vazio())
    def test_pertence(self):
        ''' Test sequence for '.pertence(3)' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        self.assertTrue(conj.pertence(3))
    def test_nao_pertence(self):
        ''' Test sequence for '.pertence(5)' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        self.assertFalse(conj.pertence(5))
    def test_insere(self):
        ''' Test sequence for '.cardinal()' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        conj.insere(8)
        self.assertEqual(5, conj.cardinal())
    def test_sub(self):
        ''' Test sequence for '.subconjunto(conj)' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        conj2 = self.unit.Conjunto(2, 3)
        self.assertTrue(conj2.subconjunto(conj))
    def test_nosub(self):
        ''' Test sequence for '.subconjunto(conj2)' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        conj2 = self.unit.Conjunto(2, 3)
        self.assertFalse(conj.subconjunto(conj2))
    def test_uniao(self):
        ''' Test sequence for '.uniao()' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        conj2 = self.unit.Conjunto(3, 4, 5, 6)
        self.assertEqual("{1, 2, 3, 4, 5, 6}", repr(conj.uniao(conj2)))
    def test_intersecao(self):
        ''' Test sequence for '.intersecao()' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        conj2 = self.unit.Conjunto(3, 4, 5, 6)
        self.assertEqual("{3, 4}", repr(conj.intersecao(conj2)))
    def test_diferenca(self):
        ''' Test sequence for '.diferenca()' '''
        conj = self.unit.Conjunto(1, 2, 3, 4)
        conj2 = self.unit.Conjunto(3, 4, 5, 6)
        self.assertEqual("{1, 2}", repr(conj.diferenca(conj2)))

if __name__ == '__main__':
    unittest.main()
