#! /usr/bin/env python3
''' tests for ex20.py '''
import unittest
SKIP = False
try :
    import ex20
except ImportError:
    SKIP = True
class TestEx20(unittest.TestCase):
    ''' test class for ex20.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex20.py")
        self.unit = ex20
    def test_1(self):
        ''' Test sequence for '.ataques_rainhas()' '''
        j = {(1, 'H'): ('branca', 'torre'), (2, 'F'): ('branca', 'peao'),
        (2, 'G'): ('branca', 'rei'), (6, 'F'): ('branca', 'bispo'),
        (5, 'C'): ('branca', 'rainha'), (6, 'G'): ('preta', 'peao'),
        (7, 'F'): ('preta', 'peao'), (8, 'F'): ('preta', 'torre'),
        (8, 'G'): ('preta', 'rei'), (2, 'C'): ('preta', 'peao')}
        res = [['peao', 'preta', (2, 'C')], ['torre', 'preta', (8, 'F')]]
        self.assertEqual(self.unit.ataques_rainhas(j), res)
if __name__ == '__main__':
    unittest.main()
