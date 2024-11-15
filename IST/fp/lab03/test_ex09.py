#! /usr/bin/env python3
''' tests for ex09.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx09(unittest.TestCase):
    ''' test class for ex09.py '''
    exp = 'Escreva um inteiro positivo\n? A soma dos dígitos é %s\n'
    def setUp(self) :
        if not exists('ex09.py'):
            self.skipTest("no ex09.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex09.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_123876(self):
        ''' Test sequence with number 123876 '''
        sys.stdin = StringIO('123876\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 27)
    def test_1000001(self):
        ''' Test sequence with number 1000001 '''
        sys.stdin = StringIO('1000001\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 2)
    def test_100000(self):
        ''' Test sequence with number 100000 '''
        sys.stdin = StringIO('100000\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 1)
    def test_000001(self):
        ''' Test sequence with number 000001 '''
        sys.stdin = StringIO('000001\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 1)
if __name__ == '__main__':
    unittest.main()
