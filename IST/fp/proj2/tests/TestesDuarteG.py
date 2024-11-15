from Sistema import *
import unittest
class Test(unittest.TestCase):
    def test_1(self):
        # Teste de EarlyStarts
        sys = Sistema()
        t0 = TarefaDependente(sys, 'task 0', 3)
        t1 = TarefaDependente(sys, 'task 1', 4)
        t2 = TarefaDependente(sys, 'task 2', 3)
        t3 = TarefaDependente(sys, 'task 3', 8)
        t4 = TarefaDependente(sys, 'task 4', 7)
        t5 = TarefaDependente(sys, 'task 5', 9)
        t6 = TarefaDependente(sys, 'task 6', 12)
        t7 = TarefaDependente(sys, 'task 7', 20)

        t2 += t0
        t2 += t1
        t3 += t1
        t4 += t2
        t5 += t2
        t5 += t3
        t6 += t5
        t6 += t4
        t7 += t4

        sys.caminho_critico()
        rep = [('task 0', 3, 0), ('task 1', 4, 0), ('task 2', 3, 4),
               ('task 3', 8, 4), ('task 4', 7, 7), ('task 5', 9, 12),
               ('task 6', 12, 21), ('task 7', 20, 14)]
        tu = [(tsk.representacao()[0], tsk.representacao()[3], tsk.inicio()) for
              tsk in sys.tarefas()]
        self.assertEqual(rep, tu)
    def test_2(self):
        # Teste de LateStarts
        sys = Sistema()
        t0 = TarefaDependente(sys, 'task 0', 3)
        t1 = TarefaDependente(sys, 'task 1', 4)
        t2 = TarefaDependente(sys, 'task 2', 3)
        t3 = TarefaDependente(sys, 'task 3', 8)
        t4 = TarefaDependente(sys, 'task 4', 7)
        t5 = TarefaDependente(sys, 'task 5', 9)
        t6 = TarefaDependente(sys, 'task 6', 12)
        t7 = TarefaDependente(sys, 'task 7', 20)

        t2 += t0
        t2 += t1
        t3 += t1
        t4 += t2
        t5 += t2
        t5 += t3
        t6 += t5
        t6 += t4
        t7 += t4

        sys.caminho_critico()
        rep = [('task 0', 3, 0, 1), ('task 1', 4, 0, 0), ('task 2', 3, 4, 4),
               ('task 3', 8, 4, 5), ('task 4', 7, 7, 7), ('task 5', 9, 12, 13),
               ('task 6', 12, 21, 22), ('task 7', 20, 14, 14)]
        tu = [(tsk.representacao()[0], tsk.representacao()[3], tsk.inicio(), tsk.inicio()+tsk.folga()) for
              tsk in sys.tarefas()]
        self.assertEqual(rep, tu)
    def test_3(self):
        # Testes de Caminho Crítico
        sys = Sistema()
        t0 = TarefaDependente(sys, 'task 0', 3)
        t1 = TarefaDependente(sys, 'task 1', 4)
        t2 = TarefaDependente(sys, 'task 2', 3)
        t3 = TarefaDependente(sys, 'task 3', 8)
        t4 = TarefaDependente(sys, 'task 4', 7)
        t5 = TarefaDependente(sys, 'task 5', 9)
        t6 = TarefaDependente(sys, 'task 6', 12)
        t7 = TarefaDependente(sys, 'task 7', 20)

        t2 += t0
        t2 += t1
        t3 += t1
        t4 += t2
        t5 += t2
        t5 += t3
        t6 += t5
        t6 += t4
        t7 += t4

        tu = sys.caminho_critico()
        rep = (t1, t2, t4, t7)
        self.assertEqual(rep, tu)


if __name__ == '__main__':
    unittest.main()