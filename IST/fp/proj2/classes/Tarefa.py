class Tarefa:
    def __init__(self,sys,descricao : str,dur : float) -> None:
        '''
        a classe tarefa verifica as mesmas condições que a tarefa do kanban
        '''
        if not isinstance(descricao , str) or not isinstance(dur , (float,int))\
            or descricao.isspace() or dur < 0:
            raise ValueError('cria_tarefa: argumentos inválidos')

        self._descricao = descricao
        self._dur_prev = dur
        self._dur_utiliz = 0.0
        self._user = None
        self._sys = sys
        #insere a tarefa nas tarefas do sistema
        sys.tarefa(self)
        #a tarefa é colocada na atividade to_do
        self._atividade = sys.to_do()
        sys.to_do().insere(self)

    def atividade(self):
        '''
        recebe uma tarefa,
        retorna a atividade a que a tarefa está associada
        '''
        return self._atividade

    def colaborador(self , user , dur : float = 0.0):
        '''
        recebe um tarefa, um user e uma duração (float/int),
        altera o user associado à tarefa,
        contabiliza os tempos da tarefa e do user
        '''
        if not isinstance(dur , float) or dur < 0 or self._sys != user.sistema():
            raise ValueError('tarefa_colaborador: operação inválida')

        #remover a tarefa da lista de tarefas do user e adicionar à lista do novo user
        if self._user is not None:
            self._user.remove(self)
            self._user.tempo(dur)

        user.insere(self)
        self._user = user
        self._dur_utiliz += dur

        return self


    def move(self , atividade , dur : float = 0.0):
        '''
        recebe uma tarefa, uma atividade e uma duração (float/int),
        troca a atividade da tarefa,
        contabiliza o tempo(int ou float) do user e da tarefa
        '''
        if self._user is None or not isinstance(dur , (float,int)) or dur < 0 or self._sys != atividade.sistema():
            raise ValueError('tarefa_move: operação inválida')

        if atividade is self._sys.to_do():
            self._dur_utiliz = 0.0
            self._user = None
            self._user.remove(self)

        #remover a tarefa da lista de tarefas da atividade e adicionar à lista da nova atividade
        self._atividade.remove(self)
        atividade.insere(self)

        self._dur_utiliz += dur
        self._atividade = atividade
        self._user.tempo(dur)

        return self

    def atraso(self):
        '''
        recebe uma tarefa,
        devolve a diferença entre o tempo previsto e o tempo já gasto na tarefa
        '''
        return self._dur_prev - self._dur_utiliz

    def descricao(self , descricao):
        '''
        recebe uma tarefa e uma descrição,
        verifica se a descrição já exite no sistema,
        altera a descrição da tarefa e devolve a antiga
        '''
        if descricao in self._sys:
            raise ValueError('tarefa_descricao: operação_inválida')

        descricao_antiga = self._descricao
        self._descricao = descricao

        return descricao_antiga

    def get_descricao(self):
        '''
        recebe uma tarefa,
        devolve a sua descrição
        '''
        return self._descricao

    def get_duracao(self):
        '''
        recebe uma tarefa,
        devolve a sua duração prevista
        '''
        return self._dur_prev

    def get_sys(self):
        '''
        recebe uma tarefa,
        devolve o sistema em que está
        '''
        return self._sys

    def representacao(self) -> tuple:
        '''
        recebe uma tarefa,
        representa a tarefa num tuplo
        '''
        user = ''
        if self._user is not None:
            #so da split ao primeiros ":" (maxsplit=1)
            user = str(self._user).split(':',maxsplit=1)[0]

        return (self._descricao , self._atividade.descricao(), \
        user , self._dur_prev , self._dur_utiliz)

    def __iter__(self):
        '''
        retorna um iterador para uma lista vazia
        '''
        return iter([])
