#! /usr/bin/env python3
''' tests for ex11.py '''
import unittest
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
    def test_1(self):
        ''' Test sequence for '[('a', 8), ('b', 9), ('a', 3)]' '''
        self.assertEqual(self.unit.agrupa_por_chave([('a', 8), ('b', 9), ('a', 3)]),
            {'a': [8, 3], 'b': [9]})
    def test_2(self):
        ''' Test sequence for '[(8, 'a'), (9, 'b'), (8, 'x')]' '''
        self.assertEqual(self.unit.agrupa_por_chave([(8, 'a'), (9, 'b'), (8, 'x')]),
            {8: ['a', 'x'], 9: ['b']})
    def test_3(self):
        ''' Test sequence for '[]' '''
        self.assertEqual(self.unit.agrupa_por_chave([]), {})
if __name__ == '__main__':
    unittest.main()
