#! /usr/bin/env python3
''' tests for ex01.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx01(unittest.TestCase):
    ''' test class for ex01.py '''
    def setUp(self) :
        if not exists('ex01.py'):
            self.skipTest("no ex01.py")
        self.stdout = sys.stdout
        sys.stdout = StringIO()
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex01.py')
        self.module = importlib.util.module_from_spec(self.spec)
    def tearDown(self):
        sys.stdout = self.stdout
    def test_1(self):
        ''' Test sequence for soma '''
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), "Soma = 10\n")
if __name__ == '__main__':
    unittest.main()
