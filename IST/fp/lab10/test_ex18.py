#! /usr/bin/env python3
''' tests for ex18.py '''
import unittest
SKIP = False
try :
    import ex18
except ImportError:
    SKIP = True
class TestEx18(unittest.TestCase):
    ''' test class for ex18.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex18.py")
        self.unit = ex18
        with open("ex18.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '6' '''
        self.assertEqual(self.unit.maior_inteiro(6), 3)
    def test_2(self):
        ''' Test sequence for '20' '''
        self.assertEqual(self.unit.maior_inteiro(20), 5)
    def test_3(self):
        ''' Test sequence for '100' '''
        self.assertEqual(self.unit.maior_inteiro(100), 13)
    def test_4(self):
        ''' Test sequence for '2000' '''
        self.assertEqual(self.unit.maior_inteiro(2000), 62)
    def test_5(self):
        ''' Test sequence for '2' '''
        self.assertEqual(self.unit.maior_inteiro(2), 1)
if __name__ == '__main__':
    unittest.main()
