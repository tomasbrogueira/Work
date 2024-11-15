#! /usr/bin/env python3
''' tests for ex11.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx11(unittest.TestCase):
    ''' test class for ex11.py '''
    exp = 'Escreva um inteiro\n? O numero tem %d zeros seguidos\n'
    def setUp(self) :
        if not exists('ex11.py'):
            self.skipTest("no ex11.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex11.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_98007640003(self):
        ''' Test sequence with number 98007640003 '''
        sys.stdin = StringIO('98007640003\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 3)
    def test_70000003(self):
        ''' Test sequence with number 70000003 '''
        sys.stdin = StringIO('70000003\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 5)
    def test_700(self):
        ''' Test sequence with number 700 '''
        sys.stdin = StringIO('700\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 1)
    def test_10203040(self):
        ''' Test sequence with number 10203040 '''
        sys.stdin = StringIO('10203040\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 0)
if __name__ == '__main__':
    unittest.main()
