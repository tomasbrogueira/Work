from math import inf
from Tarefa import Tarefa

class TarefaDependente(Tarefa):
    '''
    a classe TarefaDependente herda todos os atributos da Tarefa,
    uma TarefaDependente (t_dep) tem também:
        uma lista com as tarefas dependentes dela (1)
        uma lista com as tarefas de que depende   (2)
        um early e um late start
    '''#uma lista com tarefas visitadas usada para detetar ciclos

    def __init__(self , sys , descricao : str , dur : float):
        super().__init__(sys,descricao,dur)
        self.__tsks_dep = set()
        '''tarefas atrás'''
        self.__associadas = []
        '''tarefas à frente'''
        self.__early_start = 0
        self.__late_start = inf

    def dependentes(self):
        '''
        recebe uma t_dep,
        retorna as tarefas dependentes da t_dep
        '''
        return self.__tsks_dep

    def associadas(self):
        '''
        recebe uma t_dep,
        retorna as tarefas de que a t_dep depende
        '''
        return self.__associadas

    def add_associada(self,tarefa):
        '''
        recebe uma t_dep e uma tarefa,
        adiciona a tarefa à lista (2)
        '''
        self.__associadas.append(tarefa)

    def sub__associadas(self,tarefa):
        '''
        recebe uma t_dep e uma tarefa,
        remove uma tarefa da lista (2)
        '''
        self.__associadas.remove(tarefa)


    def detecao_ciclos(self,tarefa):
        '''
        recebe um t_dep e uma tarefa,
        deteta ciclos de dependencias usando recursão e retorna um boolean
        '''
        if not tarefa:
            return False

        if self in tarefa:
            return True

        #verificar recursivamente se há algum ciclo nas dependentes
        for t_dep in tarefa:
            if self.detecao_ciclos(t_dep):
                return True
        return False


    def __iadd__(self , tsk_dep: Tarefa):
        '''
        recebe uma t_dep(instância) e uma tarefa,
        adiciona a tarefa às dependentes e associa a instância à tarefa dependente
        '''
        if not isinstance(tsk_dep,TarefaDependente) or super().get_sys() is not tsk_dep.get_sys():
            raise ValueError('argumento inválido')

        self.__tsks_dep.add(tsk_dep)
        tsk_dep.add_associada(self)

        if self.detecao_ciclos(tsk_dep):
            raise ValueError('tarefa adicionada cria um ciclo')

        return self

    def __isub__(self, tsk_dep):
        '''
        recebe uma t_dep(instância) e uma tarefa,
        remove a tarefa das dependentes e desassocia a instancia à tarefa dependente
        '''
        self.__tsks_dep.remove(tsk_dep)
        tsk_dep.sub_associada(self)
        return self

    def __len__(self) -> float:
        '''
        recebe tarefa,
        devolve o numero de tarefas que dependem da tarefa
        '''
        return len(self.__tsks_dep)

    def __iter__(self) -> bool:
        '''
        recebe uma lista,
        itera sobre os seus termos (devolve os termos um de cada vez)
        '''
        return iter(self.__tsks_dep)

    def inicio(self) -> float :
        '''
        recebe uma tarefa,
        devolve o seu early start
        '''
        return self.__early_start

    def fim(self) -> float:
        '''
        recebe uma tarefa,
        devolve o seu late start
        '''
        return self.__late_start

    def folga(self) -> float :
        '''
        recebe uma tarefa,
        retorna a diferença entre o late e o early start
        '''
        return self.__late_start - self.__early_start

    def critica(self) -> bool:
        '''
        recebe uma tarefa,
        retorna True se a tarefa não tiver folga (tarefa crítica)
        '''
        return self.folga() == 0

    def limpa(self):
        '''
        recebe uma tarefa,
        dá reset aos valores de early e late start
        '''
        self.__early_start = 0
        self.__late_start = inf


    #cuidado so se pode mexer com os starts no caminho critico
    def set_early(self,dur : float):
        '''
        recebe uma tarefa e uma duração (float/int),
        atribui ao early start o valor da duração recebido
        '''
        self.__early_start = dur

    def set_late(self,dur):
        '''
        recebe uma tarefa e uma duração (float/int),
        atribui ao late start o valor da duração recebido
        '''
        self.__late_start = dur
