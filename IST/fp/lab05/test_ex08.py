#! /usr/bin/env python3
''' tests for ex08.py '''
import unittest
SKIP = False
try :
    import ex08
except ImportError:
    SKIP = True
class TestEx08(unittest.TestCase):
    ''' test class for ex08.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex08.py")
        self.unit = ex08
    def test_1(self):
        ''' Test sequence for '(2, 34, 200, 210), (1, 23)' '''
        self.assertEqual(self.unit.junta_ordenados((2, 34, 200, 210), (1, 23)),
            (1, 2, 23, 34, 200, 210))
    def test_2(self):
        ''' Test sequence for '(), (1, 23)' '''
        self.assertEqual(self.unit.junta_ordenados((), (1, 23)), (1, 23))
    def test_3(self):
        ''' Test sequence for '(2, 34, 200, 210), ()' '''
        self.assertEqual(self.unit.junta_ordenados((2, 34, 200, 210), ()),
            (2, 34, 200, 210))
    def test_4(self):
        ''' Test sequence for '(2, 34, 200, 210), (1, 23, 34, 200, 210)' '''
        self.assertEqual(self.unit.junta_ordenados((2, 34, 200, 210),
            (1, 23, 34, 200, 210)), (1, 2, 23, 34, 34, 200, 200, 210, 210))
if __name__ == '__main__':
    unittest.main()
