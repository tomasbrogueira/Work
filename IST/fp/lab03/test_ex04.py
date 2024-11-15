#! /usr/bin/env python3
''' tests for ex04.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx04(unittest.TestCase):
    ''' test class for ex04.py '''
    exp = 'horas de trabalho: salário/hora: pagar %d\n'
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
    def test_56(self):
        ''' Test sequence with numbers 56, 35 '''
        sys.stdin = StringIO('56\n35\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 2520)
    def test_32(self):
        ''' Test sequence with numbers 32, 78 '''
        sys.stdin = StringIO('32\n78\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 2496)
    def test_40(self):
        ''' Test sequence with numbers 40, 24 '''
        sys.stdin = StringIO('40\n24\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 960)
    def test_41(self):
        ''' Test sequence with numbers 41, 30 '''
        sys.stdin = StringIO('41\n30\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 1260)
if __name__ == '__main__':
    unittest.main()
