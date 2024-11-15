#! /usr/bin/env python3
''' tests for ex02.py '''
import unittest
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
    def test_1(self):
        ''' Test sequence for '[1]*5)' '''
        self.assertEqual(self.unit.soma_cumulativa([1]*5), [1, 2, 3, 4, 5])
    def test_2(self):
        ''' Test sequence for '[1, 2, 3, 4, 5]' '''
        self.assertEqual(self.unit.soma_cumulativa([1, 2, 3, 4, 5]), [1, 3, 6, 10, 15])
    def test_3(self):
        ''' Test sequence for '[]' '''
        self.assertEqual(self.unit.soma_cumulativa([]), [])
    def test_4(self):
        ''' Test sequence for '[1]' '''
        self.assertEqual(self.unit.soma_cumulativa([1]), [1])
    def test_5(self):
        ''' Test sequence for '[1, -5]' '''
        self.assertEqual(self.unit.soma_cumulativa([1, -5]), [1, -4])
    def test_6(self):
        ''' Test sequence for '[1, 12, 3, 41, 5]' '''
        self.assertEqual(self.unit.soma_cumulativa([1, 12, 3, 41, 5]), [1, 13, 16, 57, 62])
if __name__ == '__main__':
    unittest.main()
