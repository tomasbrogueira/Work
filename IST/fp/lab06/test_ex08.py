#! /usr/bin/env python3
''' tests for ex08.py '''
import unittest
SKIP = False
try :
    import ex08
except ImportError:
    SKIP = True
class TestEx08(unittest.TestCase):
    ''' test class for ex08.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex08.py")
        self.unit = ex08
    def test_1(self):
        ''' Test sequence for '[1, 2, 3, 4, 3], 3' '''
        self.assertEqual(self.unit.num_occ_lista([1, 2, 3, 4, 3], 3), 2)
    def test_2(self):
        ''' Test sequence for '[1, [[[1]], 2], [[[2]]], 2], 2' '''
        self.assertEqual(self.unit.num_occ_lista([1, [[[1]], 2], [[[2]]], 2], 2), 3)
if __name__ == '__main__':
    unittest.main()
