#! /usr/bin/env python3
import unittest
from Sistema import *
class TestSistema(unittest.TestCase):
	def test_1(self):
		sys = Sistema()
		act = Atividade(sys, "DONE")
		self.assertEqual("DONE", act.descricao())
	def test_2(self):
		sys = Sistema()
		tsk = Tarefa(sys, "Projeto FP", 12.3)
		self.assertEqual("TO_DO", tsk.atividade().descricao())
	def test_3(self):
		sys = Sistema()
		tsk = Tarefa(sys, "Projeto FP", 12.3)
		to_do = tsk.atividade()
		self.assertEqual(1, len(to_do.tarefas()))
		self.assertEqual(tsk, to_do.tarefas()[0])
	def test_4(self):
		sys = Sistema()
		usr = Utilizador(sys, 'ist99999', 'João da Silva')
		self.assertEqual('ist99999:0.0:0:João da Silva', str(usr))
	def test_5(self):
		sys = Sistema()
		usr = Utilizador(sys, 'ist99999', 'João da Silva')
		tsk = Tarefa(sys, "Projeto FP", 12.3)
		tsk.colaborador(usr)
		self.assertEqual('ist99999:0.0:1:João da Silva', str(usr))
		self.assertEqual("Projeto FP\n", usr.tarefas())
	def test_6(self):
		sys = Sistema()
		tsk = Tarefa(sys, "Projeto FP", 12.3)
		usr = Utilizador(sys, 'ist99999', 'João da Silva')
		act = Atividade(sys, "DONE")
		tsk.colaborador(usr)
		tsk2 = tsk.move(act, 1.23)
		self.assertEqual(tsk2, tsk)
		self.assertAlmostEqual(12.3-1.23, tsk.atraso())
	def test_7(self):
		sys = Sistema()
		tsk = Tarefa(sys, "Projeto FP", 12.3)
		usr = Utilizador(sys, 'ist99999', 'João da Silva')
		act = Atividade(sys, "DONE")
		tsk.colaborador(usr)
		tsk.move(act, 1.23)
		rep = ('Projeto FP', 'DONE', 'ist99999', 12.3, 1.23)
		self.assertEqual(rep, tsk.representacao())
	def test_8(self):
		sys = Sistema()
		tsk = Tarefa(sys, "Projeto FP", 12.3)
		usr = Utilizador(sys, 'ist99999', 'João da Silva')
		act = Atividade(sys, "DONE")
		tsk.colaborador(usr)
		tsk.move(act, 1.23)
		old = tsk.descricao("O mesmo projeto")
		self.assertEqual(old, "Projeto FP")
		rep = ('O mesmo projeto', 'DONE', 'ist99999', 12.3, 1.23)
		self.assertEqual(rep, tsk.representacao())
	def test_9(self):
		sys = Sistema()
		tsk1 = TarefaDependente(sys, "Projeto 1", 12)
		tsk2 = TarefaDependente(sys, "Projeto 2", 21)
		tsk2 += tsk1
		self.assertEqual(0, len(tsk1))
		self.assertEqual(1, len(tsk2))
	def test_10(self):
		sys = Sistema()
		tsk1 = TarefaDependente(sys, "Projeto 1", 12)
		tsk2 = TarefaDependente(sys, "Projeto 2", 21)
		tsk3 = TarefaDependente(sys, "Projeto 3", 34)
		tsk2 += tsk1
		tsk3 += tsk2
		self.assertEqual(0, len(tsk1))
		self.assertEqual(1, len(tsk2))
		self.assertEqual(1, len(tsk3))
	def test_11(self):
		sys = Sistema()
		tsk1 = TarefaDependente(sys, "Projeto 1", 12)
		tsk2 = TarefaDependente(sys, "Projeto 2", 21)
		tsk3 = TarefaDependente(sys, "Projeto 3", 34)
		tsk4 = TarefaDependente(sys, "Projeto 4", 34)
		tsk2 += tsk1
		tsk3 += tsk1
		tsk4 += tsk1
		self.assertEqual(0, len(tsk1))
		self.assertEqual(1, len(tsk2))
		self.assertEqual(1, len(tsk3))
		self.assertEqual(1, len(tsk4))
	def test_12(self):
		sys = Sistema()
		tsk1 = TarefaDependente(sys, "Projeto 1", 12)
		tsk2 = TarefaDependente(sys, "Projeto 2", 21)
		tsk3 = TarefaDependente(sys, "Projeto 3", 34)
		tsk4 = TarefaDependente(sys, "Projeto 4", 34)
		tsk1 += tsk2
		tsk1 += tsk3
		tsk1 += tsk4
		self.assertEqual(3, len(tsk1))
		self.assertEqual(0, len(tsk2))
		self.assertEqual(0, len(tsk3))
		self.assertEqual(0, len(tsk4))
	def test_13(self):
		sys = Sistema()
		todo = sys.to_do()
		tsk = TarefaDependente(sys, "Projeto 1", 12)
		self.assertEqual(todo, tsk.atividade())
	def test_14(self):
		sys = Sistema()
		t1 = TarefaDependente(sys, 't1', 12)
		t2 = TarefaDependente(sys, 't2', 21)
		t2 += t1
		self.assertEqual((t1,), sys.fonte())
		self.assertEqual((t2,), sys.sorvedoro())
	def test_15(self):
		sys = Sistema()
		t1 = TarefaDependente(sys, 't1', 12)
		t2 = TarefaDependente(sys, 't2', 21)
		t3 = TarefaDependente(sys, 't3', 21)
		t2 += t1
		t3 += t2
		self.assertEqual((t1,), sys.fonte())
		self.assertEqual((t3,), sys.sorvedoro())
	def test_16(self):
		sys = Sistema()
		tsk1 = TarefaDependente(sys, "Projeto 1", 12)
		tsk2 = TarefaDependente(sys, "Projeto 2", 21)
		tsk3 = TarefaDependente(sys, "Projeto 3", 34)
		tsk4 = TarefaDependente(sys, "Projeto 4", 34)
		tsk2 += tsk1
		tsk3 += tsk1
		tsk4 += tsk1
		self.assertEqual((tsk1,), sys.fonte())
		self.assertEqual((tsk2, tsk3, tsk4), sys.sorvedoro())
	def test_17(self):
		sys = Sistema()
		tsk1 = TarefaDependente(sys, "Projeto W", 12)
		tsk2 = TarefaDependente(sys, "Projeto X", 21)
		tsk3 = TarefaDependente(sys, "Projeto Y", 34)
		tsk4 = TarefaDependente(sys, "Projeto Z", 34)
		tsk1 += tsk2
		tsk1 += tsk3
		tsk1 += tsk4
		self.assertEqual((tsk2, tsk3, tsk4,), sys.fonte())
		self.assertEqual((tsk1,), sys.sorvedoro())
	def test_18(self):
		sys = Sistema()
		tsk = Tarefa(sys, "Projeto FP", 12.3)
		usr = Utilizador(sys, 'ist99999', 'João da Silva')
		grp = Grupo(sys, 'grupo 1', 'Muito trabalhador')
		grp += usr
		act = Atividade(sys, "DONE")
		tsk.colaborador(grp)
		tsk.move(act, 1.23)
		self.assertEqual('grupo 1:1.23:1:Muito trabalhador:1', str(grp))
	def test_19(self):
		sys = Sistema()
		tsk = Tarefa(sys, "Projeto FP", 12.3)
		usr = Utilizador(sys, 'ist99999', 'João da Silva')
		user2 = Utilizador(sys, 'ist99998', 'João dos Santos')
		grp = Grupo(sys, 'grupo 1', 'Muito trabalhador')
		grp += usr
		grp += user2
		act = Atividade(sys, "DONE")
		tsk.colaborador(grp)
		tsk.move(act, 1.23)
		self.assertEqual('grupo 1:1.23:1:Muito trabalhador:2', str(grp))
	def test_20(self):
		sys = Sistema()
		tsk = Tarefa(sys, "Projeto FP", 12.3)
		cnt = 0
		for task in tsk:
			cnt += 1
		self.assertEqual(0, cnt)
	def test_21(self):
		sys = Sistema()
		tsk = TarefaDependente(sys, "Projeto FP", 12.3)
		cnt = 0
		for task in tsk:
			cnt += 1
		self.assertEqual(0, cnt)
	def test_22(self):
		sys = Sistema()
		tsk1 = TarefaDependente(sys, "Projeto W", 12)
		tsk2 = TarefaDependente(sys, "Projeto X", 21)
		tsk3 = TarefaDependente(sys, "Projeto Y", 34)
		tsk4 = TarefaDependente(sys, "Projeto Z", 34)
		tsk1 += tsk2
		tsk1 += tsk3
		tsk1 += tsk4
		cnt = 0
		for task in tsk1:
			cnt += 1
		self.assertEqual(3, cnt)
	def test_23(self):
		sys = Sistema()
		sys2 = Sistema()
		tsk1 = TarefaDependente(sys, "Projeto W", 12)
		tsk2 = TarefaDependente(sys2, "Projeto X", 21)
		self.assertTrue("Projeto W" in sys)
		self.assertFalse("Projeto X" in sys)
		self.assertTrue("Projeto X" in sys2)
		self.assertFalse("Projeto W" in sys2)
	def test_24(self):
		sys = Sistema()
		t1 = TarefaDependente(sys, 'task 1', 4)
		t2 = TarefaDependente(sys, 'task 2', 3)
		t3 = TarefaDependente(sys, 'task 3', 8)
		t4 = TarefaDependente(sys, 'task 4', 7)
		t5 = TarefaDependente(sys, 'task 5', 9)
		t6 = TarefaDependente(sys, 'task 6', 12)
		cnt = 0
		for tsk in sys.tarefas():
			cnt += 1
		self.assertEqual(6, cnt)
	def test_25(self):
		sys = Sistema()
		cnt = 0
		for tsk in sys.atividades():
			cnt += 1
		self.assertEqual(1, cnt) # TO_DO
	def test_26(self):
		sys = Sistema()
		usr1 = Utilizador(sys, 'ist99999', 'João da Silva')
		usr2 = Utilizador(sys, 'ist99998', 'João dos Santos')
		usr3 = Utilizador(sys, 'ist99997', 'Jozé da Silva')
		usr4 = Utilizador(sys, 'ist99996', 'Jozé dos Santos')
		cnt = 0
		for tsk in sys.utilizadores():
			cnt += 1
		self.assertEqual(4, cnt)
	def test_27(self):
		sys = Sistema()
		act1 = Atividade(sys, "DOING")
		act2 = Atividade(sys, "IN_PROGRESS")
		cnt = 0
		for tsk in sys.atividades():
			cnt += 1
		self.assertEqual(3, cnt)
	def test_28(self):
		sys = Sistema()
		t1 = TarefaDependente(sys, 'task 1', 4)
		t2 = TarefaDependente(sys, 'task 2', 3)
		t3 = TarefaDependente(sys, 'task 3', 8)
		t4 = TarefaDependente(sys, 'task 4', 7)
		t5 = TarefaDependente(sys, 'task 5', 9)
		t6 = TarefaDependente(sys, 'task 6', 12)
		t2 += t1
		t3 += t1
		t4 += t2
		t5 += t2
		t5 += t3
		t6 += t5
		t6 += t4
		self.assertEqual((t1,), sys.fonte())
		self.assertEqual((t6,), sys.sorvedoro())
	def test_29(self):
		sys = Sistema()
		t1 = TarefaDependente(sys, 'task 1', 4)
		t2 = TarefaDependente(sys, 'task 2', 3)
		t3 = TarefaDependente(sys, 'task 3', 8)
		t4 = TarefaDependente(sys, 'task 4', 7)
		t5 = TarefaDependente(sys, 'task 5', 9)
		t6 = TarefaDependente(sys, 'task 6', 12)
		t2 += t1
		t3 += t1
		t4 += t2
		t5 += t2
		t5 += t3
		t6 += t5
		t6 += t4
		res = (t1, t3, t5, t6)
		self.assertEqual(res, sys.caminho_critico())
	def test_30(self):
		sys = Sistema()
		t1 = TarefaDependente(sys, 'task 1', 4)
		t2 = TarefaDependente(sys, 'task 2', 3)
		t3 = TarefaDependente(sys, 'task 3', 8)
		t4 = TarefaDependente(sys, 'task 4', 7)
		t5 = TarefaDependente(sys, 'task 5', 9)
		t6 = TarefaDependente(sys, 'task 6', 12)
		t2 += t1
		t3 += t1
		t4 += t2
		t5 += t2
		t5 += t3
		t6 += t5
		t6 += t4
		self.assertAlmostEqual(33., duracao(sys.caminho_critico()))

if __name__ == '__main__':
	unittest.main()
