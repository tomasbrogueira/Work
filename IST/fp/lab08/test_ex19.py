#! /usr/bin/env python3
''' tests for ex19.py '''
import unittest
import sys
from io import StringIO
SKIP = False
try :
    import ex19
except ImportError:
    SKIP = True
class TestEx19(unittest.TestCase):
    ''' test class for ex19.py '''
    def setUp(self) :
        if SKIP:
            self.skipTest("no ex19.py")
        self.unit = ex19
        self.stdout = sys.stdout
        sys.stdout = StringIO()
    def tearDown(self):
        sys.stdout = self.stdout
    def test_bomba(self):
        ''' Test sequence for default values '''
        es1 = self.unit.EstacaoServico()
        self.assertEqual(1000, es1.obtem_quantidade_combustivel(), "estacao com combustivel")
        for i in range(10):
            self.assertEqual(0, es1.obtem_consumo(i), "bombas sem consumo")
    def test_consumo(self):
        ''' Test sequence for '.obtem_consumo()' '''
        es1 = self.unit.EstacaoServico()
        es1.retira_combustivel(300, 3)
        self.assertEqual(300, es1.obtem_consumo(3), "consumo")
        es1.retira_combustivel(300, 4)
        self.assertEqual(300, es1.obtem_consumo(4), "consumo")
        es1.retira_combustivel(300, 3)
        self.assertEqual(600, es1.obtem_consumo(3), "consumo")
        es1.retira_combustivel(300, 4)
        self.assertEqual(400, es1.obtem_consumo(4), "consumo")
        es1.retira_combustivel(300, 3)
        self.assertEqual(600, es1.obtem_consumo(3), "consumo")
    def test_disponivel(self):
        ''' Test sequence for '.obtem_quantidade_combustivel()' '''
        es1 = self.unit.EstacaoServico()
        self.assertEqual(1000, es1.obtem_quantidade_combustivel(), "disponivel")
        es1.retira_combustivel(300, 3)
        self.assertEqual(700, es1.obtem_quantidade_combustivel(), "disponivel")
        es1.retira_combustivel(300, 4)
        self.assertEqual(400, es1.obtem_quantidade_combustivel(), "disponivel")
        es1.retira_combustivel(300, 3)
        self.assertEqual(100, es1.obtem_quantidade_combustivel(), "disponivel")
        es1.retira_combustivel(300, 4)
        self.assertEqual(0, es1.obtem_quantidade_combustivel(), "disponivel")
        es1.retira_combustivel(300, 3)
        self.assertEqual(0, es1.obtem_quantidade_combustivel(), "disponivel")
    def test_obtem_marca(self):
        ''' Test sequence for '.marca()' '''
        auto = self.unit.Veiculo("xpto")
        self.assertEqual("xpto", auto.marca(), "marca do veiculo")
    def test_abastece(self):
        ''' Test sequence for '.abastece()' '''
        es1 = self.unit.EstacaoServico()
        auto = self.unit.Veiculo("xpto")
        self.assertEqual(900, auto.abastece(900, 3, es1), "atestar")
        self.assertEqual(100, auto.abastece(900, 4, es1), "falta combustivel")
        self.assertEqual(0, auto.abastece(900, 5, es1), "bomba vazia")
    def test_obtem_marca_pesado(self):
        ''' Test sequence for Pesado '.marca()' '''
        auto = self.unit.VeiculoPesado("xpto")
        self.assertEqual("xpto", auto.marca(), "marca do veiculo")
    def test_travagem(self):
        ''' Test sequence for '.obtem_numero_travagens()' '''
        auto = self.unit.VeiculoPesado("xpto")
        self.assertEqual(0, auto.obtem_numero_travagens(), "sem travagem")
        auto.trava()
        auto.trava()
        self.assertEqual(2, auto.obtem_numero_travagens(), "travagem")
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), "GRRR GRRR\nGRRR GRRR\n")
    def test_acelera(self):
        ''' Test sequence for '.obtem_numero_aceleracoes()' '''
        auto = self.unit.VeiculoPesado("xpto")
        self.assertEqual(0, auto.obtem_numero_aceleracoes(), "sem aceleracao")
        auto.acelera()
        auto.acelera()
        self.assertEqual(2, auto.obtem_numero_aceleracoes(), "aceleracao")
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), "VRUM VRUM\nVRUM VRUM\n")
if __name__ == '__main__':
    unittest.main()
