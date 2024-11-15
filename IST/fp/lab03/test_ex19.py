#! /usr/bin/env python3
''' tests for ex19.py '''
import unittest
SKIP = False
try :
    import ex19
except ImportError:
    SKIP = True
class TestEx19(unittest.TestCase):
    ''' test class for ex19.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex19.py")
        self.unit = ex19
    def test_18_1_2014(self):
        ''' Test sequence with number 18, 1, 2014 '''
        self.assertEqual(self.unit.dia_da_semana(18,1,2014), 'sábado')
    def test_1_11_1980(self):
        ''' Test sequence with number 1, 11, 1980 '''
        self.assertEqual(self.unit.dia_da_semana(1,11,1980), 'sábado')
    def test_21_10_2021(self):
        ''' Test sequence with number 21, 10, 2021 '''
        self.assertEqual(self.unit.dia_da_semana(21,10,2021), 'quinta')
    def test_14_12_2021(self):
        ''' Test sequence with number 14, 12, 2021 '''
        self.assertEqual(self.unit.dia_da_semana(14,12,2021), 'terça')
    def test_1_1_2022(self):
        ''' Test sequence with number 1, 1, 2022 '''
        self.assertEqual(self.unit.dia_da_semana(1,1,2022), 'sábado')
    def test_9_2_2022(self):
        ''' Test sequence with number 9, 2, 2022 '''
        self.assertEqual(self.unit.dia_da_semana(9,2,2022), 'quarta')
    def test_21_2_2022(self):
        ''' Test sequence with number 21, 2, 2022 '''
        self.assertEqual(self.unit.dia_da_semana(21,2,2022), 'segunda')
if __name__ == '__main__':
    unittest.main()
