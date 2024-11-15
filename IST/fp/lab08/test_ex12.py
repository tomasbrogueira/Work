#! /usr/bin/env python3
''' tests for ex12.py '''
import unittest
SKIP = False
try :
    import ex12
except ImportError:
    SKIP = True
class TestEx12(unittest.TestCase):
    ''' test class for ex12.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex12.py")
        self.unit = ex12
    def test_exemplo(self):
        ''' Test sequence for '.val(2,3)' '''
        mem = self.unit.Mem()
        self.assertEqual(9, mem.val(2,3))
        out = "{(0, 1): 2,\n (0, 2): 3,\n (0, 3): 4,\n (0, 4): 5,\n (0, 5): 6,\n" \
            " (0, 6): 7,\n (0, 7): 8,\n (0, 8): 9,\n (1, 0): 2,\n (1, 1): 3,\n" \
            " (1, 2): 4,\n (1, 3): 5,\n (1, 4): 6,\n (1, 5): 7,\n (1, 6): 8,\n" \
            " (1, 7): 9,\n (2, 0): 3,\n (2, 1): 5,\n (2, 2): 7,\n (2, 3): 9}"
        self.assertEqual(out, mem.mem())

if __name__ == '__main__':
    unittest.main()
