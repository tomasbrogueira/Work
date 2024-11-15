#! /usr/bin/env python3
''' tests for ex01.bnf '''
from os.path import exists
import unittest
from bnf import grammar, parse
class TestEx01(unittest.TestCase):
    ''' test class for ex01.bnf '''
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self._gram = None
        self._start = None
    def setUp(self) :
        ''' load bnf grammar '''
        if not exists('ex01.bnf'):
            self.skipTest("no ex01.bnf")
        if not self._gram:
            with open('ex01.bnf',encoding="utf8") as file:
                self._gram, self._start = grammar(file.read())
    def test_asno(self):
        ''' test 'asno' sequence '''
        self.assertTrue(parse('asno'))
    def test_cria(self):
        ''' test 'cria' sequence '''
        self.assertFalse(parse('cria'))
    def test_gato(self):
        ''' test 'gato' sequence '''
        self.assertTrue(parse('gato'))
    def test_leao(self):
        ''' test 'leao' sequence '''
        self.assertFalse(parse('leao'))
    def test_ovos(self):
        ''' test 'OVOS' sequence '''
        self.assertFalse(parse('OVOS'))
    def test_tu(self):
        ''' test 'tu' sequence '''
        self.assertFalse(parse('tu'))
    def test_vaca(self):
        ''' test 'vaca' sequence '''
        self.assertTrue(parse('vaca'))
if __name__ == '__main__':
    unittest.main()
