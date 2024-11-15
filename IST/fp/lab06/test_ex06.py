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
        ''' Test sequence for 'mat * mat' '''
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(self.unit.multiplica_mat(mat, mat),
            [[30, 36, 42], [66, 81, 96], [102, 126, 150]])
    def test_2(self):
        ''' Test sequence for '2x3 * 3x2' '''
        mat1 = [[1, 2, 3], [4, 5, 6]]
        mat2 = [[0, -1], [-2, 6], [5, 4]]
        self.assertEqual(self.unit.multiplica_mat(mat1, mat2), [[11, 23], [20 ,50]])
    def test_3(self):
        ''' Test sequence for '2x3 * 3x2' '''
        mat1 = [[0, -1], [-2, 6], [5, 4]]
        mat2 = [[1, 2, 3], [4, 5, 6]]
        res = [[-4, -5, -6], [22, 26, 30], [21, 30, 39]]
        self.assertEqual(self.unit.multiplica_mat(mat1, mat2), res)
    def test_4(self):
        ''' Test sequence for '3x3 * ident' '''
        mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        mat2 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.assertEqual(self.unit.multiplica_mat(mat1, mat2), mat1)
    def test_5(self):
        ''' Test sequence for '3x3 * 3x3 real' '''
        mat = [[0.1, 2.4, -1.8], [-2.7, 0.9, 0.6], [5.1, 4.4, 8.1]]
        prod = self.unit.multiplica_mat(mat, mat)
        res = [[-15.65, -5.52, -13.32], [0.36, -3.03, 10.26], [29.94, 51.84, 59.07]]
        self.assertEqual(len(res), len(prod))
        lines = len(res)
        for i in range(lines):
            self.assertEqual(len(res[i]), len(prod[i]))
            cols = len(res[i])
            for j in range(cols):
                self.assertAlmostEqual(res[i][j], prod[i][j])
    def test_6(self):
        ''' Test sequence for '2x3 * 2x3' '''
        mat = [[1, 2, 3], [4, 5, 6]]
        self.assertRaises(ValueError, self.unit.multiplica_mat, mat, mat)
    def test_7(self):
        ''' Test sequence for '3x2 2x5' '''
        mat1 = [[0, -1], [-2, 6], [5, 4]]
        mat2 = [[1, 2, 3, 2, 1], [4, 5, 6, 5, 4]]
        res = [[-4, -5, -6, -5, -4], [22, 26, 30, 26, 22], [21, 30, 39, 30, 21]]
        self.assertEqual(self.unit.multiplica_mat(mat1, mat2), res)
if __name__ == '__main__':
    unittest.main()
