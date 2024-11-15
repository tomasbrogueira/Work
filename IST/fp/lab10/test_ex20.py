#! /usr/bin/env python3
''' tests for ex20.py '''
import unittest
SKIP = False
try :
    import ex20
except ImportError:
    SKIP = True
class TestEx20(unittest.TestCase):
    ''' test class for ex20.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex20.py")
        self.unit = ex20
        with open("ex20.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '6' '''
        self.assertTrue(self.unit.perfeito(6))
    def test_2(self):
        ''' Test sequence for '28' '''
        self.assertTrue(self.unit.perfeito(28))
    def test_3(self):
        ''' Test sequence for '2' '''
        self.assertFalse(self.unit.perfeito(2))
    def test_4(self):
        ''' Test sequence for '12' '''
        self.assertFalse(self.unit.perfeito(12))
    def test_5(self):
        ''' Test sequence for '17' '''
        self.assertFalse(self.unit.perfeito(17))
    def test_6(self):
        ''' Test sequence for '6, 30' '''
        self.assertEqual(self.unit.perfeitos_entre(6, 30), [6, 28])
if __name__ == '__main__':
    unittest.main()
