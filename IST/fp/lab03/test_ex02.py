#! /usr/bin/env python3
''' tests for ex01.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx02(unittest.TestCase):
    ''' test class for ex01.py '''
    exp = 'Escreva o número de segundos dias: %d horas: %d mins: %d segs: %d\n'
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
    def test_345678(self):
        ''' Test sequence with number 345678 '''
        sys.stdin = StringIO('345678\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % (4, 0, 1, 18))
    def test_876543(self):
        ''' Test sequence with number 876543 '''
        sys.stdin = StringIO('876543\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % (10, 3, 29, 3))
if __name__ == '__main__':
    unittest.main()
