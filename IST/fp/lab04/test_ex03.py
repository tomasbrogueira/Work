#! /usr/bin/env python3
''' tests for ex03.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx03(unittest.TestCase):
    ''' test class for ex03.py '''
    exp = 'x1 = x2 = x3 = x4 = x5 = média = '
    def setUp(self) :
        if not exists('ex03.py'):
            self.skipTest("no ex03.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex03.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_12345(self):
        ''' Test sequence for '1 2 3 4 5' '''
        sys.stdin = StringIO('1\n2\n3\n4\n5\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        med, var = 3., 1.58113883
        out = self.exp + f'{med} desvio padrão = {var}\n'
        self.assertEqual(sys.stdout.read(), out)
    def test_11355(self):
        ''' Test sequence for '1 1 3 5 5' '''
        sys.stdin = StringIO('1\n1\n3\n5\n5\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        med, var = 3., 2.
        out = self.exp + f'{med} desvio padrão = {var}\n'
        self.assertEqual(sys.stdout.read(), out)
    def test_22344(self):
        ''' Test sequence for '2 2 3 4 4' '''
        sys.stdin = StringIO('2\n2\n3\n4\n4\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        med, var = 3., 1.
        out = self.exp + f'{med} desvio padrão = {var}\n'
        self.assertEqual(sys.stdout.read(), out)
    def test_float(self):
        ''' Test sequence for '2.1 2.34 3.902 4.56 -12.3' '''
        sys.stdin = StringIO('2.1\n2.34\n3.902\n4.56\n-12.3\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        med, var = 0.1204, 7.02001288
        out = self.exp + f'{med} desvio padrão = {var}\n'
        self.assertEqual(sys.stdout.read(), out)
if __name__ == '__main__':
    unittest.main()
