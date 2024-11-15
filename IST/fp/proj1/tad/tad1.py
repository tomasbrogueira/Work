"""
TAD atividade com listas
"""

def cria_atividade(desc: str):
    ''' 2.1.1 `cria_atividade: str -> atividade '''
    # desc são maiúsculas ou _ entre 4 e 12
    if not isinstance(desc, str) or len(desc) < 4 or len(desc) > 12 or \
        any((not(ch.isupper() or ch == '_') for ch in desc)):
        raise ValueError('cria_atividade: argumentos inválidos')
    return [desc, []] # (desc, list[tsk])

def eh_atividade(obj: any) -> bool:
    ''' 2.1.2 `eh_atividade: any -> bool` '''
    return isinstance(obj, list) and len(obj) == 2 and isinstance(obj[0], str) \
    and 4 <= len(obj[0]) <= 12 and all((ch.isupper() or ch == '_' for ch in obj[0])) \
    and isinstance(obj[1], list) and all((tsk in tarefas() for tsk in obj[1]))

def atividade_descricao(act) -> str:
    ''' 2.1.3 atividade_descricao: atividade -> str '''
    return act[0]

def atividade_tarefas(act) -> tuple:
    ''' 2.1.4 atividade_tarefas: atividade -> tuple[tarefa] '''
    tsks = list(act[1])
    tsks.sort(key = lambda t: tarefa_representacao(t)[0])
    return tuple(tsks) if act[1] else ()

# funções auxiliares para garantir as barreiras de abstração
def atividade_insere(act, tsk):
    ''' 2.1.5 atividade_insere: act: atividade x tsk: tarefa '''
    if tsk not in act[1]:
        act[1] += [tsk]

def atividade_remove(act, tsk):
    ''' 2.1.5 atividade_remove: act: atividade x tsk: tarefa '''
    if tsk in act[1]:
        del act[1][act[1].index(tsk)]

_TODO = cria_atividade("TO_DO")
def atividade_to_do():
    ''' 2.1.5 atividade_to_do: -> atividade '''
    return _TODO
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
# funções auxiliares (atividades)
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
