#! /usr/bin/env python3
''' tests for ex02.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx02(unittest.TestCase):
    ''' test class for ex02.py '''
    exp = 'Escreva um número de segundos\n? O número de dias correspondentes é '
    def setUp(self) :
        if not exists('ex02.py'):
            self.skipTest("no ex02.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex02.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_65432998(self):
        ''' Test sequence for '65432998' '''
        sys.stdin = StringIO('65432998\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        val = 757.32636574
        out = self.exp + f'{val}\n'
        self.assertEqual(sys.stdout.read(), out)
    def test_1036800(self):
        ''' Test sequence for '1036800' '''
        sys.stdin = StringIO('1036800\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        val = 12.
        out = self.exp + f'{val}\n'
        self.assertEqual(sys.stdout.read(), out)
if __name__ == '__main__':
    unittest.main()
