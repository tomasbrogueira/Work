#! /usr/bin/env python3
''' tests for ex06.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx06(unittest.TestCase):
    ''' test class for ex06.py '''
    exp = 'Escreva um inteiro\n? Resultado: %d\n'
    def setUp(self) :
        if not exists('ex06.py'):
            self.skipTest("no ex06.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex06.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_785554(self):
        ''' Test sequence with number 785554 '''
        sys.stdin = StringIO('785554\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 7555)
    def test_73(self):
        ''' Test sequence with number 73 '''
        sys.stdin = StringIO('73\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 73)
    def test_0(self):
        ''' Test sequence with number 0 '''
        sys.stdin = StringIO('0\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 0)
    def test_68420(self):
        ''' Test sequence with number 68420 '''
        sys.stdin = StringIO('68420\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 0)
if __name__ == '__main__':
    unittest.main()
