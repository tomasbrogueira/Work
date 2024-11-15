import unittest
from Sistema import *
class TestSistema(unittest.TestCase):
    def test1(self):#adicionar uma tarefa a ela própria
        sys = Sistema()
        t1 = TarefaDependente(sys, "task1", 12)
        self.assertRaises(ValueError, t1.__iadd__, t1)

    def test2(self):#adionar uma tarefa da qual depende
        sys = Sistema()
        t1 = TarefaDependente(sys, "task1", 10)
        t2 = TarefaDependente(sys, "task2", 12)
        t1 += t2
        self.assertRaises(ValueError, t2.__iadd__, t1)

    def test3(self):#adicionar duas vezes a mesma tarefa
        sys = Sistema()
        t1 = TarefaDependente(sys, "task1", 10)
        t2 = TarefaDependente(sys, "task2", 12)
        t1 += t2
        self.assertRaises(ValueError, t1.__iadd__, t2)

    def test4(self):#verifica a existência de loops
        sys = Sistema()
        t1 = TarefaDependente(sys, "task1", 10)
        t2 = TarefaDependente(sys, "task2", 12)
        t3 = TarefaDependente(sys, "task3", 45)
        t4 = TarefaDependente(sys, "task4", 7)
        t5 = TarefaDependente(sys, "task5", 1)
        t2 += t1
        t3 += t2
        t4 += t3
        t5 += t4
        self.assertRaises(ValueError, t2.__iadd__, t5)

    def test5(self):#verifica se a lista de dependencias está correta
        sys = Sistema()
        t1 = TarefaDependente(sys, 'task 1', 10)
        t2 = TarefaDependente(sys, 'task 2', 10)
        t3 = TarefaDependente(sys, 'task 3', 8)
        t4 = TarefaDependente(sys, 'task 4', 4)
        t5 = TarefaDependente(sys, 'task 5', 9)
        t6 = TarefaDependente(sys, 'task 6', 3)
        t7 = TarefaDependente(sys, 'task 7', 5)
        t8 = TarefaDependente(sys, 'task 8', 1)
        t9 = TarefaDependente(sys, 'task 9', 10)
        t10 = TarefaDependente(sys, 'task 10', 8)
        t2 += t1
        t10 += t9
        t9 += t5
        t9 += t6
        t3 += t2
        t6 += t5
        t10 += t4
        t7 += t2
        t6 += t1
        t5 += t4
        t8 += t3
        t9 += t2
        t10 += t6
        t9 += t7
        t10 += t1
        self.assertEqual(len(t10), 4)

if __name__ == '__main__':
	unittest.main()