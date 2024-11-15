#! /usr/bin/env python3
''' tests for ex14.py '''
import unittest
import unittest.mock
import sys
import importlib.util
from io import StringIO
SKIP = False
try :
    import ex14
except ImportError:
    SKIP = True
class TestEx14(unittest.TestCase):
    ''' test class for ex14.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex14.py")
        self.unit = ex14
    def test_equilatero(self):
        ''' Test sequence with 3, 3, 3 '''
        self.assertEqual(self.unit.triangulo(3,3,3), 1)
    def test_escaleno1(self):
        ''' Test sequence with 2, 3, 2 '''
        self.assertEqual(self.unit.triangulo(2,3,2), 2)
    def test_escaleno2(self):
        ''' Test sequence with 2, 2, 3 '''
        self.assertEqual(self.unit.triangulo(2,2,3), 2)
    def test_escaleno3(self):
        ''' Test sequence with 3, 2, 2 '''
        self.assertEqual(self.unit.triangulo(3,2,2), 2)
    def test_isosceles(self):
        ''' Test sequence with 3, 2, 4 '''
        self.assertEqual(self.unit.triangulo(3,2,4), 3)
    def test_naotriangulo(self):
        ''' Test sequence with 1, 2, 3 '''
        self.assertEqual(self.unit.triangulo(1,2,3), 0)
    def test_nulo(self):
        ''' Test sequence with 3, 3, 0 '''
        self.assertEqual(self.unit.triangulo(3,3,0), None)
    def test_negativo(self):
        ''' Test sequence with 3, -2, 3 '''
        self.assertEqual(self.unit.triangulo(3,-2,3), None)
    def test_usage(self):
        ''' Test sequence with no arguments '''
        out = sys.stdout
        sys.stdout = StringIO()
        with unittest.mock.patch.object(sys, 'argv', ['ex14']):
            spec = importlib.util.spec_from_file_location('__main__', 'ex14.py')
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), "Usage: ex14 a b c\n")
        sys.stdout = out
    def test_argv(self):
        ''' Test sequence with arguments '''
        out = sys.stdout
        sys.stdout = StringIO()
        with unittest.mock.patch.object(sys, 'argv', ['ex14', '4', '5', '6']):
            spec = importlib.util.spec_from_file_location('__main__', 'ex14.py')
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), "3\n")
        sys.stdout = out
if __name__ == '__main__':
    unittest.main()
