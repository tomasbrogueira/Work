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
        with open("ex02.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '[2, 5, 90], [3, 5, 6, 12]' '''
        self.assertEqual(self.unit.junta_ordenados([2, 5, 90], [3, 5, 6, 12]),
            [2, 3, 5, 5, 6, 12, 90])
    def test_2(self):
        ''' Test sequence for '[2, 5, 9], [13, 15, 16, 22]' '''
        self.assertEqual(self.unit.junta_ordenados([2, 5, 9], [13, 15, 16, 22]),
            [2, 5, 9, 13, 15, 16, 22])
    def test_3(self):
        ''' Test sequence for '[82, 85, 90], [3, 5, 6, 12]' '''
        self.assertEqual(self.unit.junta_ordenados([82, 85, 90], [3, 5, 6, 12]),
            [3, 5, 6, 12, 82, 85, 90])
    def test_4(self):
        ''' Test sequence for '[], [3, 5, 6, 12]' '''
        self.assertEqual(self.unit.junta_ordenados([], [3, 5, 6, 12]), [3, 5, 6, 12])
    def test_5(self):
        ''' Test sequence for '[2, 5, 90], []' '''
        self.assertEqual(self.unit.junta_ordenados([2, 5, 90], []), [2, 5, 90])
    def test_6(self):
        ''' Test sequence for '[], []' '''
        self.assertEqual(self.unit.junta_ordenados([], []), [])
if __name__ == '__main__':
    unittest.main()
