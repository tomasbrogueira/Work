#! /usr/bin/env python3
''' tests for ex13.py '''
import unittest
SKIP = False
try :
    import ex13
except ImportError:
    SKIP = True
class TestEx13(unittest.TestCase):
    ''' test class for ex13.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex13.py")
        self.unit = ex13
    def test_1(self):
        ''' Test sequence for 'notas_dict' '''
        notas_dict = {1 : [46592, 49212, 90300, 59312],
            15 : [52592, 59212], 20 : [58323]}
        res = self.unit.resumo_fp(notas_dict)
        self.assertEqual(res[1], 4)
        self.assertAlmostEqual(res[0], 50/3)
if __name__ == '__main__':
    unittest.main()
