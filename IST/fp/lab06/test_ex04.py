#! /usr/bin/env python3
''' tests for ex04.py '''
import unittest
import sys
from io import StringIO
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
        sys.stdout = StringIO()
        self.stdout = sys.stdout
        self.unit = ex04
    def tearDown(self):
        sys.stdout = self.stdout
    def test_1(self):
        ''' Test sequence for '[[1, 2, 3], [4, 5, 6]]' '''
        self.unit.print_matriz([[1, 2, 3], [4, 5, 6]])
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), "1 2 3\n4 5 6\n")
    def test_2(self):
        ''' Test sequence for '[[1, 2], [3, 4], [5, 6]]' '''
        self.unit.print_matriz([[1, 2], [3, 4], [5, 6]])
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), "1 2\n3 4\n5 6\n")
    def test_3(self):
        ''' Test sequence for '[]' '''
        self.unit.print_matriz([])
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), "")
if __name__ == '__main__':
    unittest.main()
