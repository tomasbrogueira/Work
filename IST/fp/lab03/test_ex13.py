#! /usr/bin/env python3
''' tests for ex01.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx13(unittest.TestCase):
    ''' test class for ex01.py '''
    exp = '1 x 8 + 1 = 9\n12 x 8 + 2 = 98\n123 x 8 + 3 = 987\n' \
        '1234 x 8 + 4 = 9876\n12345 x 8 + 5 = 98765\n' \
        '123456 x 8 + 6 = 987654\n1234567 x 8 + 7 = 9876543\n' \
        '12345678 x 8 + 8 = 98765432\n123456789 x 8 + 9 = 987654321\n'
    def setUp(self) :
        if not exists('ex13.py'):
            self.skipTest("no ex13.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex13.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_1(self):
        ''' Test sequence '''
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp)
if __name__ == '__main__':
    unittest.main()
