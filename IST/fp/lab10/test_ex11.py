#! /usr/bin/env python3
''' tests for ex11.py '''
import unittest
SKIP = False
try :
    import ex11
except ImportError:
    SKIP = True
class TestEx11(unittest.TestCase):
    ''' test class for ex11.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex11.py")
        self.unit = ex11
        with open("ex11.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '2,3' '''
        self.assertEqual(self.unit.misterio(2,3), 12)
    def test_2(self):
        ''' Test sequence for '3,2' '''
        self.assertEqual(self.unit.misterio(3,2), 9)
    def test_3(self):
        ''' Test sequence for '0,6' '''
        self.assertEqual(self.unit.misterio(0,6), 0)
    def test_4(self):
        ''' Test sequence for '16,0' '''
        self.assertEqual(self.unit.misterio(16,0), 0)
    def test_5(self):
        ''' Test sequence for '16,2' '''
        self.assertEqual(self.unit.misterio(16,2), 48)
if __name__ == '__main__':
    unittest.main()
