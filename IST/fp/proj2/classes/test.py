import unittest
from Sistema import Sistema,TarefaDependente,Tarefa

class Test_t_dep(unittest.TestCase):
    def test_default(self):
        '''
        testa o caso normal de __iadd__ correto
        '''
        sys = Sistema()
        t_1 = TarefaDependente(sys, 'task 1', 4)
        t_2 = TarefaDependente(sys, 'task 2', 3)
        t_3 = TarefaDependente(sys, 'task 3', 8)
        t_4 = TarefaDependente(sys, 'task 4', 7)
        t_5 = TarefaDependente(sys, 'task 5', 9)
        t_6 = TarefaDependente(sys, 'task 6', 12)

        t_2 += t_1
        t_3 += t_1
        t_4 += t_2
        t_5 += t_2
        t_5 += t_3
        t_6 += t_5
        t_6 += t_4
        #testa também se sabe lidar com dependencias repetidas
        t_6 += t_4

        self.assertTrue(t_1 in t_2)
        self.assertTrue(t_4 in t_6)
        self.assertTrue(t_5 in t_6)
        self.assertFalse(t_6 in t_3)
        #foi usado o iterador


    def test_ciclos(self):
        '''
        testa a existência de ciclos
        '''
        sys = Sistema()
        t_1 = TarefaDependente(sys, 'task 1', 4)
        t_2 = TarefaDependente(sys, 'task 2', 3)
        t_3 = TarefaDependente(sys, 'task 3', 12)
        t_4 = TarefaDependente(sys, 'task 4', 7)
        t_5 = TarefaDependente(sys, 'task 5', 9)

        t_1 += t_2
        t_2 += t_3
        t_3 += t_4
        t_4 += t_5

        #termina o ciclo
        self.assertRaises(ValueError,t_5.__iadd__,t_1)


    def test_add_not_depend(self):
        '''
        testa se levanta erro quando se adiciona algo que não é uma t_dep
        '''
        sys = Sistema()
        t_1 = TarefaDependente(sys, 'task 1', 4)
        t_2 = TarefaDependente(sys, 'task 2', 3)
        t_3 = TarefaDependente(sys, 'task 3', 2)
        t_4 = TarefaDependente(sys, 'task 4', 7)
        t_5 = Tarefa(sys, 'task 5', 6)

        t_1 += t_2
        t_2 += t_3
        t_1 += t_4

        #adiciona uma tarefa não dependente
        self.assertRaises(ValueError,t_2.__iadd__,t_5 )


    def test_own_dep(self):
        '''
        testa a dependencia duma tarefa sobre si própria
        '''
        sys = Sistema()
        t_1 = TarefaDependente(sys, 'task 1', 4)
        t_2 = TarefaDependente(sys, 'task 2', 3)

        t_1 += t_2

        self.assertRaises(ValueError,t_1.__iadd__,t_1)
        #cria uma dependencia própria


    def test_crit_in_caminho_crit(self):
        '''
        testa se todas as tarefas do caminho critico são críticas
        '''
        sys = Sistema()
        t_1 = TarefaDependente(sys, 'task 1', 4)
        t_2 = TarefaDependente(sys, 'task 2', 3)
        t_3 = TarefaDependente(sys, 'task 3', 8)
        t_4 = TarefaDependente(sys, 'task 4', 7)
        t_5 = TarefaDependente(sys, 'task 5', 9)
        t_6 = TarefaDependente(sys, 'task 6', 12)

        t_2 += t_1
        t_3 += t_1
        t_4 += t_2
        t_5 += t_2
        t_5 += t_3
        t_6 += t_5
        t_6 += t_4

        self.assertTrue(all(tarefa.critica() for tarefa in sys.caminho_critico()))


    def test_s_dif(self):
        '''
        testa se é levantado erro quando ligamos t_dep de sistemas diferentes
        '''
        sys1 = Sistema()
        t_1 = TarefaDependente(sys1, 'task 1', 4)
        t_2 = TarefaDependente(sys1, 'task 2', 3)

        sys2 = Sistema()
        t_3 = TarefaDependente(sys2, 'task 3', 8)

        t_1 += t_2

        self.assertRaises(ValueError,t_1.__iadd__,t_3)

if __name__ == '__main__':
    unittest.main()
