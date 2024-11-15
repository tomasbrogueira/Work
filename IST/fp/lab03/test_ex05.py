#! /usr/bin/env python3
''' tests for ex05.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx05(unittest.TestCase):
    ''' test class for ex05.py '''
    exp = 'Escreva um dígito\n(-1 para terminar)\n? '
    end = 'O número é: %d\n'
    def setUp(self) :
        if not exists('ex05.py'):
            self.skipTest("no ex05.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex05.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_56(self):
        ''' Test sequence with numbers 5 and 6 '''
        sys.stdin = StringIO('5\n6\n-1\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), (self.exp * 3 + self.end) % 56)
    def test_3257(self):
        ''' Test sequence with numbers 3, 2, 5, 7 '''
        sys.stdin = StringIO('3\n2\n5\n7\n-1\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), (self.exp * 5 + self.end) % 3257)
    def test_007(self):
        ''' Test sequence with numbers 0, 0, 7 '''
        sys.stdin = StringIO('0\n0\n7\n-1\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), (self.exp * 4 + self.end) % 7)
    def test_12000(self):
        ''' Test sequence with numbers 1, 2, 0, 0, 0 '''
        sys.stdin = StringIO('1\n2\n0\n0\n0\n-1\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), (self.exp * 6 + self.end) % 12000)
if __name__ == '__main__':
    unittest.main()
