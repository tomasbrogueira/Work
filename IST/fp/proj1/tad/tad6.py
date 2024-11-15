_tarefas = { }
def tarefas():
    return _tarefas

def cria_tarefa(desc: str, time: float) -> dict:
    if isinstance(desc, str) and isinstance(time, (float, int)) \
        and desc != '' and not desc.isspace() and time > 0 and desc not in tarefas():
        tarefa = {'descricao': desc, 'duracao': time, 'execucao': 0.0, 'actividade': atividade_to_do(), 'utilizador': None}
        atividade_insere(atividade_to_do(), tarefa)
        _tarefas.update({ desc: tarefa })
        return tarefa
    raise ValueError('cria_tarefa: argumentos inválidos')

def eh_tarefa(arg: any) -> bool:
    return isinstance(arg, dict) \
        and all(k in arg.keys() for k in ('descricao', 'duracao', 'execucao', 'actividade', 'utilizador'))

def tarefa_atividade(arg: dict) -> str:
    return arg['actividade']

def tarefa_representacao(tarefa: dict) -> tuple:
    utilizador = utilizador_str(tarefa['utilizador']).split(':')[0] if tarefa['utilizador'] else ''
    return (tarefa['descricao'], atividade_descricao(tarefa_atividade(tarefa)),\
        utilizador, tarefa['duracao'], tarefa['execucao'])

def tarefa_colaborador(tarefa: dict, utilizador: dict, tempo: float=0) -> dict:
    if tempo < 0:
        raise ValueError('tarefa_colaborador: operação inválida')
    
    if atividade_descricao(tarefa_atividade(tarefa)) != 'TO_DO':
        tarefa['execucao'] += tempo
        if tarefa['utilizador']:
            utilizador_tempo(tarefa['utilizador'], tempo)
    
    if tarefa['utilizador']:
        utilizador_remove(tarefa['utilizador'], tarefa)
    tarefa['utilizador'] = utilizador
    utilizador_insere(utilizador, tarefa)
    
    return tarefa

def tarefa_move(tarefa: dict, atividade: dict, tempo: float=0.0) -> dict:
    if atividade_descricao(tarefa['actividade']) == 'TO_DO' \
        and not tarefa['utilizador'] or tempo < 0:
        raise ValueError('tarefa_move: operação inválida')

    tarefa['execucao'] += tempo
    
    if tarefa['utilizador'] != None:
        utilizador_tempo(tarefa['utilizador'], tempo)
    
    atividade_remove(tarefa['actividade'], tarefa)
    atividade_insere(atividade, tarefa)
    tarefa['actividade'] = atividade
    return tarefa

def tarefa_atraso(tarefa: dict) -> float:
    return tarefa['duracao'] - tarefa['execucao']

def tarefa_descricao(tarefa: dict, texto: str) -> str:
    if texto in tarefas():
        raise ValueError('tarefa_descricao: operação_inválida')
    
    old = tarefa['descricao']
    tarefa['descricao'] = texto
    
    _tarefas.update({ texto: tarefa})
    del _tarefas[old]
    
    return old
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
