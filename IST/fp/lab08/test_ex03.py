#! /usr/bin/env python3
''' tests for ex03.py '''
import unittest
import sys
from io import StringIO
SKIP = False
try :
    import ex03
except ImportError:
    SKIP = True
class TestEx03(unittest.TestCase):
    ''' test class for ex03.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex03.py")
        self.unit = ex03
        self.stdout = sys.stdout
        sys.stdout = StringIO()
    def tearDown(self):
        sys.stdout = self.stdout
    def test_repr(self):
        ''' Test sequence for '5, 12, 2021' '''
        data = self.unit.Data(5, 12, 2021)
        self.assertEqual(repr(data), "05/12/2021")
    def test_dia(self):
        ''' Test sequence for '5, 12, 2021' '''
        data = self.unit.Data(5, 12, 2021)
        self.assertEqual(data.dia(), 5)
    def test_mes(self):
        ''' Test sequence for '5, 12, 2021' '''
        data = self.unit.Data(5, 12, 2021)
        self.assertEqual(data.mes(), 12)
    def test_ano(self):
        ''' Test sequence for '5, 12, 2021' '''
        data = self.unit.Data(5, 12, 2021)
        self.assertEqual(data.ano(), 2021)
    def test_anterior(self):
        ''' Test sequence for '5, 12, 2021' '''
        data = self.unit.Data(5, 12, 2021)
        self.assertTrue(data.anterior(self.unit.Data(6, 12, 2021)))
    def test_leading(self):
        ''' Test sequence for '5, 1, 22' '''
        data = self.unit.Data(5, 1, 22)
        self.assertEqual(repr(data), "05/01/0022")
    def test_era(self):
        ''' Test sequence for '5, 1, -22' '''
        data = self.unit.Data(5, 1, -22)
        self.assertEqual(repr(data), "05/01/0022 AC")
    def test_idade_20(self):
        ''' Test sequence for '5, 1, 2022' '''
        data = self.unit.Data(5, 1, 2022)
        self.assertEqual(20, data.idade(self.unit.Data(2, 1, 2002)))
    def test_idade_19(self):
        ''' Test sequence for '5, 1, 2022' '''
        data = self.unit.Data(5, 1, 2022)
        self.assertEqual(19, data.idade(self.unit.Data(6, 1, 2002)))
    def test_no_idade(self):
        ''' Test sequence for '5, 1, 2022' '''
        data = self.unit.Data(5, 1, 2022)
        data2 = self.unit.Data(6, 1, 2022)
        self.assertRaises(ValueError, data.idade, data2)
    def test_mesma(self):
        ''' Test sequence for '5, 12, 2021' '''
        data = self.unit.Data(5, 12, 2021)
        self.assertTrue(data.mesma(self.unit.Data(5, 12, 2021)))
    def test_not_mesma(self):
        ''' Test sequence for '5, 12, 2021' '''
        data = self.unit.Data(5, 12, 2021)
        self.assertFalse(data.mesma(self.unit.Data(6, 12, 2021)))

if __name__ == '__main__':
    unittest.main()
