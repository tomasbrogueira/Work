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
        ''' Test sequence for '[1]' '''
        self.assertEqual(self.unit.l_nomes[1],
            {'nome': {'nomep': 'John', 'apelido': 'Doe'},
            'morada': {'rua': 'West Hazeltine Ave.', 'num': 57,
            'andar': '', 'localidade': 'Kenmore', 'estado': 'NY',
            'cp': '14317', 'pais': 'USA'}})
    def test_2(self):
        ''' Test sequence for '['nome']' '''
        self.assertEqual(self.unit.l_nomes[1]['nome'], {'nomep': 'John', 'apelido': 'Doe'})
    def test_3(self):
        ''' Test sequence for '['apelido']' '''
        self.assertEqual(self.unit.l_nomes[1]['nome']['apelido'], 'Doe')
    def test_4(self):
        ''' Test sequence for '['apelido'][0]' '''
        self.assertEqual(self.unit.l_nomes[1]['nome']['apelido'][0], 'D')
if __name__ == '__main__':
    unittest.main()
