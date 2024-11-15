from Utilizador import Utilizador

class Grupo(Utilizador):
    '''
    a classe Grupo herda todos os atributos do Utilizador,
    um grupo tem também uma lista com os utilizadores e uma duração associada
    '''
    def __init__(self,sys,identificador,descricao):
        #init da classe superior(Utilizador)
        super().__init__(sys,identificador,descricao)
        self.__users = set()
        self.__dur = 0.0

    def detecao_ciclos(self,user):
        '''
        recebe um t_dep e uma tarefa,
        deteta ciclos de dependencias usando recursão e retorna um boolean
        '''
        if not user:
            return False

        if self in user:
            return True

        #verificar recursivamente se há algum ciclo nas dependentes
        for sub_user in user:
            if self.detecao_ciclos(sub_user):
                return True
        return False

    def __iadd__(self,user):
        '''
        recebe um grupo e um argumento,
        verifica se o argumento é um user/grupo,
        adiciona o user/grupo à lista de users do primeiro grupo
        devolve o primeiro grupo
        '''
        #se for um grupo verifica que não recebeu o mesmo grupo duas vezes
        if not isinstance(user, (Utilizador,Grupo)) or self is user or self._sys != user.sistema():
            raise ValueError('operação inválida')

        if self.detecao_ciclos(user):
            raise ValueError('ciclo criado no grupo')

        user._grupo.append(self)
        self.__users.add(user)
        return self

    def __isub__(self,user):
        '''
        recebe um grupo e um argumento,
        faz as mesmas verificações que o __iadd__,
        remove o user/grupo da lista de users do primeiro grupo,
        devolve o primeiro grupo
        '''
        if not isinstance(user, (Utilizador,Grupo)) or self is user:
            raise ValueError('operação inválida')

        self.__users.remove(user)
        return self

    def __len__(self) -> int:
        '''
        recebe um grupo,
        retorna o numero de utlizadores do grupo
        '''
        return len(self.__users)

    def __iter__(self):
        '''
        recebe um grupo,
        itera sobre os users do grupo
        '''
        return iter(self.__users)

    def tempo(self, dur : float) -> None:
        '''
        recebe um grupo e uma duração (float/int)
        adiciona a duração ao grupo e distribui igualmente pelos users
        '''
        self.__dur += dur
        for user in self.__users:
            user.tempo(dur/len(self.__users))

    def __str__(self) -> str:
        '''
        recebe um grupo,
        devolve uma string semelhante à str() do utilizador
            (com a adição do numero de users do grupo)
        '''
        return f"{self._identificador}:{self.__dur}" \
        f":{len(self._tarefas)}:{self._descricao}:{len(self)}"
