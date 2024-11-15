#! /usr/bin/env python3
''' tests for ex04.py '''
import unittest
SKIP = False
try :
    import ex04
except ImportError:
    SKIP = True
class TestEx04(unittest.TestCase):
    ''' test class for ex04.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex04.py")
        self.unit = ex04
        with open("ex04.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '3, 2, 5' '''
        self.assertEqual(self.unit.soma_n_vezes(3, 2, 5), 17)
    def test_2(self):
        ''' Test sequence for '100, 1, 10' '''
        self.assertEqual(self.unit.soma_n_vezes(100, 1, 10), 1001)
    def test_3(self):
        ''' Test sequence for '1, 100, 10' '''
        self.assertEqual(self.unit.soma_n_vezes(1, 100, 10), 110)
    def test_4(self):
        ''' Test sequence for '2, 1000, 500' '''
        self.assertEqual(self.unit.soma_n_vezes(2, 1000, 500), 2000)
if __name__ == '__main__':
    unittest.main()
