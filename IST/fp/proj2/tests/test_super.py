#! /usr/bin/env python3
import os
import sys as s

# Faz com que os imports sejam válidos para ficheiros na mesma pasta, independentemente do cwd (current working directory)
s.path.append(os.path.dirname(os.path.realpath(__file__)))

from Sistema import *
import unittest
import re
from math import inf, isinf
from subprocess import Popen, PIPE, call
from multiprocessing import Process, Value
import random

# Ao contrário de alguns testes do lab10, os testes abaixo que precisem de ler o
# conteúdo de ficheiros .py são cegos a quaisquer comentários. Ou seja, se o teste
# procurar por alguma palavra no ficheiro, e ela estiver presente num comentário,
# o teste não vai encontrar nada ali. Cheers 🥂

# DISCLAIMER: os testes do operador += para TarefaDependente foram substituídos 💯

# DÚVIDAS
# verificar se += provêm de __iadd__ ou __add__ é um teste válido ao += R: não é
# que tipo de verificação é necessária aos argumentos de duracao() R: se quiseres
# > "Fica mais bonitinho com a validação, mas eu não vou testar" CONFIRMADO
# 1. ao fazer tsk.colaborador(grp), o Grupo grp propaga o insere() para os seus utilizadores? R: não

# Quando encontrarem o padrão:
#
# 	bak = Classe.func
# 	Classe.func = dec(Classe.func)
# 	assert Subclasse.func
# 	Classe.func = bak
#
# É sempre uma verificação se func vai buscar a função da classe que herda (com super().func)

# Encontra o comando correto de python no sistema em que os testes vão ser corridos
BUILD = ""
for py in ['python', 'python3', 'py']:
	if(call(py+' --version', stdout=PIPE, stderr=PIPE, shell=True) == 0):
		BUILD = py
		break
print(BUILD)

