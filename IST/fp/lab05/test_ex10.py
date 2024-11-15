#! /usr/bin/env python3
''' tests for ex10.py '''
import unittest
SKIP = False
try :
    import ex10
except ImportError:
    SKIP = True
class TestEx10(unittest.TestCase):
    ''' test class for ex10.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex10.py")
        self.unit = ex10
    def test_1(self):
        ''' Test sequence for 'abcde' '''
        self.assertEqual(self.unit.codifica('abcde'), 'acebd')
    def test_2(self):
        ''' Test sequence for 'código secreto' '''
        self.assertEqual(self.unit.codifica('código secreto'), 'cdg ertóiosceo')
    def test_3(self):
        ''' Test sequence for 'cdg ertóiosceo' '''
        self.assertEqual(self.unit.descodifica('cdg ertóiosceo'), 'código secreto')
    def test_4(self):
        ''' Test sequence for 'acebd' '''
        self.assertEqual(self.unit.descodifica('acebd'), 'abcde')
    def test_5(self):
        ''' Test sequence for 'Nada se perde tudo se transforma' '''
        txt = "Nada se perde tudo se transforma"
        cod = self.unit.codifica(txt)
        self.assertEqual(self.unit.descodifica(cod), txt)
if __name__ == '__main__':
    unittest.main()
