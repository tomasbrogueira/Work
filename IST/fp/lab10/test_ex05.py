#! /usr/bin/env python3
''' tests for ex05.py '''
import unittest
SKIP = False
try :
    import ex05
except ImportError:
    SKIP = True
class TestEx05(unittest.TestCase):
    ''' test class for ex05.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex05.py")
        self.unit = ex05
        with open("ex05.py",encoding="utf8") as file:
            data = file.read()
            self.assertNotIn('for', data, "for: cannot iterate")
            self.assertNotIn('while', data, "while: cannot iterate")
    def test_1(self):
        ''' Test sequence for '(3, ((((((6, (7, ))), ), ), ), ), 2, 1)' '''
        self.assertEqual(self.unit.soma_els_atomicos((3, ((((((6, (7, ))), ), ), ), ), 2, 1)), 19)
    def test_2(self):
        ''' Test sequence for '((((),),),)' '''
        self.assertEqual(self.unit.soma_els_atomicos(((((),),),)), 0)
    def test_3(self):
        ''' Test sequence for '(1,2,3,4,5,6,7,8,9)' '''
        self.assertEqual(self.unit.soma_els_atomicos((1,2,3,4,5,6,7,8,9)), 45)
    def test_4(self):
        ''' Test sequence for '(((((((((12,)))))))))' '''
        self.assertEqual(self.unit.soma_els_atomicos((((((((((12,)))))))))), 12)
if __name__ == '__main__':
    unittest.main()
