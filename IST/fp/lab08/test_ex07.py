#! /usr/bin/env python3
''' tests for ex07.py '''
import unittest
import sys
from io import StringIO
SKIP = False
try :
    import ex07
except ImportError:
    SKIP = True
class TestEx07(unittest.TestCase):
    ''' test class for ex07.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex07.py")
        self.unit = ex07
        self.stdout = sys.stdout
        sys.stdout = StringIO()
    def tearDown(self):
        sys.stdout = self.stdout
    def test_repr(self):
        ''' Test sequence for 'repr(ski)' '''
        ski = self.unit.SkiRental(20, 35)
        self.assertEqual("Ski: 20; Snowboard: 35",repr(ski))
    def test_ski(self):
        ''' Test sequence for '.preco_ski()' '''
        ski = self.unit.SkiRental(20, 35)
        self.assertEqual(20, ski.preco_ski())
    def test_snowboard(self):
        ''' Test sequence for '.preco_snowboarsd()' '''
        ski = self.unit.SkiRental(20, 35)
        self.assertEqual(35, ski.preco_snowboarsd())
    def test_reserva(self):
        ''' Test sequence for '.reserva(3,1)' '''
        ski = self.unit.SkiRental(20, 35)
        self.assertEqual(95, ski.reserva(3,1))

if __name__ == '__main__':
    unittest.main()
