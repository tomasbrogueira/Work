#! /usr/bin/env python3
''' tests for ex17.py '''
import unittest
SKIP = False
try :
    import ex17
except ImportError:
    SKIP = True
class TestEx17(unittest.TestCase):
    ''' test class for ex17.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex17.py")
        self.unit = ex17
    def test_jan2017(self):
        ''' Test sequence with jan 2017 '''
        self.assertEqual(self.unit.dias_mes('jan', 2017), 31)
    def test_fev2016(self):
        ''' Test sequence with fev 2016 '''
        self.assertEqual(self.unit.dias_mes('fev', 2016), 29)
    def test_caps(self):
        ''' Test sequence with MAR 2017 '''
        self.assertRaises(ValueError, self.unit.dias_mes, 'MAR', 2017)
    def test_fev2020(self):
        ''' Test sequence with fev 2020 '''
        self.assertEqual(self.unit.dias_mes('fev', 2020), 29)
    def test_fev2022(self):
        ''' Test sequence with fev 2022 '''
        self.assertEqual(self.unit.dias_mes('fev', 2022), 28)
    def test_fev2023(self):
        ''' Test sequence with fev 2023 '''
        self.assertEqual(self.unit.dias_mes('fev', 2023), 28)
    def test_fev2024(self):
        ''' Test sequence with fev 2024 '''
        self.assertEqual(self.unit.dias_mes('fev', 2024), 29)
    def test_jul2021(self):
        ''' Test sequence with jul 2021 '''
        self.assertEqual(self.unit.dias_mes('jul', 2021), 31)
    def test_nov2021(self):
        ''' Test sequence with nov 2021 '''
        self.assertEqual(self.unit.dias_mes('nov', 2021), 30)
if __name__ == '__main__':
    unittest.main()
