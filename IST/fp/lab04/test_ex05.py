#! /usr/bin/env python3
''' tests for ex05.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx05(unittest.TestCase):
    ''' test class for ex05.py '''
    exp = 'Qual o valor de x\n? Qual o valor de n\n? O valor da soma é '
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
    def test_2_3(self):
        ''' Test sequence for '2 3' '''
        sys.stdin = StringIO('2\n3\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        val = 6.33333333
        out = self.exp + f'{val}\n'
        self.assertEqual(sys.stdout.read(), out)
    def test_415_12(self):
        ''' Test sequence for '4.15 12' '''
        sys.stdin = StringIO('4.15\n12\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        val = 63.4095399
        out = self.exp + f'{val}\n'
        self.assertEqual(sys.stdout.read(), out)
    def test__65_8(self):
        ''' Test sequence for '-6.5 8' '''
        sys.stdin = StringIO('-6.5\n8\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        val = 34.05188967
        out = self.exp + f'{val}\n'
        self.assertEqual(sys.stdout.read(), out)
if __name__ == '__main__':
    unittest.main()
