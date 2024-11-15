#! /usr/bin/env python3
''' tests for ex12.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx12(unittest.TestCase):
    ''' test class for ex12.py '''
    def setUp(self) :
        if not exists('ex12.py'):
            self.skipTest("no ex12.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex12.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_200(self):
        ''' Test sequence with number 200 '''
        sys.stdin = StringIO('200\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        exp = 'Escreva uma quantia ? 4 * 50 €\n'
        self.assertEqual(sys.stdout.read(), exp)
    def test_237_89(self):
        ''' Test sequence with number 237.89 '''
        sys.stdin = StringIO('237.89\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        exp = 'Escreva uma quantia ? 4 * 50 €\n1 * 20 €\n1 * 10 €\n'\
            '1 * 5 €\n1 * 2 €\n1 * 50 cênt\n1 * 20 cênt\n'\
            '1 * 10 cênt\n1 * 5 cênt\n2 * 2 cênt\n'
        self.assertEqual(sys.stdout.read(), exp)
    def test_101_73(self):
        ''' Test sequence with number 101.73 '''
        sys.stdin = StringIO('101.73\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        exp = 'Escreva uma quantia ? 2 * 50 €\n1 * 1 €\n' \
            '1 * 50 cênt\n1 * 20 cênt\n1 * 2 cênt\n1 * 1 cênt\n'
        self.assertEqual(sys.stdout.read(), exp)
    def test_8(self):
        ''' Test sequence with number 8 '''
        sys.stdin = StringIO('8\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        exp = 'Escreva uma quantia ? 1 * 5 €\n1 * 2 €\n1 * 1 €\n'
        self.assertEqual(sys.stdout.read(), exp)
if __name__ == '__main__':
    unittest.main()
