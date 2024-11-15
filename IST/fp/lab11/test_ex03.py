#! /usr/bin/env python3
''' tests for ex03.py '''
import unittest
SKIP = False
try :
    import ex03
except ImportError:
    SKIP = True
class TestEx03(unittest.TestCase):
    ''' test class for ex03.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex03.py")
        self.unit = ex03
    def test_1(self):
        ''' Test sequence for '.soma_fn()' com 'x*x' '''
        self.assertEqual(self.unit.soma_fn(4, lambda x: x * x), 30)
    def test_2(self):
        ''' Test sequence for '.soma_fn' com 'x*1' '''
        self.assertEqual(self.unit.soma_fn(4, lambda x: x * 1), 10)
    def test_3(self):
        ''' Test sequence for '.soma_fn_for' com 'x*x' '''
        self.assertEqual(self.unit.soma_fn_for(4, lambda x: x * x), 30)
    def test_4(self):
        ''' Test sequence for '.soma_fn_for' com 'x*1' '''
        self.assertEqual(self.unit.soma_fn_for(4, lambda x: x * 1), 10)
if __name__ == '__main__':
    unittest.main()
