#! /usr/bin/env python3
''' tests for ex15.py '''
import unittest
SKIP = False
try :
    import ex15
except ImportError:
    SKIP = True
class TestEx15(unittest.TestCase):
    ''' test class for ex15.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex15.py")
        self.unit = ex15
    def test_1(self):
        ''' Test sequence for 'aranha' '''
        txt = 'a aranha arranha a ra a ra arranha a aranha ' \
        + 'nem a aranha arranha a ra nem a ra arranha a aranha'
        self.assertEqual(self.unit.conta_palavras(txt),
        {'aranha': 4, 'arranha': 4, 'ra': 4, 'a': 8, 'nem': 2})
if __name__ == '__main__':
    unittest.main()
