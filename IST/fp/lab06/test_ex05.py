#! /usr/bin/env python3
''' tests for ex05.py '''
import unittest
SKIP = False
try :
    import ex05
except ImportError:
    SKIP = True
class TestEx05(unittest.TestCase):
    ''' test class for ex05.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex05.py")
        self.unit = ex05
    def test_1(self):
        ''' Test sequence for 'mat + mat' '''
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.unit.soma_mat(mat, mat), [[2,4,6],[8,10,12],[14,16,18]])
    def test_2(self):
        ''' Test sequence for 'mat1 + mat2' '''
        mat1 = [[1, 2, 3], [4, 5, 6]]
        mat2 = [[0, -1, -2], [6, 5, 4]]
        self.assertEqual(self.unit.soma_mat(mat1, mat2), [[1,1,1],[10,10,10]])
if __name__ == '__main__':
    unittest.main()
