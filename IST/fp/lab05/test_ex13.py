#! /usr/bin/env python3
''' tests for ex13.py '''
import unittest
SKIP = False
try :
    import ex13
except ImportError:
    SKIP = True
class TestEx13(unittest.TestCase):
    ''' test class for ex13.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex13.py")
        self.unit = ex13
    def test_1(self):
        ''' Test sequence for 'banana', 'a' '''
        self.assertEqual(self.unit.apaga_char('banana', 'a'), 'bnn')
    def test_2(self):
        ''' Test sequence for 'banana', 'n' '''
        self.assertEqual(self.unit.apaga_char('banana', 'n'), 'baaa')
    def test_3(self):
        ''' Test sequence for 'banana', 'b' '''
        self.assertEqual(self.unit.apaga_char('banana', 'b'), 'anana')
    def test_4(self):
        ''' Test sequence for 'banana', 'x' '''
        self.assertEqual(self.unit.apaga_char('banana', 'x'), 'banana')
    def test_5(self):
        ''' Test sequence for '', 'a' '''
        self.assertEqual(self.unit.apaga_char('', 'a'), '')
if __name__ == '__main__':
    unittest.main()
