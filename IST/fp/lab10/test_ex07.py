#! /usr/bin/env python3
''' tests for ex07.py '''
import unittest
SKIP = False
try :
    import ex07
except ImportError:
    SKIP = True
class TestEx07(unittest.TestCase):
    ''' test class for ex07.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex07.py")
        self.unit = ex07
        with open("ex07.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '[3, 4, 5], 2' '''
        self.assertFalse(self.unit.pertence([3, 4, 5], 2))
    def test_2(self):
        ''' Test sequence for '[3, 4, 5], 5' '''
        self.assertTrue(self.unit.pertence([3, 4, 5], 5))
if __name__ == '__main__':
    unittest.main()
