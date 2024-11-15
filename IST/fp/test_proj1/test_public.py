#! /usr/bin/env python3
import unittest
from kanban import *
class TestKanban(unittest.TestCase):
	def test_1(self):
		self.assertRaises(ValueError, cria_atividade, 'to_do')
	def test_2(self):
		self.assertIsNotNone(cria_atividade('DONE'))
	def test_3(self):
		self.assertTrue(eh_atividade(cria_atividade('DONE')))
	def test_4(self):
		self.assertFalse(eh_atividade(1.2))
	def test_5(self):
		self.assertEqual('DONE', atividade_descricao(cria_atividade('DONE')))
	def test_6(self):
		self.assertEqual((), atividade_tarefas(cria_atividade('DONE')))
	def test_7(self):
		self.assertIsNotNone(cria_utilizador('ist99999', 'João da Silva'))
	def test_8(self):
		self.assertRaises(ValueError, cria_utilizador, 'ist99999', 'João Silva')
	def test_9(self):
		self.assertTrue(eh_utilizador(cria_utilizador('ist99999', 'João da Silva')))
	def test_10(self):
		self.assertFalse(eh_utilizador('ist99999'))
	def test_11(self):
		self.assertEqual('ist99999:0.0:0:João da Silva', utilizador_str(cria_utilizador('ist99999', 'João da Silva')))
	def test_12(self):
		user = cria_utilizador('ist99999', 'João da Silva')
		self.assertEqual('', utilizador_tarefas(user))
	def test_13(self):
		self.assertIsNotNone(cria_tarefa('projeto de F1', 12.0))
	def test_14(self):
		self.assertRaises(ValueError, cria_tarefa, ' \n\t', 2)
	def test_15(self):
		tsk = cria_tarefa('projeto de F2', 12.0)
		self.assertTrue(eh_tarefa(tsk))
	def test_16(self):
		self.assertFalse(eh_tarefa(1.0))
	def test_17(self):
		tsk = cria_tarefa('projeto de FF', 12.0)
		self.assertEqual('TO_DO', atividade_descricao(tarefa_atividade(tsk)))
	def test_18(self):
		tsk = cria_tarefa('projeto de F3', 12.0)
		rep = ('projeto de F3', 'TO_DO', '', 12.0, 0.0)
		self.assertEqual(rep, tarefa_representacao(tsk))
	def test_19(self):
		tsk = cria_tarefa('projeto de F4', 12.0)
		user = cria_utilizador('ist99999', 'João da Silva')
		out = tarefa_representacao(tarefa_colaborador(tsk, user))
		rep = ('projeto de F4', 'TO_DO', 'ist99999', 12.0, 0.0)
		self.assertEqual(rep, out)
	def test_20(self):
		tsk = cria_tarefa('projeto de F6', 12.0)
		act = cria_atividade('IN_PROGRESS')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = tarefa_colaborador(tsk, user)
		out = tarefa_representacao(tarefa_move(tsk, act, 5.6))
		rep = ('projeto de F6', 'IN_PROGRESS', 'ist99999', 12.0, 5.6)
		self.assertEqual(rep, out)
	def test_21(self):
		tsk = cria_tarefa('projeto de F7', 12.0)
		doing = cria_atividade('IN_PROGRESS')
		done = cria_atividade('DONE')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = tarefa_colaborador(tsk, user)
		tsk = tarefa_move(tsk, doing)
		tsk = tarefa_move(tsk, done, 5.6)
		self.assertAlmostEqual(6.4, tarefa_atraso(tsk))
	def test_22(self):
		tsk = cria_tarefa('projeto de F8', 12.0)
		out = tarefa_descricao(tsk, 'projeto de FC')
		self.assertEqual('projeto de F8', out)
	def test_23(self):
		self.assertRaises(ValueError, cria_atividade, 'LONG_ACTIVITY')
	def test_24(self):
		self.assertRaises(ValueError, cria_atividade, 'END')
	def test_25(self):
		self.assertRaises(ValueError, cria_utilizador, 'ist:99999', 'João da Silva')
	def test_26(self):
		self.assertRaises(ValueError, cria_utilizador, '', 'João da Silva')
	def test_27(self):
		self.assertRaises(ValueError, cria_utilizador, 'ist199999', 'João da Silva, estadista')
	def test_28(self):
		self.assertIsNotNone(cria_tarefa('    tsk    ', 12.0))
	def test_29(self):
		tsk = cria_tarefa('projeto de F9', 12.0)
		act = cria_atividade('IN_PROGRESS')
		self.assertRaises(ValueError, tarefa_move, tsk, act)
	def test_30(self):
		tsk = cria_tarefa('projeto de FG', 12.0)
		tarefa_colaborador(tsk, cria_utilizador('ist99999', 'João da Silva'))
		done = cria_atividade('DONE')
		tsk = tarefa_move(tsk, done, 5.6)
		self.assertEqual('DONE', atividade_descricao(tarefa_atividade(tsk)))

if __name__ == '__main__':
	unittest.main()
