#! /usr/bin/env python3
import unittest
from kanban import *
class Test(unittest.TestCase):
	def test_1(self):
		tsk = cria_tarefa('projeto de F0', 12.0)
		act = tarefa_atividade(tsk)
		tsks = atividade_tarefas(act)
		self.assertTrue(type(tsks) == tuple)
		self.assertEqual(len(tsks), 1)
		self.assertEqual(tsks[0], tsk)
	def test_2(self):
		tsk = cria_tarefa('Projeto de F0', 12.0)
		act = tarefa_atividade(tsk)
		tsks = atividade_tarefas(act)
		self.assertTrue(type(tsks) == tuple)
		self.assertEqual(len(tsks), 2)
		self.assertEqual(tsks[0], tsk)
		self.assertEqual(tarefa_representacao(tsks[1])[0], "projeto de F0")
	def test_3(self): # must include elapsed time for the user
		self.assertFalse(eh_utilizador(['ist99999', 'João da Silva']))
	def test_4(self): # 1 user task
		tsk = cria_tarefa('Projeto de F1', 12.0)
		user = cria_utilizador('ist99999', 'João da Silva')
		tarefa_colaborador(tsk, user)
		prjs = utilizador_tarefas(user)
		self.assertEqual(prjs, 'Projeto de F1\n')
	def test_5(self): # 2 user tasks
		tsk1 = cria_tarefa('projeto de F2', 12.0)
		tsk2 = cria_tarefa('Projeto de F2', 12.0)
		user = cria_utilizador('ist99999', 'João da Silva')
		tarefa_colaborador(tsk1, user)
		tarefa_colaborador(tsk2, user)
		prjs = utilizador_tarefas(user)
		self.assertEqual(prjs, 'Projeto de F2\nprojeto de F2\n')
	def test_6(self): # must include elapsed time
		self.assertFalse(eh_tarefa(['desc', 1.0]))
	def test_7(self): # trim
		self.assertRaises(ValueError, cria_tarefa, 'abc', '12')
	def test_8(self): # dup
		tsk = cria_tarefa('projeto de F3', 12.0)
		self.assertRaises(ValueError, cria_tarefa, 'projeto de F3', 21.0)
	def test_9(self): # tarefa_atividade other
		act = cria_atividade('IN_PROGRESS')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = cria_tarefa('projeto de F4', 12.0)
		old = tarefa_atividade(tsk)
		tarefa_colaborador(tsk, user)
		tarefa_move(tsk, act, 5.6)
		new = tarefa_atividade(tsk)
		self.assertEqual(atividade_descricao(old), 'TO_DO')
		self.assertEqual(atividade_descricao(new), 'IN_PROGRESS')
	def test_10(self): # user str após tsk assoc
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = cria_tarefa('projeto de F6', 12.0)
		tarefa_colaborador(tsk, user)
		self.assertEqual('ist99999:0.0:1:João da Silva', utilizador_str(user))
	def test_11(self): # tsk repr após move
		act = cria_atividade('IN_PROGRESS')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = cria_tarefa('projeto de F7', 12.0)
		tarefa_colaborador(tsk, user)
		tarefa_move(tsk, act, 6.5)
		rep = ('projeto de F7', 'IN_PROGRESS', 'ist99999', 12.0, 6.5)
		self.assertEqual(rep, tarefa_representacao(tsk))
	def test_12(self): # 1 user 2 tsks: utilizador_tarefas
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk1 = cria_tarefa('projeto de FA', 12.0)
		tsk2 = cria_tarefa('projeto de FB', 2.1)
		tarefa_colaborador(tsk1, user)
		tarefa_colaborador(tsk2, user)
		self.assertEqual('projeto de FA\nprojeto de FB\n', utilizador_tarefas(user))
	def test_13(self): # move success: atividade_tarefas
		tsk = cria_tarefa('projeto de FH', 12.0)
		tarefa_colaborador(tsk, cria_utilizador('ist99999', 'João da Silva'))
		done = cria_atividade('DONE')
		tsk = tarefa_move(tsk, done, 5.6)
		self.assertEqual(1, len(atividade_tarefas(done)))
		self.assertEqual(tsk, atividade_tarefas(done)[0])
	def test_14(self): # move all tsks in TO_DO to DONE
		tsk = cria_tarefa('projeto de FI', 12.0)
		user = cria_utilizador('ist99999', 'João da Silva')
		todo = tarefa_atividade(tsk)
		done = cria_atividade('DONE')
		for tsk in atividade_tarefas(todo):
			tarefa_colaborador(tsk, user)
			tarefa_move(tsk, done)
		self.assertEqual((), atividade_tarefas(todo))
	def test_15(self): # move success: utilizador_str
		act = cria_atividade('IN_PROGRESS')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = cria_tarefa('projeto de F8', 12.0)
		tarefa_colaborador(tsk, user)
		tarefa_move(tsk, act, 6.5)
		self.assertEqual('ist99999:6.5:1:João da Silva', utilizador_str(user))
	def test_16(self): # 1 user 2 moves: tsk_repr
		act = cria_atividade('IN_PROGRESS')
		done = cria_atividade('DONE')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = cria_tarefa('projeto de F9', 12.0)
		tarefa_colaborador(tsk, user)
		tarefa_move(tsk, act, 6.5)
		tarefa_move(tsk, done, 5.6)
		rep = ('projeto de F9', 'DONE', 'ist99999', 12.0, 12.1)
		self.assertEqual(rep, tarefa_representacao(tsk))
	def test_17(self): # 1 user 2 moves: user_str(sum)
		act = cria_atividade('IN_PROGRESS')
		done = cria_atividade('DONE')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = cria_tarefa('projeto de F10', 12.0)
		tarefa_colaborador(tsk, user)
		tarefa_move(tsk, act, 6.5)
		tarefa_move(tsk, done, 5.6)
		self.assertEqual('ist99999:12.1:1:João da Silva', utilizador_str(user))
	def test_18(self): # 2 user 1 tsk: user-1 => no task, user-2 => tsk
		done = cria_atividade('DONE')
		user1 = cria_utilizador('ist99999', 'João da Silva')
		user2 = cria_utilizador('ist99998', 'João dos Santos')
		tsk = cria_tarefa('projeto de F11', 12.0)
		tarefa_colaborador(tsk, user1)
		tarefa_colaborador(tsk, user2)
		self.assertEqual('ist99999:0.0:0:João da Silva', utilizador_str(user1))
		self.assertEqual('ist99998:0.0:1:João dos Santos', utilizador_str(user2))
	def test_19(self): # move: negative time
		done = cria_atividade('DONE')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = cria_tarefa('projeto de F12', 12.0)
		tarefa_colaborador(tsk, user)
		self.assertRaises(ValueError, tarefa_move, tsk, done, -6.5)
	def test_20(self): # 2 moves: atraso positivo
		act = cria_atividade('IN_PROGRESS')
		done = cria_atividade('DONE')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = cria_tarefa('projeto de F13', 12.0)
		tarefa_colaborador(tsk, user)
		tarefa_move(tsk, act, 6.5)
		tarefa_move(tsk, done, 5.4)
		self.assertAlmostEqual(0.1, tarefa_atraso(tsk))
	def test_21(self): # 2 moves: atraso negativo
		act = cria_atividade('IN_PROGRESS')
		done = cria_atividade('DONE')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = cria_tarefa('projeto de F14', 12.0)
		tarefa_colaborador(tsk, user)
		tarefa_move(tsk, act, 6.5)
		tarefa_move(tsk, done, 5.6)
		self.assertAlmostEqual(-0.1, tarefa_atraso(tsk))
	def test_22(self): # rename: insert new name
		tsk = cria_tarefa('projeto de F15', 12.0)
		tarefa_descricao(tsk, 'projeto de F16')
		self.assertRaises(ValueError, cria_tarefa, 'projeto de F16', 12.0)
	def test_23(self): # rename: insert old name
		tsk = cria_tarefa('projeto de F17', 12.0)
		tarefa_descricao(tsk, 'projeto de F18')
		tsk2 = cria_tarefa('projeto de F17', 12.0)
		self.assertNotEqual(id(tsk), id(tsk2))
	def test_24(self): # rename: user_str
		tsk = cria_tarefa('projeto de F19', 12.0)
		user = cria_utilizador('ist99999', 'João da Silva')
		tarefa_colaborador(tsk, user)
		tarefa_descricao(tsk, 'projeto de F20')
		self.assertEqual('projeto de F20\n', utilizador_tarefas(user))
	def test_25(self): # rename: act_tsks
		done = cria_atividade('DONE')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = cria_tarefa('projeto de F21', 12.0)
		tarefa_descricao(tsk, 'projeto de F22')
		tarefa_colaborador(tsk, user)
		tarefa_move(tsk, done, 5.6)
		self.assertEqual(tsk, atividade_tarefas(done)[0])
	def test_26(self): # no rename: act_tsks
		done = cria_atividade('DONE')
		user = cria_utilizador('ist99999', 'João da Silva')
		tsk = cria_tarefa('projeto de F21', 12.0) # free
		self.assertRaises(ValueError, tarefa_descricao, tsk, 'projeto de F22')
	def test_27(self): # colaborador: negative time
		doing = cria_atividade('DOING')
		user = cria_utilizador('ist99999', 'João da Silva')
		user2 = cria_utilizador('ist99998', 'João dos Santos')
		tsk = cria_tarefa('projeto de F23', 12.0)
		tarefa_colaborador(tsk, user)
		tarefa_move(tsk, doing, 5.6)
		self.assertRaises(ValueError, tarefa_colaborador, tsk, user2, -2.3)
	Tab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	tab = 'abcdefghijklmnopqrstuvwxyz'
	def intstr(self, num, tab = tab):
		out = ''
		while num:
			out += tab[num%len(tab)]
			num //= len(tab)
		return out
	def test_28(self): # 4k tsks: atividade tarefas
		tsk = cria_tarefa('a_', 12.0)
		for i in range(1, 4000):
			tsk = cria_tarefa(self.intstr(i), i)
		user = cria_utilizador('ist99999', 'João da Silva')
		tarefa_colaborador(tsk, user)
		act = cria_atividade('IN_PROGRESS')
		tarefa_move(tsk, act, 6.5)
		self.assertEqual(id(tsk), id(atividade_tarefas(act)[0]))
	def test_29(self): # 2k tsks: utilizador tarefas
		tsk = cria_tarefa('A_', 12.0)
		for i in range(1, 2000):
			desc = self.intstr(i, Test.Tab)
			tsk = cria_tarefa(desc, i)
		user = cria_utilizador('ist99999', 'João da Silva')
		tarefa_colaborador(tsk, user)
		self.assertEqual(desc+'\n', utilizador_tarefas(user))
	def test_30(self): # 500 tsks: move
		tsk = cria_tarefa('0_', 12.0)
		act = cria_atividade('IN_PROGRESS')
		user = cria_utilizador('ist99999', 'João da Silva')
		for i in range(1, 500):
			tsk = cria_tarefa(self.intstr(i, "0123456789"), i)
			tarefa_colaborador(tsk, user)
			tarefa_move(tsk, act, 1.0)
		self.assertEqual(499, len(atividade_tarefas(act)))
		self.assertEqual('ist99999:499.0:499:João da Silva', utilizador_str(user))

if __name__ == '__main__':
	# run tests in order (global TO_DO dependencies)
	cnt = 0
	for name in ('Test.test_' + str(n) for n in range(1,31)):
		print('Running', name)
		res = unittest.main(defaultTest=name, exit=False)
		if res.result.wasSuccessful():
			cnt += 1
	print('passed %d tests.' % cnt)
