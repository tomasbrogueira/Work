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
        with open("ex03.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '[[1], 2, [3]]' '''
        self.assertEqual(self.unit.sublistas([[1], 2, [3]]), 2)
    def test_2(self):
        ''' Test sequence for '[[[[[1]]]]]' '''
        self.assertEqual(self.unit.sublistas([[[[[1]]]]]), 4)
    def test_3(self):
        ''' Test sequence for '['a', [2, 3, [[[1]], 6, 7], 'b']]' '''
        self.assertEqual(self.unit.sublistas(['a', [2, 3, [[[1]], 6, 7], 'b']]), 4)
    def test_4(self):
        ''' Test sequence for '[1, 2, 3]' '''
        self.assertEqual(self.unit.sublistas([1, 2, 3]), 0)
    def test_5(self):
        ''' Test sequence for '[]' '''
        self.assertEqual(self.unit.sublistas([]), 0)
if __name__ == '__main__':
    unittest.main()
