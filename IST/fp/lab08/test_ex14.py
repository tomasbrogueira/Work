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
    def test_mesmo(self):
        ''' Test sequence for 'id()' iguais '''
        one = self.unit.Unica.get_instance()
        other = self.unit.Unica.get_instance()
        self.assertEqual(id(one), id(other))
    def test_valor(self):
        ''' Test sequence for '.store()' '''
        one = self.unit.Unica.get_instance()
        one.store(56)
        other = self.unit.Unica.get_instance()
        self.assertEqual(56, other.value())
    def test_other(self):
        ''' Test sequence for 'construtor' '''
        self.unit.Unica.get_instance()
        self.assertRaises(Exception, self.unit.Unica)

if __name__ == '__main__':
    unittest.main()