class TestSistemaSuper(unittest.TestCase):
	def random_tree(self, sys, tarefas, propensao):
		'''
		Cria uma árvore aleatória
		'''
		random.seed("esquilo")

		tsks = []
		for i in range(tarefas):
			tsk = TarefaDependente(sys, f"task {i}", random.randint(2, 16))
			for t in tsks:
				if(random.random() < propensao):
					tsk += t
			tsks.append(tsk)

	def base_tree(self, sys):
		'''
		Cria a árvore de tarefas do enunciado em `sys` 
		e devolve as 6 tarefas criadas
		'''
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
		return t1, t2, t3, t4, t5, t6

	def func_add(self, obj):
		'''
		Devolve a função associada ao operador `+=` de `obj`, ou a `+`, se a anterior não existir.
		Se nenhuma função tal for encontrada, levanta `NotImplementedError`
		'''
		if(not '__iadd__' in dir(obj) and not '__add__' in dir(obj)):
			raise NotImplementedError()
		return obj.__iadd__ if '__iadd__' in dir(obj) else obj.__add__

	def func_sub(self, obj):
		'''
		Devolve a função associada ao operador `-=` de `obj`, ou a `-`, se a anterior não existir.
		Se nenhuma função tal for encontrada, levanta `NotImplementedError`
		'''
		if(not '__isub__' in dir(obj) and not '__sub__' in dir(obj)):
			raise NotImplementedError()
		return obj.__isub__ if '__isub__' in dir(obj) else obj.__sub__

	def get_adjacent(self, file_name):
		return os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)

	def test_1(self):
		# Verificar se não há tralha a mais nos módulos, fora de classes, ou a ser importada pelo Sistema
		# ENUNCIADO
		manifesto = {"Atividade", "Grupo", "Sistema", "Tarefa", "TarefaDependente", "Utilizador", "duracao"}
		self.assertEqual({k for k in dir(__import__("Sistema")) if not k.startswith("__") and not k.endswith("__")}, manifesto)
	def test_2(self):
		# Verificar se as atividades TO_DO de 2 sistemas diferentes são distintas
		# RAZOÁVEL
		sys1 = Sistema()
		sys2 = Sistema()
		self.assertEqual(sys1.to_do().descricao(), 'TO_DO')
		self.assertEqual(sys2.to_do().descricao(), 'TO_DO')
		self.assertNotEqual(id(sys1.to_do()), id(sys2.to_do()))
	def test_3(self):
		# Verificar se todos os ficheiros do projeto já foram criados
		# RAZOÁVEL
		for file in ['Atividade', 'Utilizador', 'Tarefa', 'TarefaDependente', 'Grupo', 'Sistema', 'test', 'duracao']:
			self.assertTrue(os.path.exists(self.get_adjacent(file+'.py')))
	def test_4(self):
		# Verificar se uma tarefa fora da árvore principal constitui também uma árvore
		# (early = 0 e late = 0 != inf)
		# CONFIRMADO
		sys = Sistema()
		self.base_tree(sys)
		t7 = TarefaDependente(sys, 'task 7', 12)
		sys.caminho_critico()
		self.assertEqual(t7.inicio(), 0)
		self.assertAlmostEqual(t7.folga(), 21)
	"""def test_5(self):
		# Verificar se o __str__ da classe Grupo depende do __str__ herdado
		# RAZOÁVEL
		def dec(func):
			def new_func(*args, **kwargs):
				return "ID -> "+func(*args, **kwargs)
			return new_func
		bak = Utilizador.__str__
		Utilizador.__str__ = dec(Utilizador.__str__)
		grp = Grupo(Sistema(), 'grupo 1', "Pouco trabalhador")
		self.assertTrue(str(grp).startswith('ID -> '))
		Utilizador.__str__ = bak"""
	def test_6(self):
		# Verificar se a classe grupo reimplementa corretamente a função tempo
		# (alteração de 4jan22. em 2022. vão lá ver ao enunciado)
		# ENUNCIADO 
		sys = Sistema()
		grp = Grupo(sys, "grupo 1", "Pouco trabalhador")
		usr1 = Utilizador(sys, "user 1", "Manel das Couves")
		usr2 = Utilizador(sys, "user 2", "Manel das Batatas")
		grp.tempo(2147483647)
		grp += usr1
		grp += usr2
		self.assertEqual(str(grp), "grupo 1:2147483647.0:0:Pouco trabalhador:2")
		self.assertEqual(str(usr1), "user 1:0.0:0:Manel das Couves")
		self.assertEqual(str(usr2), "user 2:0.0:0:Manel das Batatas")
	def test_7(self):
		# Verificar se o programa passa os 30 testes públicos
		# RAZOÁVEL
		public = Popen([BUILD, self.get_adjacent('test_public.py')], stdout=PIPE, stderr=PIPE)
		msg = public.communicate()[1].decode('utf-8').split('\n')[-2]
		self.assertTrue(msg.startswith('OK'))
	def test_8(self):
		# Verificar se o programa passa os testes em test.py, se implementados
		# Salta o teste se test.py não existir ou não referenciar a classe TestCase do unittest
		# RAZOÁVEL
		if(not os.path.exists(self.get_adjacent('test.py'))):
			self.skipTest("test.py não existe")
		with open(self.get_adjacent('test.py'), 'r') as file:
			skip = True
			for line in file.readlines():
				ref_line = line[:-1] if not '#' in line else line[:line.find('#')]
				if('TestCase' in ref_line):
					skip = False
					break
			if(skip):
				self.skipTest("test.py não tem uma classe de testes")
		public = Popen([BUILD, self.get_adjacent('test.py')], stdout=PIPE, stderr=PIPE)
		msg = public.communicate()[1].decode('utf-8').split('\n')[-2]
		self.assertTrue(msg.startswith('OK'))
	def test_9(self):
		# Verificar se não existem atributos públicos ou demasiados atributos protegidos
		# Dica: ter uma função pública que devolve um atributo privado faz-te perder 5x
		# menos valores
		# RAZOÁVEL
		act = Atividade(Sistema(), 'PROGRESS')
		self.assertTrue(all([re.match('_\w+__', k) for k in act.__dict__]))
		tsk_dep = TarefaDependente(Sistema(), 'Tarefa 1', 15.0)
		count = [k for k in tsk_dep.__dict__ if not re.match('_\w+__', k)]
		self.assertTrue(len(count) <= 2 and all([k.startswith('_') for k in count]))
		grp = Grupo(Sistema(), 'grupo 1', "Pouco trabalhadores")
		count = [k for k in grp.__dict__ if not re.match('_\w+__', k)]
		self.assertTrue(len(count) <= 2 and all([k.startswith('_') for k in count]))
	def test_10(self):
		# Verificar se o caminho crítico muda após adicionar uma tarefa
		# RAZOÁVEL
		sys = Sistema()
		t6 = self.base_tree(sys)[5]
		t7 = TarefaDependente(sys, 'task 7', 9)
		out = [k.representacao()[0] for k in sys.caminho_critico()]
		self.assertEqual('task 1 -> task 3 -> task 5 -> task 6', ' -> '.join(out))
		out = [k.representacao()[0] for k in sys.caminho_critico()]
		self.assertEqual('task 1 -> task 3 -> task 5 -> task 6', ' -> '.join(out))
		t7 += t6
		out = [k.representacao()[0] for k in sys.caminho_critico()]
		self.assertEqual('task 1 -> task 3 -> task 5 -> task 6 -> task 7', ' -> '.join(out))
	def test_11(self):
		# Verificar se as tarefas que foram removidas da árvore têm os seus valores atualizados
		# RAZOÁVEL
		sys = Sistema()
		t6 = self.base_tree(sys)[5]
		t7 = TarefaDependente(sys, 'task 7', 9)
		t7 += t6
		sys.caminho_critico()
		self.assertEqual(t7.inicio(), 33)
		self.assertAlmostEqual(t7.folga(), 0)
		self.assertFalse(isinf(sum([k.folga() for k in sys.tarefas()])))
		t7 -= t6
		sys.caminho_critico()
		self.assertEqual(t7.inicio(), 0)
		self.assertAlmostEqual(t7.folga(), 24)
	def test_12(self):
		# Verificar se as tarefas NÃO são atualizadas para os utilizadores dentro do grupo
		# CONFIRMADO
		sys = Sistema()
		grp = Grupo(sys, 'grupo 1', "Pouco trabalhadores")
		user1 = Utilizador(sys, "user 1", "Manel das Couves")
		user2 = Utilizador(sys, "user 2", "Manel das Batatas")
		grp += user1
		grp += user2
		Tarefa(sys, "lavrar as terras", 2).colaborador(grp, 4)
		self.assertEqual(grp.tarefas(), "lavrar as terras\n")
		self.assertEqual(user1.tarefas(), "")
		self.assertEqual(user2.tarefas(), "")
	def test_13(self):
		# Verificar se -= funciona como esperado (não levanta erro quando não está lá)
		# RAZOÁVEL
		sys = Sistema()
		grp = Grupo(sys, 'grupo 1', "Pouco trabalhadores")
		self.assertRaises(ValueError, self.func_sub(grp), grp)
		user1 = Utilizador(sys, "user 1", "Manel das Couves")
		user2 = Utilizador(sys, "user 2", "Manel das Batatas")
		grp += user1
		grp += user2
		self.assertEqual(2, len(grp))
		grp -= user1
		self.assertEqual(1, len(grp))
		grp -= user1
		self.assertEqual(1, len(grp))
		#self.assertRaises(ValueError, self.func_sub(grp), user1)
		grp -= user2
		self.assertEqual(0, len(grp))
		grp -= user2
		self.assertEqual(0, len(grp))
		#self.assertRaises(ValueError, self.func_sub(grp), user2)
		tsk_parente = TarefaDependente(sys, 'task 1', 4)
		tsk1 = TarefaDependente(sys, 'task 2', 4)
		tsk2 = TarefaDependente(sys, 'task 3', 4)
		tsk_parente += tsk1
		tsk_parente += tsk2
		self.assertEqual(2, len(tsk_parente))
		tsk_parente -= tsk1
		self.assertEqual(1, len(tsk_parente))
		tsk_parente -= tsk1
		self.assertEqual(1, len(tsk_parente))
		#self.assertRaises(ValueError, self.func_sub(tsk_parente), tsk1)
		tsk_parente -= tsk2
		self.assertEqual(0, len(tsk_parente))
		tsk_parente -= tsk2
		self.assertEqual(0, len(tsk_parente))
		#self.assertRaises(ValueError, self.func_sub(tsk_parente), tsk2)
	def test_14(self):
		# Verificar se fonte e sorvedoro aceitam tarefas fora da árvore
		# Nota: tarefas dependentes não anexadas a nada são sorvedouros e fontes ao mesmo tempo
		# CONFRIMADO
		sys = Sistema()
		t1 = TarefaDependente(sys, 'task 1', 4)
		t2 = TarefaDependente(sys, 'task 2', 3)
		t3 = TarefaDependente(sys, 'task 3', 8)
		t4 = TarefaDependente(sys, 'task 4', 7)
		self.assertRaises(ValueError, lambda: Tarefa(sys, 'task 4', 4))
		self.assertEqual((t1, t2, t3, t4), sys.fonte())
		self.assertEqual((t1, t2, t3, t4), sys.sorvedoro())
		t1 += t2
		t2 += t3
		self.assertEqual((t3, t4), sys.fonte())
		self.assertEqual((t1, t4), sys.sorvedoro())
	def test_15(self):
		# Verificar se as classes e as funções públicas têm todas docstrings
		# CONFIRMADO
		classes = [Atividade, Tarefa, Utilizador, TarefaDependente, Grupo, Sistema]
		funcs = set()
		for c in classes:
			funcs.update({eval(c.__name__+'.'+k) for k in dir(c) if not k.startswith('__') and not k.endswith('__')})
			self.assertNotEqual(c.__doc__, None)
		for f in funcs:
			self.assertNotEqual(f.__doc__, None)
	def test_16(self):
		# Verifica se todos os erros levantados nestes 30 testes têm uma mensagem que começa
		# com o nome da função em que está inserida, ou "cria", se for um construtor
		# RAZOÁVEL
		def newAssertRaises(err, func, *args, **kwargs):
			regex = f'cria_\w*' if func.__name__ == "<lambda>" else f'\w*{func.__name__}'
			self.assertRaisesRegex(err, regex+': .*', func, *args, **kwargs)
		bak = self.assertRaises
		self.assertRaises = newAssertRaises
		error_tests = set()
		with open(__file__, 'r') as self_file: # Sim, um programa pode ler-se a si próprio
			test = ""
			for line in self_file:
				ref_line = line[:line.find('#')] if '#' in line else line
				search = re.search('def (test_\d+)\(self\)', ref_line)
				if(search):
					test = search.group(1)
					continue
				if(test and re.search('self.assertRaises\(\w+Error,', ref_line)):
					error_tests.add(test)
		for err in error_tests:
			exec(f"self.{err}()")
		self.assertRaises = bak
	def test_17(self):
		# Verifica se todos os dunders foram implementados
		# RAZOÁVEL
		# self.assertTrue(all([k in dir(Tarefa) for k in ['__len__', '__iter__']]))
		self.assertIn('__iter__', dir(Tarefa))
		self.func_add(TarefaDependente)
		self.func_sub(TarefaDependente)
		self.assertTrue(all([k in dir(TarefaDependente) for k in ['__len__', '__iter__']]))
		self.func_add(Grupo)
		self.func_sub(Grupo)
		self.assertTrue(all([k in dir(Grupo) for k in ['__len__', '__str__']]))
		self.assertIn('__contains__', dir(Sistema))
		self.assertIn('__str__', dir(Utilizador))
	def test_18(self):
		# Verifica se os utilizadores de um grupo são sempre únicos
		# RAZOÁVEL
		sys = Sistema()
		grp = Grupo(sys, "grupo 1", "Pouco trabalhador")
		user1 = Utilizador(sys, "user 1", "Manel das Couves")
		user2 = Utilizador(sys, "user 1", "Manel das Batatas")
		user3 = Utilizador(sys, "user 1", "Manel dos Nabos")
		grp += user1
		grp += user2
		grp += user2
		grp += user3
		grp += user3
		grp += user3
		self.assertEqual(len(grp), 3)
		self.assertRaises(ValueError, self.func_add(grp), grp)
	def test_19(self):
		# Verifica se inserir uma tarefa em um objeto de outro sistema diferente dá erro
		# CONFIRMADO
		tsk = TarefaDependente(Sistema(), 'task 1', 4)
		act = Atividade(Sistema(), 'PROGRESS')
		self.assertRaises(ValueError, tsk.move, act)
		self.assertRaises(ValueError, tsk.move, Sistema().to_do())
		self.assertRaises(ValueError, tsk.colaborador, Utilizador(Sistema(), "user 1", "Manel das Nabiças"))
	def test_20(self):
		# Verifica se interações no mesmo sistema passam e entre sistemas diferentes levantam erro
		# CONFIRMADO
		sys = Sistema()
		grp = Grupo(sys, "grupo 1", "Pouco trabalhador")
		grp_ext = Grupo(Sistema(), "grupo 1", "Pouco trabalhador")
		user = Utilizador(sys, "user 1", "Manel das Couves")
		user_ext = Utilizador(Sistema(), "user 1", "Manel das Couves")
		act = Atividade(sys, 'PROGRESS')
		act_ext = Atividade(Sistema(), 'PROGRESS')
		tsk = Tarefa(sys, 'task 1', 4)
		tsk.colaborador(grp)
		# self.assertRaises(ValueError, tsk.move, act)
		tsk.move(act)
		grp += user
		tsk.move(act).colaborador(user)
		self.assertRaises(ValueError, tsk.colaborador, grp_ext)
		self.assertRaises(ValueError, tsk.move, act_ext)
		self.assertRaises(ValueError, tsk.colaborador, user_ext)
	def test_21(self):
		# Verifica se o caminho crítico é sempre a árvore com maior durcação
		# CONFIRMADO
		sys = Sistema()
		t1 = TarefaDependente(sys, 'task 1', 4)
		t2 = TarefaDependente(sys, 'task 2', 4)
		t3 = TarefaDependente(sys, 'task 3', 4)
		t4 = TarefaDependente(sys, 'task 4', 10)
		self.assertEqual((t4,), sys.caminho_critico())
		t2 += t1
		self.assertEqual((t4,), sys.caminho_critico())
		t3 += t2
		self.assertEqual((t1, t2, t3), sys.caminho_critico())
		t4 += t3
		self.assertEqual((t1, t2, t3, t4), sys.caminho_critico())
	def test_22(self):
		# Verifica se o operador += provêm de __iadd__ e não de __add__ e o mesmo para o -=
		# (os outros testes estão desenhados para não avaliar isto)
		# CONFIRMADO
		self.assertIn('__iadd__', dir(TarefaDependente))
		self.assertNotIn('__add__', dir(TarefaDependente))
		self.assertIn('__isub__', dir(TarefaDependente))
		self.assertNotIn('__sub__', dir(TarefaDependente))
		self.assertIn('__iadd__', dir(Grupo))
		self.assertNotIn('__add__', dir(Grupo))
		self.assertIn('__isub__', dir(Grupo))
		self.assertNotIn('__sub__', dir(Grupo))
	def test_23(self):
		# Verifica se o caminho_critico() se porta bem perante uma árvore esquisita
		# (este tipo de árvore foi aceite)
		# CONFIRMADO
		sys = Sistema()
		t1 = TarefaDependente(sys, 'task 1', 4)
		t2 = TarefaDependente(sys, 'task 2', 3)
		t3 = TarefaDependente(sys, 'task 3', 8)
		t4 = TarefaDependente(sys, 'task 4', 7)
		t4 += t1
		t4 += t2
		t4 += t3
		t3 += t1
		t3 += t2
		t2 += t1
		out = [k.representacao()[0] for k in sys.caminho_critico()]
		self.assertEqual('task 1 -> task 2 -> task 3 -> task 4', ' -> '.join(out))
		self.assertTrue(all(k.critica() for k in sys.tarefas()))
	def test_24(self):
		# Verifica como é que a função duração valida os argumentos
		# (No enunciado entende-se que se deve calcular folga() e inicio() no corpo da
		# função. De acordo com o professor, deve-se ler "usar")
		# Em relação à validação, não é estritamente necessário, mas, e cito, 
		# "fica mais bonitinho"
		# RAZOÁVEL
		sys = Sistema()
		t1, t2, t3, t4, t5, t6 = self.base_tree(sys)
		t7 = TarefaDependente(sys, 'task 7', 9)
		# t8 = Tarefa(sys, 'task 8', 4)
		# self.assertRaises(StopIteration, next, iter(t8))
		self.assertAlmostEqual(duracao(sys.caminho_critico()), 33)
		# vvv COMPONENTES DE VALIDAÇÃO vvv
		# self.assertAlmostEqual(duracao((t1, t3, t5, t6)), 33)
		# self.assertRaises(ValueError, duracao, [t1, t3, t5, t6])
		# self.assertRaises(ValueError, duracao, (t1, t2, t5, t6))
		# self.assertRaises(ValueError, duracao, (t1, t5, t2, t6))
		# self.assertRaises(ValueError, duracao, (t1, t2, t5, t8))
		# self.assertAlmostEqual(duracao((t3, t5, t6)), 29)
		# self.assertAlmostEqual(duracao((t1, t3, t5)), 21)
		# self.assertRaises(ValueError, duracao, (t1, t5, t6))
	def test_25(self):
		# Verifica se as tarefas são corretamente assinaladas como críticas após alterar as dependências
		# CONFIRMADO
		sys = Sistema()
		t1 = TarefaDependente(sys, 'task 1', 4)
		t2 = TarefaDependente(sys, 'task 2', 3)
		t3 = TarefaDependente(sys, 'task 3', 8)
		t4 = TarefaDependente(sys, 'task 4', 7)
		t5 = TarefaDependente(sys, 'task 5', 2)
		t6 = TarefaDependente(sys, 'task 6', 12)
		t2 += t1
		t3 += t1
		t4 += t2
		t5 += t3
		t6 += t5
		t6 += t4
		crit = sys.caminho_critico()
		self.assertTrue((t1, t2, t4, t6) == crit or (t1, t3, t5, t6) == crit)
		self.assertTrue(all(k.critica() for k in sys.tarefas()))
		t7 = TarefaDependente(sys, 'task 7', 14)
		self.assertTrue(all(k.critica() for k in sys.tarefas() if k != t7))
		self.assertFalse(t7.critica())
		t8 = TarefaDependente(sys, 'task 8', 26)
		sys.caminho_critico()
		self.assertTrue(all(k.critica() for k in sys.tarefas() if k != t7))
		t9 = TarefaDependente(sys, 'task 9', 27)
		self.assertTrue((t9,), sys.caminho_critico())
		self.assertTrue(all(not k.critica() for k in sys.tarefas() if k != t9))
		self.assertTrue(t9.critica())
	def test_26(self):
		# Verifica se o operador += do tipo Grupo tem comportamento semelhante ao do TarefaDepentente
		# RAZOÁVEL
		sys = Sistema()
		grp1 = Grupo(sys, "grupo 1", "Pouco trabalhador")
		grp2 = Grupo(sys, "grupo 2", "Muito trabalhador")
		grp3 = Grupo(sys, "grupo 3", "Baixo desempenho")
		grp4 = Grupo(sys, "grupo 4", "Não dá uma para a caixa")
		grp1 += grp2
		grp2 += grp3
		grp3 += grp4
		self.assertRaises(ValueError, self.func_add(grp4), grp1)
		self.assertRaises(ValueError, self.func_add(grp1), grp1)
	def test_27(self):
		# Verifica se os grupos contabilizam o tempo mesmo bem
		# RAZOÁVEL
		sys = Sistema()
		grp1 = Grupo(sys, "grupo 1", "Pouco trabalhadores")
		grp2 = Grupo(sys, "grupo 2", "Esforçam se pouco")
		grp3 = Grupo(sys, "grupo 3", "Não dão uma para a caixa")
		grp4 = Grupo(sys, "grupo 4", "Desmotivados")
		user1 = Utilizador(sys, "user 1", "Manel das Couves")
		user2 = Utilizador(sys, "user 2", "Manel das Batatas")
		user3 = Utilizador(sys, "user 3", "Manel das Cenouras")
		user4 = Utilizador(sys, "user 4", "Manel dos Nabos")
		user5 = Utilizador(sys, "user 5", "Manel das Courgetes")
		user6 = Utilizador(sys, "user 6", "Manel das Cebolas")
		self.assertEqual("grupo 1:0.0:0:Pouco trabalhadores:0", str(grp1))
		grp1 += user1
		grp1 += user2
		grp1 += grp2
		self.assertEqual("grupo 1:0.0:0:Pouco trabalhadores:3", str(grp1))
		grp1.tempo(30)
		# self.assertEqual("grupo 1:30.0:0:Pouco trabalhadores:3", str(grp1))
		# self.assertEqual("user 1:15.0:0:Manel das Couves", str(user1))
		# self.assertEqual("user 2:15.0:0:Manel das Batatas", str(user2))
		self.assertEqual("grupo 1:30.0:0:Pouco trabalhadores:3", str(grp1))
		self.assertEqual("user 1:10.0:0:Manel das Couves", str(user1))
		self.assertEqual("user 2:10.0:0:Manel das Batatas", str(user2))
		grp2 += grp3
		grp2 += grp4
		grp1.tempo(30)
		# self.assertEqual("grupo 1:60.0:0:Pouco trabalhadores:3", str(grp1))
		# self.assertEqual("grupo 2:10.0:0:Esforçam se pouco:2", str(grp2))
		# self.assertEqual("grupo 3:0.0:0:Não dão uma para a caixa:0", str(grp3))
		# self.assertEqual("grupo 4:0.0:0:Desmotivados:0", str(grp4))
		# self.assertEqual("user 1:25.0:0:Manel das Couves", str(user1))
		# self.assertEqual("user 2:25.0:0:Manel das Batatas", str(user2))
		self.assertEqual("grupo 1:60.0:0:Pouco trabalhadores:3", str(grp1))
		self.assertEqual("grupo 2:20.0:0:Esforçam se pouco:2", str(grp2))
		self.assertEqual("grupo 3:5.0:0:Não dão uma para a caixa:0", str(grp3))
		self.assertEqual("grupo 4:5.0:0:Desmotivados:0", str(grp4))
		self.assertEqual("user 1:20.0:0:Manel das Couves", str(user1))
		self.assertEqual("user 2:20.0:0:Manel das Batatas", str(user2))
		grp3 += user3
		grp3 += user4
		grp4 += user5
		grp4 += user6
		grp4 += user1
		grp1.tempo(180)
		# self.assertEqual("grupo 1:240.0:0:Pouco trabalhadores:3", str(grp1))
		# self.assertEqual("grupo 2:70.0:0:Esforçam se pouco:2", str(grp2))
		# self.assertEqual("grupo 3:30.0:0:Não dão uma para a caixa:2", str(grp3))
		# self.assertEqual("grupo 4:30.0:0:Desmotivados:3", str(grp4))
		# self.assertEqual("user 1:95.0:0:Manel das Couves", str(user1))
		# self.assertEqual("user 2:85.0:0:Manel das Batatas", str(user2))
		# self.assertEqual("user 3:15.0:0:Manel das Cenouras", str(user3))
		# self.assertEqual("user 4:15.0:0:Manel dos Nabos", str(user4))
		# self.assertEqual("user 5:10.0:0:Manel das Courgetes", str(user5))
		# self.assertEqual("user 6:10.0:0:Manel das Cebolas", str(user6))
		self.assertEqual("grupo 1:240.0:0:Pouco trabalhadores:3", str(grp1))
		self.assertEqual("grupo 2:80.0:0:Esforçam se pouco:2", str(grp2))
		self.assertEqual("grupo 3:35.0:0:Não dão uma para a caixa:2", str(grp3))
		self.assertEqual("grupo 4:35.0:0:Desmotivados:3", str(grp4))
		self.assertEqual("user 1:90.0:0:Manel das Couves", str(user1))
		self.assertEqual("user 2:80.0:0:Manel das Batatas", str(user2))
		self.assertEqual("user 3:15.0:0:Manel das Cenouras", str(user3))
		self.assertEqual("user 4:15.0:0:Manel dos Nabos", str(user4))
		self.assertEqual("user 5:10.0:0:Manel das Courgetes", str(user5))
		self.assertEqual("user 6:10.0:0:Manel das Cebolas", str(user6))
	def test_28(self):
		# Verifica se todos os ficheiros passam ao teste do lizard
		# ENUNCIADO
		msg = "LIZARD OK"
		for file in ['Atividade', 'Utilizador', 'Tarefa', 'TarefaDependente', 'Grupo', 'Sistema', 'duracao']:
			if(call(f"lizard -L 25 {file}.py", stdout=PIPE, stderr=PIPE, shell=True) != 0):
				msg = file + ".py falhou"
				break
		self.assertEqual(msg, "LIZARD OK")
	def test_29(self):
		# Verifica se algumas componentes do Sistema funcionam como esperado e são utilizadas
		# onde esperado
		# (__contains__(), atividade(), utilizador(), tarefa())
		# RAZOÁVEL
		sys = Sistema()
		objs = {
			'tarefa': Tarefa(sys, "AQUIAQUIAQUI", 10), 
			'atividade': Atividade(sys, "AQUIAQUIAQUI"), 
			'utilizador': Utilizador(sys, 'user 0', "AQUIAQUIAQUI")
		}
		descs = {}
		for key in objs:
			for obj_key in objs[key].__dict__:
				if(objs[key].__dict__[obj_key] == "AQUIAQUIAQUI"):
					descs[key] = obj_key
					break
		def dec_obj(suffix):
			def dec(func):
				def new_func(self, obj):
					obj.__dict__[descs[func.__name__]] += suffix
					func(self, obj)
				return new_func
			return dec
		# vvv __contains__() vvv
		tsk = Tarefa(sys, 'task 1', 3)
		tsk_dep = TarefaDependente(sys, 'task 2', 3)
		self.assertIn('task 1', sys)
		self.assertIn('task 2', sys)
		self.assertNotIn('task 3', sys)
		# self.assertRaises(ValueError, sys.__contains__, tsk)
		# self.assertRaises(ValueError, sys.__contains__, tsk_dep)
		self.assertNotIn(tsk, sys)
		self.assertNotIn(tsk_dep, sys)
		# vvv tarefa(), atividade(), utilizador() vvv
		bak1, bak2, bak3 = Sistema.tarefa, Sistema.atividade, Sistema.utilizador
		Sistema.tarefa =  dec_obj(" - modificada")(Sistema.tarefa)
		Sistema.atividade =  dec_obj("_MOD")(Sistema.atividade)
		Sistema.utilizador =  dec_obj(" - modificado")(Sistema.utilizador)
		sys = Sistema()
		tsk = Tarefa(sys, 'apanhar uvas', 6)
		act = Atividade(sys, 'VINDIMAS')
		user = Utilizador(sys, 'user 1', "Manel das Uvas")
		self.assertEqual(["apanhar uvas - modificada"], [k.representacao()[0] for k in sys.tarefas()])
		self.assertEqual(["TO_DO_MOD", "VINDIMAS_MOD"], [k.descricao() for k in sys.atividades()])
		self.assertEqual(["Manel das Uvas - modificado"], [str(k).split(':')[3] for k in sys.utilizadores()])
		Sistema.tarefa, Sistema.atividade, Sistema.utilizador = bak1, bak2, bak3
	def test_30(self):
		# Verifica se todos os construtores de classes que herdam de outras referem ao construtor
		# da classe de que herdam (com super())
		# RAZOÁVEL
		def dec(func):
			def new_func(base, *args):
				func(base, *args)
				base.__atributo_tonto = "uma cena qualquer"
			return new_func
		bak1, bak2 = Tarefa.__init__, Utilizador.__init__
		Tarefa.__init__ = dec(Tarefa.__init__)
		Utilizador.__init__ = dec(Utilizador.__init__)
		sys = Sistema()
		tsk = TarefaDependente(sys, 'task 1', 4)
		grp = Grupo(sys, "grupo 1", "Pouco trabalhador")
		self.assertIn('_TestSistemaSuper__atributo_tonto', tsk.__dict__)
		self.assertIn('_TestSistemaSuper__atributo_tonto', grp.__dict__)
		self.assertEqual(tsk.__atributo_tonto, "uma cena qualquer")
		self.assertEqual(grp.__atributo_tonto, "uma cena qualquer")
		Tarefa.__init__, Utilizador.__init__ = bak1, bak2

if __name__ == '__main__':
	unittest.main()
