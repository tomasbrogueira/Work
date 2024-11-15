import unittest
from Sistema import *
class Testiadd(unittest.TestCase):
    def test_good(self):
        sys = Sistema()
        task1 = TarefaDependente(sys, "task1", 12.0)
        task2 = TarefaDependente(sys, "task2", 8.0)
        task1 += task2
        self.assertTrue(task2 in task1)
    def test_slef_dependent(self):
        sys = Sistema()
        task1 = TarefaDependente(sys, "task1", 12.0)
        self.assertRaises(ValueError, task1.__iadd__, task1)
    def test_add_again(self):
        sys = Sistema()
        task1 = TarefaDependente(sys, "task1", 12.0)
        task2 = TarefaDependente(sys, "task2", 8.0)
        task1 += task2
        self.assertRaises(ValueError, task1.__iadd__, task2)
    def test_add_dependent(self):
        sys = Sistema()
        task1 = TarefaDependente(sys, "task1", 12.0)
        task2 = TarefaDependente(sys, "task2", 8.0)
        task1 += task2
        self.assertRaises(ValueError, task2.__iadd__, task1)
    def test_create_cycle(self):
        sys = Sistema()
        task1 = TarefaDependente(sys, "task1", 12.0)
        task2 = TarefaDependente(sys, "task2", 8.0)
        task3 = TarefaDependente(sys, "task3", 6.0)
        task4 = TarefaDependente(sys, "task4", 3.0)
        task5 = TarefaDependente(sys, "task5", 17.0)
        task6 = TarefaDependente(sys, "task6", 15.0)
        task7 = TarefaDependente(sys, "task7", 13.0)
        task8 = TarefaDependente(sys, "task8", 11.0)
        task1 += task3
        task2 += task4
        task3 += task8
        task4 += task5
        task5 += task6
        task3 += task5
        task5 += task7
        self.assertRaises(ValueError, task7.__iadd__, task1)
    def test_critica(self):
        sys = Sistema()
        task1 = TarefaDependente(sys, "task1", 12.0)
        task2 = TarefaDependente(sys, "task2", 8.0)
        task3 = TarefaDependente(sys, "task3", 6.0)
        task4 = TarefaDependente(sys, "task4", 3.0)
        task5 = TarefaDependente(sys, "task5", 17.0)
        task6 = TarefaDependente(sys, "task6", 15.0)
        task7 = TarefaDependente(sys, "task7", 13.0)
        task8 = TarefaDependente(sys, "task8", 11.0)
        task1 += task3
        task2 += task4
        task3 += task8
        task4 += task5
        task5 += task6
        task3 += task5
        task5 += task7
        path = sys.caminho_critico()
        self.assertTrue(all(task.critica() for task in path))
    def test_late_start(self):
        sys = Sistema()
        task1 = TarefaDependente(sys, "task1", 12.0)
        task2 = TarefaDependente(sys, "task2", 8.0)
        task3 = TarefaDependente(sys, "task3", 6.0)
        task4 = TarefaDependente(sys, "task4", 3.0)
        task5 = TarefaDependente(sys, "task5", 17.0)
        task6 = TarefaDependente(sys, "task6", 15.0)
        task7 = TarefaDependente(sys, "task7", 13.0)
        task8 = TarefaDependente(sys, "task8", 11.0)
        task1 += task3
        task2 += task4
        task3 += task8
        task4 += task5
        task5 += task6
        task3 += task5
        task5 += task7
        path = sys.caminho_critico()
        self.assertEqual(7,task2.folga())
        self.assertEqual(21,task8.folga())

    def test_change_desc(self):
        sys = Sistema()
        task1 = TarefaDependente(sys, "task1", 12.0)
        task1.descricao("new_desc")
        self.assertTrue("task1" not in sys and "new_desc" in sys)

    def test_sorvedor(self):
        sys = Sistema()
        task1 = TarefaDependente(sys, "task1", 12.0)
        task2 = TarefaDependente(sys, "task2", 8.0)
        task3 = TarefaDependente(sys, "task3", 6.0)
        task4 = TarefaDependente(sys, "task4", 3.0)
        task5 = TarefaDependente(sys, "task5", 17.0)
        task6 = TarefaDependente(sys, "task6", 15.0)
        task7 = TarefaDependente(sys, "task7", 13.0)
        task8 = TarefaDependente(sys, "task8", 11.0)
        task1 += task3
        task2 += task4
        task3 += task8
        task4 += task5
        task5 += task6
        task3 += task5
        task5 += task7
        self.assertEqual((task1, task2), sys.sorvedoro())

    def test_sorvedor(self):
        sys = Sistema()
        task1 = TarefaDependente(sys, "task1", 12.0)
        task2 = TarefaDependente(sys, "task2", 8.0)
        task3 = TarefaDependente(sys, "task3", 6.0)
        task4 = TarefaDependente(sys, "task4", 3.0)
        task5 = TarefaDependente(sys, "task5", 17.0)
        task6 = TarefaDependente(sys, "task6", 15.0)
        task7 = TarefaDependente(sys, "task7", 13.0)
        task8 = TarefaDependente(sys, "task8", 11.0)
        task1 += task3
        task2 += task4
        task3 += task8
        task4 += task5
        task5 += task6
        task3 += task5
        task5 += task7
        self.assertEqual((task6, task7, task8), sys.fonte())

if __name__ == '__main__':
    unittest.main()
