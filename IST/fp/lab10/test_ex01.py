#! /usr/bin/env python3
''' tests for ex01.py '''
import unittest
SKIP = False
try :
    import ex01
except ImportError:
    SKIP = True
class TestEx01(unittest.TestCase):
    ''' test class for ex01.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex01.py")
        self.unit = ex01
        with open("ex01.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '468' '''
        self.assertEqual(self.unit.apenas_digitos_impares(468), 0)
    def test_2(self):
        ''' Test sequence for '12426374856' '''
        self.assertEqual(self.unit.apenas_digitos_impares(12426374856), 1375)
    def test_3(self):
        ''' Test sequence for '1' '''
        self.assertEqual(self.unit.apenas_digitos_impares(1), 1)
    def test_4(self):
        ''' Test sequence for '13975579' '''
        self.assertEqual(self.unit.apenas_digitos_impares(13975579), 13975579)
    def test_5(self):
        ''' Test sequence for '0' '''
        self.assertEqual(self.unit.apenas_digitos_impares(0), 0)
if __name__ == '__main__':
    unittest.main()
