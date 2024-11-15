#! /usr/bin/env python3
''' tests for ex04.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx04(unittest.TestCase):
    ''' test class for ex04.py '''
    exp = 'Escreva um número de segundos\n(um número negativo para terminar)\n? '
    res = 'O número de dias correspondente é '
    def setUp(self) :
        if not exists('ex04.py'):
            self.skipTest("no ex04.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex04.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_45(self):
        ''' Test sequence for '45 6654441' '''
        sys.stdin = StringIO('45\n6654441\n-1\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        val1, val2 = 0.00052083, 77.01899306
        out = self.exp + self.res + f'{val1}\n' + self.exp + self.res + f'{val2}\n' + self.exp
        self.assertEqual(sys.stdout.read(), out)
    def test_neg(self):
        ''' Test sequence for '-8' '''
        sys.stdin = StringIO('-8\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp)
if __name__ == '__main__':
    unittest.main()
