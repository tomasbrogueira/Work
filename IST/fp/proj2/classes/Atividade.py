class Atividade:
    '''
    a classe atividade verifica as mesmas condições que a atividade do kanban
    '''
    def __init__(self,sys,descricao) -> None:
        if not 4 <= len(descricao) <= 12 or not isinstance(descricao,str)\
        or not descricao.isupper() or not descricao.replace('_','').isalpha():
            raise ValueError(': cria_atividade: argumentos inválidos')

        self.__descricao = descricao
        self.__tarefas = []
        self._sys = sys
        #adiciona a atividade às atividades do sistema
        sys.atividade(self)

    def descricao(self) -> str:
        '''
        recebe uma atividade,
        devolve a descrição da atividade
        '''
        return self.__descricao

    def insere(self,tarefa) -> None:
        '''
        recebe uma atividade e uma tarefa,
        insere a tarefa na lista de tarefas da atividade
        '''
        self.__tarefas.append(tarefa)

    def remove(self,tarefa) -> None:
        '''
        recebe uma atividade e uma tarefa,
        remove a tarefa da lista de tarefas da atividade
        '''
        self.__tarefas.remove(tarefa)

    def tarefas(self) -> tuple:
        '''
        recebe uma atividade,
        devolve um tuplo com as tarefas da atividade oranizadas pela descrição
        '''
        #usa o predicado get_descricao() no sorted para fazer a organização
        return tuple(sorted(self.__tarefas, key=lambda t: t.get_descricao()))

    def sistema(self):
        '''
        recebe uma atividade,
        retorna o seu sistema
        '''
        return self._sys
