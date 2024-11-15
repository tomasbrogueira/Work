#! /usr/bin/env python3
''' tests for ex01.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx01(unittest.TestCase):
    ''' test class for ex01.py '''
    exp = 'Vou pedir-lhe dois numeros\n' \
        'Escreva o primeiro numero, x = ' \
        'Escreva o segundo numero, y = ' \
        'O valor de (x + 3 * y) * (x - y) e: %s\n'
    def setUp(self) :
        if not exists('ex01.py'):
            self.skipTest("no ex01.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex01.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_56(self):
        ''' Test sequence with numbers 5 and 6 '''
        sys.stdin = StringIO('5\n6\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % -23)
    def test_73(self):
        ''' Test sequence with numbers 7 and 3 '''
        sys.stdin = StringIO('7\n3\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 64)
if __name__ == '__main__':
    unittest.main()
