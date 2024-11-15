#! /usr/bin/env python3
''' tests for ex16.py '''
import unittest
import sys
from io import StringIO
SKIP = False
try :
    import ex16
except ImportError:
    SKIP = True
class TestEx16(unittest.TestCase):
    ''' test class for ex16.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex16.py")
        sys.stdout = StringIO()
        self.stdout = sys.stdout
        self.unit = ex16
    def tearDown(self):
        sys.stdout = self.stdout
    def test_1(self):
        ''' Test sequence for 'arranha' '''
        dic = {'aranha': 4, 'arranha': 4, 'ra': 4, 'a': 8, 'nem': 2}
        res = "a 8\naranha 4\narranha 4\nnem 2\nra 4\n"
        self.unit.mostra_ordenado(dic)
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), res)
if __name__ == '__main__':
    unittest.main()
