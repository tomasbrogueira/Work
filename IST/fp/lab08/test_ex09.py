#! /usr/bin/env python3
''' tests for ex09.py '''
import unittest
SKIP = False
try :
    import ex09
except ImportError:
    SKIP = True
class TestEx09(unittest.TestCase):
    ''' test class for ex09.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex09.py")
        self.unit = ex09
    def test_den(self):
        ''' Test sequence for '.deno()' '''
        rat = self.unit.Racional(2,4)
        self.assertEqual(2, rat.deno())
    def test_num(self):
        ''' Test sequence for '.nume()' '''
        rat = self.unit.Racional(2,4)
        self.assertEqual(1, rat.nume())
    def test_real(self):
        ''' Test sequence for '.real()' '''
        rat = self.unit.Racional(2,4)
        self.assertAlmostEqual(.5, rat.real())
    def test_add(self):
        ''' Test sequence for 'add' '''
        rat = self.unit.Racional(2,4)
        rat2 = self.unit.Racional(1,6)
        rat3 = rat + rat2
        self.assertEqual(2,rat3.nume())
        self.assertEqual(3,rat3.deno())
    def test_mul(self):
        ''' Test sequence for 'mul' '''
        rat = self.unit.Racional(2,4)
        rat2 = self.unit.Racional(1,6)
        rat3 = rat * rat2
        self.assertEqual(1,rat3.nume())
        self.assertEqual(12,rat3.deno())
    def test_eq(self):
        ''' Test sequence for 'eq' '''
        rat = self.unit.Racional(2,4)
        rat2 = self.unit.Racional(4,8)
        self.assertTrue(rat == rat2)
    def test_ne(self):
        ''' Test sequence for ' ' '''
        rat = self.unit.Racional(2,4)
        rat2 = self.unit.Racional(1,6)
        self.assertTrue(rat != rat2)
    def test_repr(self):
        ''' Test sequence for 'ne' '''
        rat = self.unit.Racional(2,4)
        self.assertEqual("1/2", repr(rat))
    def test_no(self):
        ''' Test sequence for 'no' '''
        self.assertRaises(ValueError, self.unit.Racional, 2, 0)

if __name__ == '__main__':
    unittest.main()
