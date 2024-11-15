#! /usr/bin/env python3
''' tests for ex06.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx06(unittest.TestCase):
    ''' test class for ex06.py '''
    exp = 'Nota ? '
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
    def test_pos(self):
        ''' Test sequence for '12 17 19 15 18 16 16' '''
        sys.stdin = StringIO('12\n17\n19\n15\n18\n16\n16\n-1\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        out = self.exp * 8 + '7 positivas 100.0 %\n'
        self.assertEqual(sys.stdout.read(), out)
    def test_mix(self):
        ''' Test sequence for '12 12 9 12' '''
        sys.stdin = StringIO('12\n12\n9\n12\n-1\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        out = self.exp * 5 + '3 positivas 75.0 %\n'
        self.assertEqual(sys.stdout.read(), out)
if __name__ == '__main__':
    unittest.main()
