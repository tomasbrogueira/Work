from math import inf
from Atividade import Atividade
from Tarefa import Tarefa
from TarefaDependente import TarefaDependente
from Utilizador import Utilizador
from Grupo import Grupo
from auxiliares import duracao

class Sistema:
    '''
    cria a classe Sistema que engloba tudo o resto:
        lista de atividades  (1)
        lista de users       (2)
        lista de tarefas     (3)
    '''
    def __init__(self):
        self.__atividades = []
        self.__users = []
        self.__tarefas = []
        #a atividade inicial é a to_do
        self.__ativ_to_do = Atividade(self,'TO_DO')
        #os metodos crit vão servir para calcular o caminho crítico
        self.__dur_crit = 0
        self.__caminho_crit = []

    def atividade(self,ativ):
        '''
        recebe um sistema e uma atividade,
        adiciona a atividade à (1)
        '''
        self.__atividades.append(ativ)

    def atividades(self) -> list:
        '''
        recebe um sistema,
        devolve a (1)
        '''
        return self.__atividades

    def to_do(self):
        '''
        retorna a atividade to_do
        '''
        return self.__ativ_to_do

    def utilizador(self,user):
        '''
        recebe um sistema e um user,
        adiciona a atividade à (2)
        '''
        self.__users.append(user)

    def utilizadores(self):
        '''
        recebe um sistema,
        devolve a (2)
        '''
        return self.__users

    def tarefa(self,tarefa):
        '''
        recebe um sistema e uma tarefa,
        adiciona a atividade à (3)
        '''
        self.__tarefas.append(tarefa)

    def tarefas(self) -> list:
        '''
        recebe um sistema,
        devolve a (3)
        '''
        return self.__tarefas

    def __contains__(self,tarefa : str) -> bool:
        '''
        recebe um sistema e uma tarefa,
        devolve o valor boolean da existência da tarefa no sistema
        '''
        return tarefa in [tsk.get_descricao() for tsk in self.__tarefas]

    def get_dur_crit(self):
        '''
        recebe um sistema,
        devolve a duração crítica
        '''
        return self.__dur_crit

    def fonte(self) -> tuple:
        #usa se a lambda function para ordenar pela descrição (o sorted usa pred)
        '''
        recebe um sistema,
        retorna um tuplo com as fontes ordenadas
        '''
        return tuple(sorted([tarefa for tarefa in self.__tarefas \
            if len(tarefa) == 0] , key = lambda t : t.get_descricao()))

    def sorvedoro(self) -> tuple:
        '''
        recebe um sistema,
        retorna um tuplo com os sorvedores ordenados
        '''
        return tuple(sorted([tarefa for tarefa in self.__tarefas \
            if not tarefa.associadas()],key = lambda t : t.get_descricao()))

    def e_start_recur (self,tarefa):
        '''
        recebe sistema e uma tarefa,
        devolve o early start da tarefa e atualiza os early starts por que passa
        '''
        #usa o iterador das tarefas dependentes
        if not tarefa.dependentes():
            return 0

        #otimização usando programação dinâmica
        if tarefa.inicio() != 0 :
            return tarefa.inicio()

        for t_dep in tarefa:
            tarefa.set_early(max(tarefa.inicio(), t_dep.get_duracao() + self.e_start_recur(t_dep)))

        return tarefa.inicio()

    def l_start_recur(self,tarefa):
        '''
        recebe sistema e uma tarefa,
        devolve o late start da tarefa e atualiza os early starts por que passa
        '''
        if not tarefa.associadas():
            tarefa.set_late(self.__dur_crit - tarefa.get_duracao())
            return tarefa.fim()

        #otimização usando programação dinâmica
        if tarefa.fim() != inf :
            return tarefa.fim()

        for t_assoc in tarefa.associadas():
            tarefa.set_late(min(tarefa.fim(), self.l_start_recur(t_assoc) - tarefa.get_duracao()))

        return tarefa.fim()

    def explorador(self, caminho : list) -> None:
        '''
        recebe sistema e caminho (list),
        faz uma pesquisa para encontrar o caminho critico
        '''
        tarefa = caminho[-1]

        if not tarefa.associadas():
            if duracao(caminho) == self.__dur_crit:
                #cria uma copia do caminho critico para ele nao se alterar
                self.__caminho_crit = caminho.copy()

        for tsk in tarefa.associadas():
            if tsk.critica():
            #adiciona tarefa ao final do caminho para a recursao
            #depois limpa para o caminho ficar inalterado
                caminho.append(tsk)
                self.explorador(caminho)
                caminho.remove(tsk)

    def caminho_critico(self):
        '''
        recebe sistema,
        atualiza as durações críticas
        devolve um tuplo com o caminho crítico
        '''
        for tarefa in self.__tarefas:
            tarefa.limpa()

        for sorvedoro in self.sorvedoro():
            #calcula a dur crit tirando o max
            #entre o early finish de cada sorvedoro com o valor guardado
            e_finish = self.e_start_recur(sorvedoro) + sorvedoro.get_duracao()
            self.__dur_crit = max(e_finish,self.__dur_crit)

        for fonte in self.fonte():
            #atualiza o late start de todas as tarefas
            self.l_start_recur(fonte)

        for fonte in self.fonte():
            #a dora precisa dos late e early starts calculados para conseguir explorar
            self.explorador([fonte])

        return tuple(self.__caminho_crit)
