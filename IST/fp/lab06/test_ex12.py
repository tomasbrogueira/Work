#! /usr/bin/env python3
''' tests for ex12.py '''
import unittest
b = [{'np': 'espadas', 'vlr': 'A'}, {'np': 'espadas', 'vlr': '2'},
    {'np': 'espadas', 'vlr': '3'}, {'np': 'espadas', 'vlr': '4'},
    {'np': 'espadas', 'vlr': '5'}, {'np': 'espadas', 'vlr': '6'},
    {'np': 'espadas', 'vlr': '7'}, {'np': 'espadas', 'vlr': '8'},
    {'np': 'espadas', 'vlr': '9'}, {'np': 'espadas', 'vlr': '10'},
    {'np': 'espadas', 'vlr': 'J'}, {'np': 'espadas', 'vlr': 'Q'},
    {'np': 'espadas', 'vlr': 'K'}, {'np': 'copas', 'vlr': 'A'},
    {'np': 'copas', 'vlr': '2'}, {'np': 'copas', 'vlr': '3'},
    {'np': 'copas', 'vlr': '4'}, {'np': 'copas', 'vlr': '5'},
    {'np': 'copas', 'vlr': '6'}, {'np': 'copas', 'vlr': '7'},
    {'np': 'copas', 'vlr': '8'}, {'np': 'copas', 'vlr': '9'},
    {'np': 'copas', 'vlr': '10'}, {'np': 'copas', 'vlr': 'J'},
    {'np': 'copas', 'vlr': 'Q'}, {'np': 'copas', 'vlr': 'K'},
    {'np': 'ouros', 'vlr': 'A'}, {'np': 'ouros', 'vlr': '2'},
    {'np': 'ouros', 'vlr': '3'}, {'np': 'ouros', 'vlr': '4'},
    {'np': 'ouros', 'vlr': '5'}, {'np': 'ouros', 'vlr': '6'},
    {'np': 'ouros', 'vlr': '7'}, {'np': 'ouros', 'vlr': '8'},
    {'np': 'ouros', 'vlr': '9'}, {'np': 'ouros', 'vlr': '10'},
    {'np': 'ouros', 'vlr': 'J'}, {'np': 'ouros', 'vlr': 'Q'},
    {'np': 'ouros', 'vlr': 'K'}, {'np': 'paus', 'vlr': 'A'},
    {'np': 'paus', 'vlr': '2'}, {'np': 'paus', 'vlr': '3'},
    {'np': 'paus', 'vlr': '4'}, {'np': 'paus', 'vlr': '5'},
    {'np': 'paus', 'vlr': '6'}, {'np': 'paus', 'vlr': '7'},
    {'np': 'paus', 'vlr': '8'}, {'np': 'paus', 'vlr': '9'},
    {'np': 'paus', 'vlr': '10'}, {'np': 'paus', 'vlr': 'J'},
    {'np': 'paus', 'vlr': 'Q'}, {'np': 'paus', 'vlr': 'K'}]
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
    def test_1(self):
        ''' Test sequence for '.baralho()' '''
        self.assertEqual(self.unit.baralho(), b)
    def test_2(self):
        ''' Test sequence for '.distribui()' '''
        dist = self.unit.distribui(b.copy())
        self.assertEqual(len(dist), 4)
        for i in dist:
            self.assertEqual(len(i), 13)
        for i in b:
            self.assertTrue(i in dist[0] or i in dist[1] or i in dist[2] or i in dist[3])
    def test_3(self):
        ''' Test sequence for '.baralha()' '''
        shuffle = self.unit.baralha(b.copy())
        self.assertEqual(len(shuffle), len(b))
        for i in b:
            self.assertIn(i, shuffle)
if __name__ == '__main__':
    unittest.main()
