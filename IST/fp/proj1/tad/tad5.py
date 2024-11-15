"""
TAD tarefa com listas
"""

def cria_tarefa(desc: str, dur: int):
    ''' 2.3.1 cria_tarefa: str x float -> tarefa '''
    if not isinstance(desc, str) or not desc.strip() \
        or desc in _todas() \
        or not isinstance(dur, (int,float)) or dur < 0:
        raise ValueError('cria_tarefa: argumentos inválidos')
    tsk = [desc, float(dur), atividade_to_do(), None, 0.0]
    _todas()[desc] = tsk
    atividade_insere(atividade_to_do(), tsk)
    return tsk # [str, float, act, user, float]

def eh_tarefa(obj: any) -> bool:
    ''' 2.3.2 eh_tarefa: any -> bool '''
    return isinstance(obj, list) and len(obj) == 5 and isinstance(obj[0], str) \
    and isinstance(obj[1], float) and eh_atividade(obj[2]) \
    and (obj[3] is None or eh_utilizador(obj[3])) and isinstance(obj[4], float) \
    and obj[1] >= 0 and obj[4] >= 0

def tarefa_atividade(tsk):
    ''' 2.3.3 tarefa_atividade: tarefa -> atividade '''
    return tsk[2]

def tarefa_representacao(tsk) -> tuple:
    ''' 2.3.4 tarefa_representacao: tarefa -> tuple '''
    ident = utilizador_str(tsk[3]).split(':')[0] if tsk[3] else ''
    return tsk[0], atividade_descricao(tsk[2]), ident, tsk[1], tsk[4]

def tarefa_colaborador(tsk, user, dur: int = 0):
    ''' 2.3.5 tarefa_colaborador: tarefa x utilizador x float -> tarefa '''
    if dur < 0:
        raise ValueError('tarefa_colaborador: operação inválida')
    if tsk[3]: # atualizar tempo do colaborador anterior e remover
        utilizador_remove(tsk[3], tsk)
        utilizador_tempo(tsk[3], dur)
    tsk[3] = user
    utilizador_insere(tsk[3], tsk)
    return tsk

def tarefa_move(tsk, act, dur: int = 0):
    ''' 2.3.6 tarefa_move: tarefa x atividade x float -> tarefa '''
    if dur < 0:
        raise ValueError('tarefa_move: operação inválida')
    if tsk[3]: # atualizar tempo do colaborador
        utilizador_tempo(tsk[3], dur)
    elif act != atividade_to_do(): # tem de ter colaborador (exceto TO_DO)
        raise ValueError('tarefa_move: operação inválida')
    tsk[4] += dur
    atividade_remove(tsk[2], tsk)
    atividade_insere(act, tsk)
    tsk[2] = act
    if act == atividade_to_do():
        if tsk[3]:
            utilizador_remove(tsk, tsk[3])
        tsk[3] = None
        tsk[4] = 0
    return tsk

def tarefa_atraso(tsk) -> int:
    ''' 2.3.7 tarefa_atraso: tarefa -> float '''
    return tsk[1] - tsk[4]

def tarefa_descricao(tsk, desc: str) -> str:
    ''' 2.3.8 tarefa_descricao: tarefa x str -> str '''
    if not isinstance(desc, str) or not desc.strip() \
        or desc in _todas():
        raise ValueError('tarefa_descricao: argumentos inválidos')
    del _todas()[tsk[0]]
    old = tsk[0]
    tsk[0] = desc
    _todas()[desc] = tsk
    return old

# funções auxiliares para garantir as barreiras de abstração
def tarefas():
    ''' 2.3.9 tarefas: -> list[tarefa] '''
    return _TODAS.values()

_TODAS = {}
def _todas():
    ''' 2.3.0 dicionário de tarefas '''
    return _TODAS
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
def cria_utilizador(identificador : str , descricao : str) -> dict :
    '''
    recebe id e descrição devolvendo um user com ambos,
    bem como os valores default associados a um user
    '''
    if not isinstance(identificador,str) or not isinstance(descricao,str):
        raise ValueError('cria_utilizador: argumentos inválidos')
    if not 1 <= len(identificador) <= 12 or ':' in identificador \
        or not descricao.replace(' ','').isalpha() or len(descricao) < 12 :
        raise ValueError('cria_utilizador: argumentos inválidos')
    novo_user = {
        'id' : identificador ,
        'dur' : 0.0 ,
        'tarefas' : [] ,
        'descricao' : descricao
    }
    _lista_utilizadores.append(novo_user)
    return novo_user
def eh_utilizador(hipotese : any) -> bool :
    '''
    verifica se o argumento é um utilizador usando a _lista_utilizadores
    '''
    return hipotese in _lista_utilizadores
def utilizador_str(user : dict) -> str :
    '''
    reescreve user em str,
    troca a lista de tarefas pelo número de tarefas associado
    '''
    return f"{user['id']}:{user['dur']}" \
        f":{len(user['tarefas'])}:{user['descricao']}"
def utilizador_tarefas(user : dict) -> str :
    '''
    devolve uma str com a descrição de todas as atividades de um user
    '''
    cadeia_caract = ''
    tarefas_ordenadas = []
    for tarefa in user['tarefas']:
        tarefas_ordenadas.append(tarefa_representacao(tarefa)[0])
    tarefas_ordenadas.sort()
    for task in tarefas_ordenadas:
        cadeia_caract += task + '\n'
    return cadeia_caract
# funções auxiliares (utilizadores)
def utilizador_tempo(user : dict, dur : float):
    '''
    adiciona o valor recebido ao tempo já gasto pelo utilizador
    '''
    user['dur'] += dur
def utilizador_insere(user : dict, tarefa):
    '''
    insere uma nova tarefa nas tarefas do utilizador
    '''
    user['tarefas'].append(tarefa)
def utilizador_remove(user : dict, tarefa):
    '''
    remove a tarefa nas tarefas do utilizador
    '''
    user['tarefas'].remove(tarefa)
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
# função auxiliar de tarefas
# a função tarefas foi criada caso houve-se necessidade de garantir barreiras
# de abestração, no entanto não surgiu essa necessidade
# a função tarefas() foi na mesma implementada como sugeria no enunciado
