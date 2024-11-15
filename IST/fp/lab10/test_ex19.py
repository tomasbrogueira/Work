#! /usr/bin/env python3
''' tests for ex19.py '''
import unittest
SKIP = False
try :
    import ex19
except ImportError:
    SKIP = True
class TestEx19(unittest.TestCase):
    ''' test class for ex19.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex19.py")
        self.unit = ex19
        with open("ex19.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '144' '''
        self.assertEqual(self.unit.soma_divisores(144), 259)
    def test_2(self):
        ''' Test sequence for '12' '''
        self.assertEqual(self.unit.soma_divisores(12), 16)
    def test_3(self):
        ''' Test sequence for '11' '''
        self.assertEqual(self.unit.soma_divisores(11), 1)
    def test_4(self):
        ''' Test sequence for '199' '''
        self.assertEqual(self.unit.soma_divisores(199), 1)
if __name__ == '__main__':
    unittest.main()
