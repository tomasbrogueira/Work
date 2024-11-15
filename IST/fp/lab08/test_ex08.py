#! /usr/bin/env python3
''' tests for ex08.py '''
import unittest
import importlib.util
from os.path import exists
class TestEx08(unittest.TestCase):
    ''' test class for ex08.py '''
    def setUp(self) :
        if not exists('ex08.py'):
            self.skipTest("no ex08.py")
        self.spec = importlib.util.spec_from_file_location('__main__', 'ex08.py')
        self.unit = importlib.util.module_from_spec(self.spec)
        self.spec.loader.exec_module(self.unit)
    def test_nome(self):
        ''' Test sequence for '.nome()' '''
        id_ = self.unit.Id('Ana')
        self.assertEqual('Ana', id_.nome())
    def test_ident(self):
        ''' Test sequence for '.ident()' '''
        id_ = self.unit.Id('Ana')
        self.assertEqual(1, id_.ident())
    def test_str(self):
        ''' Test sequence for 'str(id)' '''
        id_ = self.unit.Id('Ana')
        self.assertEqual('1: Ana', str(id_))
    def test_ultimo(self):
        ''' Test sequence for '.ultimo()' '''
        self.unit.Id('Ana')
        self.assertEqual(1, self.unit.Id.ultimo())
    def test_procura(self):
        ''' Test sequence for '.procura()' '''
        self.unit.Id('Ana')
        self.unit.Id('Beatriz')
        self.unit.Id('Carlos')
        self.assertEqual(2, self.unit.Id.procura('Beatriz'))
    def test_id(self):
        ''' Test sequence for '.ids()' '''
        self.unit.Id('Ana')
        id_ = self.unit.Id('Beatriz')
        self.unit.Id('Carlos')
        self.assertEqual(id_, self.unit.Id.ids(2))
    def test_index(self):
        ''' Test sequence for '.ids() error' '''
        self.unit.Id('Ana')
        self.assertRaises(IndexError, self.unit.Id.ids, 2)

if __name__ == '__main__':
    unittest.main()
