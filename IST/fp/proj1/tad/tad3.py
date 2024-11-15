"""
TAD utilizador com listas
"""

def _utilizador_attr(ident: str, desc: str) -> bool:
    ''' 2.2.0 verifica argumentos ident e desc '''
    return not isinstance(ident, str) or len(ident) == 0 or len(ident) > 12 \
        or ident.find(':') >= 0 or not isinstance(desc, str) \
        or len(desc) < 12 \
        or any((not(ch.isalpha() or ch == ' ') for ch in desc))
def cria_utilizador(ident: str, desc: str):
    ''' 2.2.1 cria_utilizador: str x str -> utilizador '''
    if _utilizador_attr(ident, desc):
        raise ValueError('cria_utilizador: argumentos inválidos')
    return [ident, desc, 0.0, []] # [str, str, tempo, tasks]

def eh_utilizador(obj: any) -> bool:
    ''' 2.2.2 eh_utilizador: any -> bool '''
    return isinstance(obj, list) and len(obj) == 4 \
        and not _utilizador_attr(obj[0], obj[1]) \
        and isinstance(obj[2], float) and obj[2] >= 0.0 \
        and isinstance(obj[3], list) \
        and all((tsk in tarefas() for tsk in obj[3]))

def utilizador_str(user) -> str:
    ''' 2.2.3 utilizador_str: utilizador -> str '''
    return user[0] + ':' + str(user[2]) + ':' + str(len(user[3])) + ':' + user[1]

def utilizador_tarefas(user) -> str:
    ''' 2.2.4 utilizador_tarefas: utilizador -> str '''
    if not user[3]:
        return ''
    tsks = [tarefa_representacao(tsk)[0] + '\n' for tsk in user[3]]
    tsks.sort()
    return ''.join(tsks)

# funções auxiliares para garantir as barreiras de abstração
def utilizador_tempo(user, dur: int):
    ''' 2.2.5 utilizador_tempo: user: utilizador x dur: int '''
    if isinstance(dur, (int,float)) and dur >= 0:
        user[2] += dur

def utilizador_insere(user, tsk):
    ''' 2.2.5 utilizador_insere: user: utilizador x tsk: tarefa '''
    if tsk not in user[3]:
        user[3] += [tsk]

def utilizador_remove(user, tsk):
    ''' 2.2.5 utilizador_remove: user: utilizador x tsk: tarefa '''
    if tsk in user[3]:
        del user[3][user[3].index(tsk)]

"""
Criação de um sistema kanban
"""
__author__ = 'ist1106754 Tomás Brogueira'
__version__ = 1.0
_atividade_to_do = {'descricao' : 'TO_DO', 'tarefas' : []}
_lista_atividades = [_atividade_to_do]
_lista_utilizadores = []
_lista_tarefas = []
# funções relativas às atividades
################################################################################
# atividade := {                                                               #
#        'descricao' : descricao da atividade (str) ,                          #
#        'tarefas' : lista de tarefas associadas à atividade                   #
#        }                                                                     #
################################################################################
def cria_atividade(descricao : str) -> dict :
    '''
    cria uma representação duma atividade com a descricao recebida
    e as caracteríscticas(valores associados) default duma atividade
    '''
    if not 4 <= len(descricao) <= 12 or not isinstance(descricao,str) :
        raise ValueError(': cria_atividade: argumentos inválidos')
    if not descricao.isupper() or not descricao.replace('_','').isalpha():
        raise ValueError(': cria_atividade: argumentos inválidos')
    atividade = {
        'descricao' : descricao ,
        'tarefas' : []
    }
    _lista_atividades.append(atividade)
    return atividade
def eh_atividade(hipotese : any) -> bool :
    '''
    verifica se o argumento é uma atividade usando a _lista_atividades
    '''
    return hipotese in _lista_atividades
def atividade_descricao(atividade : dict) -> str :
    '''
    recebe uma atividade e devolve a sua descrição
    '''
    return atividade['descricao']
def atividade_tarefas(atividade : dict) -> tuple :
    '''
    reorganiza a lista das tarefas presente no dicionário da atividade
    '''
    lista_tsk = []
    for tarefa in atividade['tarefas']:
        lista_tsk.append([tarefa_representacao(tarefa)[0], tarefa])
    lista_tsk.sort()
    nova_lista = [tsk[1] for tsk in lista_tsk]
    return tuple(nova_lista)
# funções auxiliares (atividades)
def atividade_to_do() -> dict :
    '''
    devolve a _atividade_to_do no seu estado atual
    '''
    return _atividade_to_do
def atividade_insere(act: dict, tarefa):
    '''
    insere a tarefa recebida na lista de tarefas da atividade
    '''
    act['tarefas'].append(tarefa)
def atividade_remove(act: dict, tarefa):
    '''
    remove a tarefa recebida da lista de tarefas da atividade
    '''
    act['tarefas'].remove(tarefa)
