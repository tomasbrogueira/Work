#! /usr/bin/env python3
''' tests for ex20.py '''
import unittest
SKIP = False
try :
    import ex20
except ImportError:
    SKIP = True
class TestEx20(unittest.TestCase):
    ''' test class for ex20.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex20.py")
        self.unit = ex20
    def test_246(self):
        ''' Test sequence with number 246 '''
        self.assertEqual(self.unit.misterio(246), 1089)
    def test_131(self):
        ''' Test sequence with number 131 '''
        self.assertRaises(ValueError, self.unit.misterio, 131)
if __name__ == '__main__':
    unittest.main()
