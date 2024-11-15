def duracao(caminho : list):
    '''
    calcula a duração do caminho somando as durações das suas tarefa
    '''
    return sum(tarefa.get_duracao() for tarefa in caminho)
