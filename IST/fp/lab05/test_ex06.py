#! /usr/bin/env python3
''' tests for ex06.py '''
import unittest
SKIP = False
try :
    import ex06
except ImportError:
    SKIP = True
class TestEx06(unittest.TestCase):
    ''' test class for ex06.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex06.py")
        self.unit = ex06
    def test_1(self):
        ''' Test sequence for '1234567890' '''
        self.assertEqual(self.unit.num_para_seq_cod(1234567890), (9, 4, 1, 6, 3, 8, 5, 0, 7, 2))
if __name__ == '__main__':
    unittest.main()
