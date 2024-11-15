#! /usr/bin/env python3
''' tests for ex14.py '''
import unittest
SKIP = False
try :
    import ex14
except ImportError:
    SKIP = True
class TestEx14(unittest.TestCase):
    ''' test class for ex14.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex14.py")
        self.unit = ex14
    def test_1(self):
        ''' Test sequence for '.metanolismo()' '''
        dic = {'Maria' : ('F', 34, 1.65, 64),
            'Pedro': ('M', 34, 1.65, 64),
            'Ana': ('F', 54, 1.65, 120),
            'Hugo': ('M', 12, 1.82, 75)}
        res = {'Ana': 1432.555, 'Hugo': 643.578,
            'Maria': 1097.755, 'Pedro': 721.685}
        self.assertEqual(self.unit.metabolismo(dic), res)
if __name__ == '__main__':
    unittest.main()
