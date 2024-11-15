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
    def test_1(self):
        ''' Test sequence for 'b': '''
        dic1 = {'a' : [1, 2], 'b' : [3, 4]}
        dic2 = {'b' : [4, 5], 'c' : [6, 7]}
        dic = {'a': [1, 2], 'b': [3, 4, 5], 'c': [6, 7]}
        self.assertEqual(self.unit.soma_dicionarios(dic1,dic2),dic)
    def test_2(self):
        ''' Test sequence for 'disjunto' '''
        dic1 = {'a' : [1, 2], 'b' : [3, 4]}
        dic2 = {'c' : [4, 5], 'd' : [6, 7]}
        dic = {'a': [1, 2], 'b': [3, 4], 'c': [4, 5], 'd': [6, 7]}
        self.assertEqual(self.unit.soma_dicionarios(dic1,dic2),dic)
    def test_3(self):
        ''' Test sequence for 'mesma chaves, valores distintos' '''
        dic1 = {'a' : [1, 2], 'b' : [3, 4]}
        dic2 = {'a' : [4, 5], 'b' : [6, 7]}
        dic = {'a': [1, 2, 4, 5], 'b': [3, 4, 6, 7]}
        self.assertEqual(self.unit.soma_dicionarios(dic1,dic2),dic)
    def test_4(self):
        ''' Test sequence for 'mesma chave, valores iguais' '''
        dic1 = {'a' : [1, 2], 'b' : [3, 4]}
        dic2 = {'a' : [1, 2], 'b' : [3, 4]}
        dic = {'a': [1, 2], 'b': [3, 4]}
        self.assertEqual(self.unit.soma_dicionarios(dic1,dic2),dic)
    def test_5(self):
        ''' Test sequence for 'mesma chave, valores parcialmente sobrepostos' '''
        dic1 = {'a' : [1, 2], 'b' : [3, 4]}
        dic2 = {'a' : [2, 1], 'b' : [4, 3]}
        dic = {'a': [1, 2], 'b': [3, 4]}
        self.assertEqual(self.unit.soma_dicionarios(dic1,dic2),dic)
if __name__ == '__main__':
    unittest.main()
