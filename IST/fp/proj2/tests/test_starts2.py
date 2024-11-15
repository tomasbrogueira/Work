from Sistema import *
sys = Sistema()
t1 = TarefaDependente(sys, 'task 1', 341)
t2 = TarefaDependente(sys, 'task 2', 941)
t3 = TarefaDependente(sys, 'task 3', 958)
t4 = TarefaDependente(sys, 'task 4', 789)
t5 = TarefaDependente(sys, 'task 5', 166)
t6 = TarefaDependente(sys, 'task 6', 577)
t7 = TarefaDependente(sys, 'task 7', 690)
t8 = TarefaDependente(sys, 'task 8', 779)
t9 = TarefaDependente(sys, 'task 9', 721)
t10 = TarefaDependente(sys, 'task 10', 710)
t11 = TarefaDependente(sys, 'task 11', 894)
t12 = TarefaDependente(sys, 'task 12', 272)
t13 = TarefaDependente(sys, 'task 13', 38)
t14 = TarefaDependente(sys, 'task 14', 607)
t15 = TarefaDependente(sys, 'task 15', 874)
t16 = TarefaDependente(sys, 'task 16', 997)
t17 = TarefaDependente(sys, 'task 17', 68)
t18 = TarefaDependente(sys, 'task 18', 625)
t19 = TarefaDependente(sys, 'task 19', 485)
t20 = TarefaDependente(sys, 'task 20', 373)
t20 += t10
t17 += t11
t14 += t4
t8 += t3
t18 += t14
t3 += t2
t12 += t5
t16 += t13
t19 += t18
t15 += t3
t19 += t7
t20 += t2
t18 += t3
t19 += t14
t11 += t3
t16 += t14
t17 += t14
t9 += t2
t20 += t11
t20 += t18
t11 += t10
t2 += t1
t17 += t2
t9 += t4
t17 += t15
t19 += t10
t10 += t9
t13 += t3
t11 += t4
t18 += t9
t13 += t2
t13 += t11
t18 += t15
t13 += t8
t14 += t5
t15 += t2
t13 += t1
t18 += t16
t20 += t3
t9 += t1
import time
start = time.time()
print(duracao(sys.caminho_critico()))
end = time.time()
print('took', end - start, 'seconds')
print('t0:', 't0.inicio()', 't0.final()', 't0.folga()')
print('t1:', t1.inicio(), t1.inicio() + t1.folga(), t1.folga(), t1 in sys.fonte(), t1 in sys.sorvedoro())
print('t2:', t2.inicio(), t2.inicio() + t2.folga(), t2.folga(), t2 in sys.fonte(), t2 in sys.sorvedoro())
print('t3:', t3.inicio(), t3.inicio() + t3.folga(), t3.folga(), t3 in sys.fonte(), t3 in sys.sorvedoro())
print('t4:', t4.inicio(), t4.inicio() + t4.folga(), t4.folga(), t4 in sys.fonte(), t4 in sys.sorvedoro())
print('t5:', t5.inicio(), t5.inicio() + t5.folga(), t5.folga(), t5 in sys.fonte(), t5 in sys.sorvedoro())
print('t6:', t6.inicio(), t6.inicio() + t6.folga(), t6.folga(), t6 in sys.fonte(), t6 in sys.sorvedoro())
print('t7:', t7.inicio(), t7.inicio() + t7.folga(), t7.folga(), t7 in sys.fonte(), t7 in sys.sorvedoro())
print('t8:', t8.inicio(), t8.inicio() + t8.folga(), t8.folga(), t8 in sys.fonte(), t8 in sys.sorvedoro())
print('t9:', t9.inicio(), t9.inicio() + t9.folga(), t9.folga(), t9 in sys.fonte(), t9 in sys.sorvedoro())
print('t10:', t10.inicio(), t10.inicio() + t10.folga(), t10.folga(), t10 in sys.fonte(), t10 in sys.sorvedoro())
print('t11:', t11.inicio(), t11.inicio() + t11.folga(), t11.folga(), t11 in sys.fonte(), t11 in sys.sorvedoro())
print('t12:', t12.inicio(), t12.inicio() + t12.folga(), t12.folga(), t12 in sys.fonte(), t12 in sys.sorvedoro())
print('t13:', t13.inicio(), t13.inicio() + t13.folga(), t13.folga(), t13 in sys.fonte(), t13 in sys.sorvedoro())
print('t14:', t14.inicio(), t14.inicio() + t14.folga(), t14.folga(), t14 in sys.fonte(), t14 in sys.sorvedoro())
print('t15:', t15.inicio(), t15.inicio() + t15.folga(), t15.folga(), t15 in sys.fonte(), t15 in sys.sorvedoro())
print('t16:', t16.inicio(), t16.inicio() + t16.folga(), t16.folga(), t16 in sys.fonte(), t16 in sys.sorvedoro())
print('t17:', t17.inicio(), t17.inicio() + t17.folga(), t17.folga(), t17 in sys.fonte(), t17 in sys.sorvedoro())
print('t18:', t18.inicio(), t18.inicio() + t18.folga(), t18.folga(), t18 in sys.fonte(), t18 in sys.sorvedoro())
print('t19:', t19.inicio(), t19.inicio() + t19.folga(), t19.folga(), t19 in sys.fonte(), t19 in sys.sorvedoro())
print('t20:', t20.inicio(), t20.inicio() + t20.folga(), t20.folga(), t20 in sys.fonte(), t20 in sys.sorvedoro())
last_tsk = None
for tsk in sys.caminho_critico():
	print(tsk.representacao())
	print(tsk in sys.fonte(), last_tsk in tsk, tsk in sys.sorvedoro())
	last_tsk = tsk
