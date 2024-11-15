from random import random
def euromilhoes():
    chave = [[],[]]
    while len(chave[0]) < 5:
        x = int((random()*50)//1)
        if chave[0].count(x) == 0 :
            chave[0].append(x)
    while len(chave[1]) < 2:
        x = int((random()*12)//1)
        if chave[1].count(x) == 0 :
            chave[1].append(x)
    return chave
'''
import random
def euromilhoes():
    output = []
    first = []
    second = []
    for x in range(5):
        first.append(random.randrange(1,50))
    output.append(first)
    for x in range(2):
        second.append(random.randrange(1,12))
    output.append(second)
    return output
'''