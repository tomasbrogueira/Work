#! /usr/bin/env python3
''' tests for ex03.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx03(unittest.TestCase):
    ''' test class for ex03.py '''
    exp = 'x1 = x2 = x3 = O maior é %d\n'
    def setUp(self) :
        if not exists('ex03.py'):
            self.skipTest("no ex03.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex03.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_123(self):
        ''' Test sequence with numbers 1, 2, 3 '''
        sys.stdin = StringIO('1\n2\n3\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 3)
    def test_731(self):
        ''' Test sequence with numbers 7, 3, 1 '''
        sys.stdin = StringIO('7\n3\n1\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 7)
    def test_793(self):
        ''' Test sequence with numbers 7, 9, 3 '''
        sys.stdin = StringIO('7\n9\n3\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 9)
    def test_386(self):
        ''' Test sequence with numbers 3, 8, 6 '''
        sys.stdin = StringIO('3\n8\n6\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 8)
    def test_425(self):
        ''' Test sequence with numbers 4, 2, 5 '''
        sys.stdin = StringIO('4\n2\n5\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 5)
    def test_825(self):
        ''' Test sequence with numbers 8, 2, 5 '''
        sys.stdin = StringIO('8\n2\n5\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 8)
if __name__ == '__main__':
    unittest.main()
