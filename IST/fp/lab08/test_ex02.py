#! /usr/bin/env python3
''' tests for ex02.py '''
import unittest
import sys
from io import StringIO
SKIP = False
try :
    import ex02
except ImportError:
    SKIP = True
class TestEx02(unittest.TestCase):
    ''' test class for ex02.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex02.py")
        self.unit = ex02
        self.stdout = sys.stdout
        sys.stdout = StringIO()
    def tearDown(self):
        sys.stdout = self.stdout
    def test_exemplo(self):
        ''' Test sequence for '30' '''
        bus = self.unit.Autocarro(30)
        self.assertEqual(0, bus.passageiros())
        self.assertEqual(30, bus.capacidade())
        bus.sai(35)
        self.assertEqual(0, bus.passageiros())
        bus.entra(40)
        self.assertEqual(30, bus.passageiros())
        bus.sai(5)
        self.assertEqual(25, bus.passageiros())
        self.assertEqual(str(bus), "Autocarro de 30 lugares com 25 passageiros.")
        bus.sai(26)
        self.assertEqual(0, bus.passageiros())
if __name__ == '__main__':
    unittest.main()
