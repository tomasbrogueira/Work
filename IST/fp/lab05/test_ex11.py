#! /usr/bin/env python3
''' tests for ex11.py '''
import unittest
SKIP = False
try :
    import ex11
except ImportError:
    SKIP = True
class TestEx11(unittest.TestCase):
    ''' test class for ex11.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex11.py")
        self.unit = ex11
    def test_1(self):
        ''' Test sequence for 'bom dia' '''
        self.assertEqual(self.unit.lista_codigos('bom dia'),
            (98, 111, 109, 32, 100, 105, 97))
    def test_2(self):
        ''' Test sequence for 'BOM DIA' '''
        self.assertEqual(self.unit.lista_codigos('BOM DIA'),
            (66, 79, 77, 32, 68, 73, 65))
    def test_3(self):
        ''' Test sequence for 'programação' '''
        self.assertEqual(self.unit.lista_codigos('programação'),
            (112, 114, 111, 103, 114, 97, 109, 97, 231, 227, 111))
    def test_4(self):
        ''' Test sequence for '' '''
        self.assertEqual(self.unit.lista_codigos(''), ())
if __name__ == '__main__':
    unittest.main()
