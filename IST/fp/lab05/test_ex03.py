#! /usr/bin/env python3
''' tests for ex03.py '''
import unittest
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
    def test_1(self):
        ''' Test sequence for '(3, 4, 0, 0, 4)' '''
        self.assertEqual(self.unit.implode((3, 4, 0, 0, 4)), 34004)
    def test_2(self):
        ''' Test sequence for '(2, 'a', 5)' '''
        self.assertRaises(ValueError, self.unit.implode, (2, 'a', 5))
    def test_3(self):
        ''' Test sequence for '(3, 4, 5, 0, 0)' '''
        self.assertEqual(self.unit.implode((3, 4, 5, 0, 0)), 34500)
if __name__ == '__main__':
    unittest.main()
