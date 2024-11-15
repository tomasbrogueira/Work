def cria_atividade(desc: str) -> dict:        
    if 4 <= len(desc) <= 12 and desc.isupper():
        return {'descricao':desc, 'tarefas': []}
    raise ValueError('cria_atividade: argumentos inválidos')

_act0 = cria_atividade('TO_DO')

def atividade_to_do():
    return _act0

def eh_atividade(arg: any) -> bool:
    return isinstance(arg, dict) \
        and all(k in arg.keys() for k in ('descricao', 'tarefas'))

def atividade_descricao(act: dict) -> str:
    return act['descricao']

def atividade_tarefas(act: dict) -> tuple:
    return tuple(sorted(act['tarefas'], key=lambda t: tarefa_representacao(t)[0]))

def atividade_insere(act, tar):
    act['tarefas'].append(tar)

def atividade_remove(act, tar):
    act['tarefas'].remove(tar)

_tarefas = { }
def tarefas():
    return _tarefas

def cria_tarefa(desc: str, time: float) -> dict:
    if isinstance(desc, str) and isinstance(time, (float, int)) \
        and desc != '' and not desc.isspace() and time > 0 and desc not in tarefas():
        tarefa = {'descricao': desc, 'duracao': time, 'execucao': 0.0,\
             'actividade': atividade_to_do(), 'utilizador': None}
        atividade_insere(atividade_to_do(), tarefa)
        _tarefas.update({ desc: tarefa })
        return tarefa
    raise ValueError('cria_tarefa: argumentos inválidos')

def eh_tarefa(arg: any) -> bool:
    return isinstance(arg, dict) \
        and all(k in arg.keys() for k in ('descricao', 'duracao',\
             'execucao', 'actividade', 'utilizador'))

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
    
    if tarefa['utilizador'] is not None:
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

def cria_utilizador(i_d: str, nome: str) -> dict:
    if 1 <= len(i_d) <= 12 and not (':' in i_d) and len(nome) >= 12 and all(c.isalpha() or c==' ' for c in nome):
        return {'id': i_d, 'nome': nome, 'tarefas': [], 'tempo': 0.0}
    raise ValueError('cria_utilizador: argumentos inválidos')

def eh_utilizador(arg: any) -> bool:
    return isinstance(arg, dict) \
        and all(k in arg.keys() for k in ('id', 'nome', 'tarefas', 'tempo'))

def utilizador_str(user: dict) -> str:
    return user['id'] + ':' + str(user['tempo']) + ':' + \
        str(len(user['tarefas'])) \
        + ':' + user['nome']

def utilizador_tarefas(user: dict) -> str:
    ordenadas = sorted([tarefa_representacao(t)[0] for t in user['tarefas']])
    return ''.join([desc +'\n' for desc in ordenadas])

def utilizador_tempo(utilizador, tempo):
    utilizador['tempo'] += tempo

def utilizador_insere(user, tarefa):
    user['tarefas'].append(tarefa)

def utilizador_remove(user, tarefa):
    user['tarefas'].remove(tarefa)