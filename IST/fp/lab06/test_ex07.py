#! /usr/bin/env python3
''' tests for ex07.py '''
import unittest
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
    def test_1(self):
        ''' Test sequence for '1' '''
        self.assertEqual(self.unit.seq_racaman(1), [0])
    def test_2(self):
        ''' Test sequence for '2' '''
        self.assertEqual(self.unit.seq_racaman(2), [0, 1])
    def test_3(self):
        ''' Test sequence for '3' '''
        self.assertEqual(self.unit.seq_racaman(3), [0, 1, 3])
    def test_4(self):
        ''' Test sequence for '15' '''
        res = [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11, 22, 10, 23, 9]
        self.assertEqual(self.unit.seq_racaman(15), res)
if __name__ == '__main__':
    unittest.main()
