#! /usr/bin/env python3
''' tests for ex02.py '''
import unittest
SKIP = False
try :
    import ex02
except (ModuleNotFoundError, SyntaxError):
    SKIP = True
class TestEx02(unittest.TestCase):
    ''' test class for ex02.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex02.py")
        self.unit = ex02
    def test_1(self):
        ''' Test sequence for '34500' '''
        self.assertEqual(self.unit.explode(34500), (3, 4, 5, 0, 0))
    def test_2(self):
        ''' Test sequence for '3.5' '''
        self.assertRaises(ValueError, self.unit.explode, 3.5)
if __name__ == '__main__':
    unittest.main()
