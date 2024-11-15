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
    def test_1(self):
        ''' Test sequence for 'amigas', 'amigas' '''
        self.assertTrue(self.unit.amigas('amigas', 'amigas'))
    def test_2(self):
        ''' Test sequence for 'amigas', 'asigos' '''
        self.assertFalse(self.unit.amigas('amigas', 'asigos'))
    def test_3(self):
        ''' Test sequence for ''australopitecos', 'australopitecus' '''
        self.assertTrue(self.unit.amigas('australopitecos', 'australopitecus'))
if __name__ == '__main__':
    unittest.main()
