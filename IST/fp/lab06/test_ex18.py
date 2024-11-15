#! /usr/bin/env python3
''' tests for ex18.py '''
import unittest
SKIP = False
try :
    import ex18
except ImportError:
    SKIP = True
class TestEx18(unittest.TestCase):
    ''' test class for ex18.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex18.py")
        self.unit = ex18
    def test_1(self):
        ''' Test sequence for 'G. Arroz' '''
        bib = [{'autores': ['G. Arroz', 'J. Monteiro', 'A. Oliveira'],
    'titulo': 'Arquitectura de computadores', 'editor': 'IST Press',
    'cidade': 'Lisboa', 'ano': 2007, 'numpags': 799,
    'isbn': '978-972-8469-54-2'}, {'autores': ['J.P. Martins'],
    'titulo': 'Logica e Raciocinio', 'editor': 'College Publications',
    'cidade': 'Londres', 'ano': 2014, 'numpags': 438,
    'isbn': '978-1-84890-125-4'}]
        self.assertEqual(self.unit.mais_antigo(bib), 'Arquitectura de computadores')
if __name__ == '__main__':
    unittest.main()
