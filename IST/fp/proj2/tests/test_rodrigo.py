import unittest, sys
from Sistema import *
sys.setrecursionlimit(2000000)


class TestCaminho(unittest.TestCase):
    def test_1(self):
        s = Sistema()
        t1 = TarefaDependente(s, 'task 1', 4)
        t2 = TarefaDependente(s, 'task 2', 3)
        t3 = TarefaDependente(s, 'task 3', 8)
        t4 = TarefaDependente(s, 'task 4', 7)
        t5 = TarefaDependente(s, 'task 5', 9)
        t6 = TarefaDependente(s, 'task 6', 12)
        t7 = TarefaDependente(s, 'task 7', 8)
        t8 = TarefaDependente(s, 'task 8', 9)
        t2 += t1
        t3 += t1
        t4 += t2
        t5 += t2
        t5 += t3
        t6 += t5
        t6 += t4
        t5 += t7
        t3 += t7
        t8 += t4
        caminho = [tsk.representacao()[0] for tsk in s.caminho_critico()]
        self.assertEqual(37, duracao(s.caminho_critico()))

    def test_2(self):
        s = Sistema()
        t1 = TarefaDependente(s, 'task 1', 9)
        t2 = TarefaDependente(s, 'task 2', 8)
        t3 = TarefaDependente(s, 'task 3', 14)
        t4 = TarefaDependente(s, 'task 4', 27)
        t5 = TarefaDependente(s, 'task 5', 3)
        t6 = TarefaDependente(s, 'task 6', 19)
        t7 = TarefaDependente(s, 'task 7', 12)
        t8 = TarefaDependente(s, 'task 8', 20)
        t9 = TarefaDependente(s, 'task 9', 21)
        t10 = TarefaDependente(s, 'task 10', 7)
        t1 += t3
        t2 += t7
        t4 += t7
        t4 += t10
        t5 += t3
        t5 += t10
        t8 += t4
        t8 += t1
        t6 += t5
        t9 += t8
        caminho = [tsk.representacao()[0] for tsk in s.caminho_critico()]
        self.assertEqual(80, duracao(s.caminho_critico()))

    Tab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tab = 'abcdefghijklmnopqrstuvwxyz'

    def intstr(self, num, tab=tab):
        out = ''
        while num:
            out += tab[num % len(tab)]
            num //= len(tab)
        return out

    def test_3(self):
        import time
        start = time.time()
        s = Sistema()
        n = 4000
        for i in range(1, n):
            tsk = TarefaDependente(s, self.intstr(i, "0123456789"), i)
            tsk2 = TarefaDependente(s, self.intstr(i, "ola"), i)
            tsk += tsk2

        end = time.time()

        print('took', end - start, 'seconds', n)

    def test_4(self):
        s = Sistema()
        t1 = TarefaDependente(s, 'task 1', 341)
        t2 = TarefaDependente(s, 'task 2', 941)
        t3 = TarefaDependente(s, 'task 3', 958)
        t4 = TarefaDependente(s, 'task 4', 789)
        t5 = TarefaDependente(s, 'task 5', 166)
        t6 = TarefaDependente(s, 'task 6', 577)
        t7 = TarefaDependente(s, 'task 7', 690)
        t8 = TarefaDependente(s, 'task 8', 779)
        t9 = TarefaDependente(s, 'task 9', 721)
        t10 = TarefaDependente(s, 'task 10', 710)
        t11 = TarefaDependente(s, 'task 11', 894)
        t12 = TarefaDependente(s, 'task 12', 272)
        t13 = TarefaDependente(s, 'task 13', 38)
        t14 = TarefaDependente(s, 'task 14', 607)
        t15 = TarefaDependente(s, 'task 15', 874)
        t16 = TarefaDependente(s, 'task 16', 997)
        t17 = TarefaDependente(s, 'task 17', 68)
        t18 = TarefaDependente(s, 'task 18', 625)
        t19 = TarefaDependente(s, 'task 19', 485)
        t20 = TarefaDependente(s, 'task 20', 373)
        with self.assertRaises(ValueError):
            t4 += t3
            t20 += t4
            t2 += t5
            t11 += t20
            t11 += t9
            t8 += t9
            t5 += t11
            t6 += t5
            print('here')
            t3 += t6

    def test_5(self):
        import time
        start = time.time()
        s = Sistema()
        n = 2000
        old = TarefaDependente(s, "Tarefa", 20)
        for i in range(1, n):
            tsk2 = TarefaDependente(s, self.intstr(i, "123456789"), i)
            tsk2 += old
            old = tsk2

        end = time.time()

        print('took', end - start, 'seconds', n)

    def test_6(self):
        import time
        start = time.time()
        s = Sistema()
        n = 10000
        fonte = TarefaDependente(s, "fonte", 20)
        sorv = TarefaDependente(s, "sorv", 20)
        for i in range(1, n):
            tsk = TarefaDependente(s, self.intstr(i, "123456789"), i)
            tsk += fonte
            sorv += tsk

        end = time.time()

        print('took', end - start, 'seconds', n)


if __name__ == '__main__':
    unittest.main()
