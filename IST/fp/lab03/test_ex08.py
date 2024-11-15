#! /usr/bin/env python3
''' tests for ex08.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx08(unittest.TestCase):
    ''' test class for ex08.py '''
    exp = 'Escreva um numero para eu escrever a tabuada da multiplicação\n' \
        'Num -> %d x 1 = %d\n%d x 2 = %d\n%d x 3 = %d\n%d x 4 = %d\n' \
        '%d x 5 = %d\n%d x 6 = %d\n%d x 7 = %d\n' \
        '%d x 8 = %d\n%d x 9 = %d\n%d x 10 = %s\n'
    def setUp(self) :
        if not exists('ex08.py'):
            self.skipTest("no ex08.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.res = ()
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex08.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_8(self):
        ''' Test sequence with number 8 '''
        sys.stdin = StringIO('8\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        for i in range(1,11):
            self.res += (8, 8*i)
        self.assertEqual(sys.stdout.read(), self.exp % self.res)
    def test_2(self):
        ''' Test sequence with number 2 '''
        sys.stdin = StringIO('2\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        for i in range(1,11):
            self.res += (2, 2*i)
        self.assertEqual(sys.stdout.read(), self.exp % self.res)
    def test_12(self):
        ''' Test sequence with number 12 '''
        sys.stdin = StringIO('12\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        for i in range(1,11):
            self.res += (12, 12*i)
        self.assertEqual(sys.stdout.read(), self.exp % self.res)
if __name__ == '__main__':
    unittest.main()
