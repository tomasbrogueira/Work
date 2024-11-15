class Utilizador:
    '''
    a classe utilizador verifica as mesmas condições que o utilizador do kanban
    '''
    def __init__(self,sys,identificador,descricao) -> None:
        if not isinstance(identificador,str) or not isinstance(descricao,str):
            raise ValueError('cria_utilizador: argumentos inválidos')

        if not 1 <= len(identificador) <= 12 or ':' in identificador \
            or not descricao.replace(' ','').isalpha() or len(descricao) < 12 :
            raise ValueError('cria_utilizador: argumentos inválidos')

        self._identificador = identificador
        self._dur = 0.0
        self._descricao = descricao
        self._tarefas = []
        self._sys = sys
        #adiciona o utilizador aos utilizadores do sistema
        sys.utilizador(self)
        self._grupo = []

    def tempo(self,dur : float) -> None:
        '''
        recebe um user e um float/int,
        adiciona a duração recebida ao tempo do user
        '''
        self._dur += dur

    def tarefas(self):
        '''
        recebe um user,
        devolve uma str com as descrições das atividades do user oredenadas
        '''

        ordenadas = sorted([t.get_descricao() for t in self.tarefa_grupo()])
        return ''.join(desc +'\n' for desc in ordenadas)

    def tarefa_grupo(self):
        '''
        função auxiliar para ir buscar as tarefas do grupo
        '''
        tasks = self._tarefas
        for user in self._grupo:
            tasks += user.tarefa_grupo()

        return tasks

    def insere(self,tarefa):
        '''
        recebe um user e uma tarefa,
        insere a tarefa nas tarefas do user
        '''
        self._tarefas.append(tarefa)

    def remove(self,tarefa):
        '''
        recebe um user e uma tarefa,
        remove a tarefa das tarefas do user
        '''
        self._tarefas.remove(tarefa)

    def sistema(self):
        '''
        recebe utilizador,
        devolve o seu sistema
        '''
        return self._sys

    def __iter__(self):
        '''
        retorna um iterador para uma lista vazia
        '''
        return iter([])

    def __str__(self) -> str:
        '''
        reescreve user recebido em str,
        troca a lista de tarefas pelo número de tarefas associado
        '''
        return f"{self._identificador}:{self._dur}" \
        f":{len(self._tarefas)}:{self._descricao}"
