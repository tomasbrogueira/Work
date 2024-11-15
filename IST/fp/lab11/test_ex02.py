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
        ''' Test sequence for '1, 5' com 'x+1' '''
        self.assertEqual(self.unit.piatorio(1, 5, lambda x : x, lambda x : x + 1), 120)
    def test_2(self):
        ''' Test sequence for '1, 5' com 'x+2' '''
        self.assertEqual(self.unit.piatorio(1, 5, lambda x : x, lambda x : x + 2), 15)
    def test_3(self):
        ''' Test sequence for '1, 12' com 'x+3' '''
        self.assertEqual(self.unit.piatorio(1, 12, lambda x : x, lambda x : x + 3), 280)
    def test_4(self):
        ''' Test sequence for '1, 12' com 'x+1' '''
        self.assertEqual(self.unit.piatorio(1, 12, lambda x : x + 1, lambda x : x + 3), 880)
    def test_5(self):
        ''' Test sequence for '.fatorial()' '''
        self.assertEqual(self.unit.fatorial(5), 120)
if __name__ == '__main__':
    unittest.main()
