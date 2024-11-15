#! /usr/bin/env python3
''' tests for ex01.py '''
import unittest
import sys
import importlib.util
from io import StringIO
from os.path import exists
class TestEx01(unittest.TestCase):
    ''' test class for ex01.py '''
    exp = 'distância percorrida (Km): tempo gasto (minutos): '
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
    def test_300_200(self):
        ''' Test sequence for '300 200' '''
        sys.stdin = StringIO('300\n200\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        kmh, mseg = 90., 25.
        out = self.exp + f'{kmh} Km/h\n{mseg} m/s\n'
        self.assertEqual(sys.stdout.read(), out)
    def test_120_20(self):
        ''' Test sequence for '120 20' '''
        sys.stdin = StringIO('120\n20\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        kmh, mseg = 360., 100.
        out = self.exp + f'{kmh} Km/h\n{mseg} m/s\n'
        self.assertEqual(sys.stdout.read(), out)
    def test_30_100(self):
        ''' Test sequence for '30 100' '''
        sys.stdin = StringIO('30\n100\n')
        self.spec.loader.exec_module(self.module)
        sys.stdout.seek(0)
        kmh, mseg = 18., 5.
        out = self.exp + f'{kmh} Km/h\n{mseg} m/s\n'
        self.assertEqual(sys.stdout.read(), out)
if __name__ == '__main__':
    unittest.main()