# funções relativas ao utilizador
################################################################################
# utilizador := {                                                              #
#        'id' : identificador do user (str) ,                                  #
#        'dur' : tempo gasto pelo utilizador nas tarefas (float) ,             #
#        'tarefas' : lista que contém as tarefas associadas ao utilizador ,    #
#        'descricao' : descrição do utilizador (str)                           #
#        }                                                                     #
################################################################################
# funções auxiliares (utilizadores)
# funções relativas às tarefas
################################################################################
# tarefa := {                                                                  #
#        'descricao' : descrição da tarefa (str) ,                             #
#        'dur_prev' : duração prevista da tarefa (float) ,                     #
#        'dur_utiliz' : tempo utilizado na tarefa (float) ,                    #
#        'user' : utilizador a que a tarefa está associada ,                   #
#        'atividade' : atividade a que a tarefa está associada                 #
#        }                                                                     #
################################################################################
def cria_tarefa(descricao : str , dur : float) -> dict :
    '''
    cria tarefa com descrição, dur prevista(int ou float) e valores triviais
    '''
    if not isinstance(descricao , str) or not isinstance(dur , (float,int)):
        raise ValueError('cria_tarefa: argumentos inválidos')
    if descricao.isspace() or dur < 0:
        raise ValueError('cria_tarefa: argumentos inválidos')
    to_do = atividade_to_do()
    nova_tarefa = {
        'descricao' : descricao,
        'dur_prev' : dur,
        'dur_utiliz' : 0.0,
        'user' : None,
        'atividade' : to_do
    }
    for tarefa in  tarefas():
        if tarefa['descricao'] == descricao :
            raise ValueError('cria_tarefa: argumentos inválidos')
    atividade_insere(to_do, nova_tarefa)
    tarefas().append(nova_tarefa)
    return nova_tarefa
def eh_tarefa(hipotese : any) -> bool :
    '''
    verifica se a tarefa está na _lista_tarefas
    '''
    return hipotese in tarefas()
def tarefa_atividade(tarefa : dict) -> str :
    '''
    devolve a atividade a que uma tarefa esta ligada
    '''
    return tarefa['atividade']
def tarefa_representacao(tarefa : dict) -> tuple :
    '''
    representa a tarefa num tuplo
    '''
    desc_tarefa = tarefa['descricao']
    desc_ativ = atividade_descricao(tarefa['atividade'])
    dur_prev, dur_utiliz = tarefa['dur_prev'], tarefa['dur_utiliz']
    user = tarefa['user']
    if user is None:
        user = ''
    else:
        user = utilizador_str(tarefa['user']).split(':' , maxsplit = -1)[0]
    return desc_tarefa, desc_ativ, user, dur_prev, dur_utiliz
def tarefa_colaborador(tarefa : dict , user , dur : float = 0.0) -> dict :
    '''
    altera o user associado a uma tarefa,
    contabiliza os tempos da tarefa e do user
    '''
    if not isinstance(dur , float) or dur < 0 :
        raise ValueError('tarefa_colaborador: operação inválida')
    if tarefa['user'] is not None :
        utilizador_remove(tarefa['user'], tarefa)
        utilizador_tempo(tarefa['user'], dur)
    utilizador_insere(user, tarefa)
    tarefa['user'] = user
    tarefa['dur_utiliz'] += dur
    return tarefa
def tarefa_move(tarefa : dict , atividade , dur = 0.0) -> dict :
    '''
    trocar a atividade da tarefa,
    contabilizar o tempo(int ou float) do user e da tarefa
    '''
    if tarefa['user'] is None or not isinstance(dur , (float,int)) or dur < 0:
        raise ValueError('tarefa_move: operação inválida')
    user = tarefa['user']
    if atividade == atividade_to_do():
        tarefa['dur_utiliz'] = 0.0
        tarefa['user'] = None
        utilizador_remove(user, tarefa)
    atividade_remove(tarefa['atividade'], tarefa)
    atividade_insere(atividade, tarefa)
    tarefa['dur_utiliz'] += dur
    tarefa['atividade'] = atividade
    utilizador_tempo(tarefa['user'],dur)
    return tarefa
def tarefa_atraso(tarefa : dict) -> float :
    '''
    devolve a diferença entre a duração prevista e o tempo já gasto da tarefa
    '''
    return tarefa['dur_prev'] - tarefa['dur_utiliz']
def tarefa_descricao(tarefa : dict , descricao : str) -> str :
    '''
    altera a descrição da tarefa e devolve a antiga
    '''
    for tsk in tarefas():
        if tsk['descricao'] == descricao:
            raise ValueError
    descricao_antiga = tarefa['descricao']
    tarefa['descricao'] = descricao
    return descricao_antiga
# função auxiliar de tarefas
def tarefas():
    '''
    retorna a lista de tarefas existentes
    '''
    return _lista_tarefas
# a função tarefas foi criada caso houve-se necessidade de garantir barreiras
# de abestração, no entanto não surgiu essa necessidade
# a função tarefas() foi na mesma implementada como sugeria no enunciado
