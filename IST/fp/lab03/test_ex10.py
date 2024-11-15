#! /usr/bin/env python3
''' tests for ex10.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx10(unittest.TestCase):
    ''' test class for ex10.py '''
    exp = 'Escreva um número\n-> %s\n'
    def setUp(self) :
        if not exists('ex10.py'):
            self.skipTest("no ex10.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.stdin = sys.stdin
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex10.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
        sys.stdin = self.stdin
    def test_347(self):
        ''' Test sequence with number 347 '''
        sys.stdin = StringIO('347\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 347743)
    def test_2500(self):
        ''' Test sequence with number 2500 '''
        sys.stdin = StringIO('2500\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 25000052)
    def test_007(self):
        ''' Test sequence with number 007 '''
        sys.stdin = StringIO('007\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 77)
    def test_2005(self):
        ''' Test sequence with number 2005 '''
        sys.stdin = StringIO('2005\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 20055002)
    def test_02500(self):
        ''' Test sequence with number 02500 '''
        sys.stdin = StringIO('2500\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), self.exp % 25000052)
if __name__ == '__main__':
    unittest.main()
