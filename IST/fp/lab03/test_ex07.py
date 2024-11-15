#! /usr/bin/env python3
''' tests for ex07.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx07(unittest.TestCase):
    ''' test class for ex07.py '''
    exp = 'Escreva um inteiro positivo\n? O número invertido é %d\n'
    def setUp(self) :
        if not exists('ex07.py'):
            self.skipTest("no ex07.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex07.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_7633256(self):
        ''' Test sequence with number 7633256 '''
        sys.stdin = StringIO('7633256\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 6523367)
    def test_123456(self):
        ''' Test sequence with number 123456 '''
        sys.stdin = StringIO('123456\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 654321)
    def test_014(self):
        ''' Test sequence with number 014 '''
        sys.stdin = StringIO('014\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 41)
    def test_120(self):
        ''' Test sequence with number 120 '''
        sys.stdin = StringIO('120\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 21)
if __name__ == '__main__':
    unittest.main()
