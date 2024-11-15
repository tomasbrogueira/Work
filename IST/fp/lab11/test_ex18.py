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
    def test_1(self):
        ''' Test sequence for 'None' '''
        dic = {}
        func = self.unit.atualiza(dic)
        self.assertEqual(func('a', 2), None)
    def test_2(self):
        ''' Test sequence for update '''
        dic = {'a': 12}
        func = self.unit.atualiza(dic)
        self.assertEqual(func('a', 2), 12)
    def test_3(self):
        ''' Test sequence for multiple adds '''
        dic = {}
        func = self.unit.atualiza(dic)
        func('a', 3)
        func('x', -5)
        self.assertEqual(len(dic), 2)
        self.assertEqual(dic['a'], 3)
        self.assertEqual(dic['x'], -5)
    def test_4(self):
        ''' Test sequence for mutiple replaces '''
        dic = {'a': 12, 12: 'a'}
        func = self.unit.atualiza(dic)
        func('a', 3)
        func(12, 'x')
        self.assertEqual(len(dic), 2)
        self.assertEqual(dic['a'], 3)
        self.assertEqual(dic[12], 'x')
if __name__ == '__main__':
    unittest.main()
