# UML (plantuml) to python converter
#
# Author: Pedro Reis dos Santos
# Date: June 25, 2022
__all__ = [ 'scan', 'grammar', 'uml2py' ]
from ply import *
from graphlib import TopologicalSorter as toposort
from graphlib import CycleError

# -------------- LEX ----------------
reserved = { 'class': 'CLASS', 'interface': 'INTERFACE', 'skinparam': 'SKINPARAM', '__': 'SEP4', 'abstract': 'ABSTRACT', 'static': 'STATIC', }
tokens = ( 'ID', 'INT', 'STR', 'SEP', 'SEP2', 'SEP3', 'START', 'END', 'DEPEND', 'DEPEND2', 'INHERIT', 'INHERIT2', 'COMPOSE', 'COMPOSE2', 'AGGREG', 'AGGREG2', 'TEMPLATE', ) + tuple(reserved.values())
literals = [',', '(', ')', ':', '{', '}', '[',']', '+', '-', '#', '~', '=' ]
t_ignore = ' \t\r'
t_INT = r'\d+'
t_STR = r'"([^"\\]|\\.)*"'
t_SEP = '--'
t_SEP2 = '=='
t_SEP3 = '\.\.'
t_START = '@startuml'
t_END = '@enduml'
t_INHERIT = '\<\|--|\<\|..'
t_INHERIT2 = '--\|>|..\|>'
t_COMPOSE = '\*--\>?'
t_COMPOSE2 = '--\*|\<--\*'
t_AGGREG = 'o--\>?'
t_AGGREG2 = '\<?--o'
t_DEPEND = '\-\-\>'
t_DEPEND2 = '\<\-\-'
t_TEMPLATE = '\<[_A-Za-z][A-Za-z0-9_]*\>'

def t_ID(t):
	r'[_A-Za-z][A-Za-z0-9_]*'
	t.type = reserved.get(t.value,'ID')
	return t

def t_COMMENT(t):
	r'\#.*\n'
	t.lexer.lineno += 1
	pass # No return value. Token discarded

def t_newline(t):
	r'\n'
	t.lexer.lineno += 1
	pass # No return value. Token discarded

def t_error(t):
	print("%d: Illegal character '%s'" % (t.lexer.lineno, t.value[0]))
	print(t.value)
	t.lexer.skip(1)

def scan(data): # for debug
	lexer = lex.lex(debug=True)
	lexer.input(data)
	for t in lexer:
		print(t)

# -------------- YACC ----------------
precedence = []
dbg=False
graph = {} # for topological sorting of class dependecies
classes = set() # top level names

def p_uml(p):
	'''uml : START decls END '''
	if dbg: print(p[2])
	p[0] = p[2]

def p_decls_0(p):
	'''decls : '''
	p[0] = ()

def p_decls_1(p):
	'''decls : decls SKINPARAM ID ID '''
	p[0] = p[1]

def p_decls_2(p):
	'''decls : decls SKINPARAM ID INT '''
	p[0] = p[1]

def p_decls_3(p):
	'''decls : decls class '''
	p[0] = p[1] + (p[2],)

def p_decls_4(p):
	'''decls : decls assoc '''
	p[0] = p[1] + (p[2],)

def p_class_0(p):
	'''class : abs CLASS ID '{' attribs '}' '''
	p[0] = ('CLASS', p[3], p[5], p[1])
	if p[3] not in graph: graph[p[3]] = set()
	global classes
	classes |= { p[3] }

def p_class_1(p):
	'''class : abs INTERFACE ID '{' attribs '}' '''
	p[0] = ('INTERFACE', p[3], p[5], p[1])
	if p[3] not in graph: graph[p[3]] = set()
	global classes
	classes |= { p[3] }

def p_abs_0(p):
	'''abs : '''
	p[0] = None

def p_abs_1(p):
	'''abs : ABSTRACT '''
	p[0] = 'ABSTRACT'

def p_attribs_0(p):
	'''attribs : '''
	p[0] = ()

def p_attribs_1(p):
	'''attribs : attribs prot ID vec type init'''
	p[0] = p[1] + ((p[2], p[3], p[5], p[6]),)

def p_attribs_2(p):
	'''attribs : attribs prot ID '(' ')' type'''
	p[0] = p[1] + ((p[2], None, p[3], p[6], ()),)

def p_attribs_3(p):
	'''attribs : attribs prot ID '(' args ')' type'''
	p[0] = p[1] + ((p[2], None, p[3], p[7], p[5]),)

def p_attribs_8(p):
	'''attribs : attribs prot STATIC ID '(' ')' type'''
	p[0] = p[1] + ((p[2], p[3], p[4], p[7], ()),)

def p_attribs_9(p):
	'''attribs : attribs prot STATIC ID '(' args ')' type'''
	p[0] = p[1] + ((p[2], p[3], p[4], p[8], p[6]),)

def p_attribs_10(p):
	'''attribs : attribs prot ABSTRACT ID '(' ')' type'''
	p[0] = p[1] + ((p[2], p[3], p[4], p[7], ()),)

def p_attribs_11(p):
	'''attribs : attribs prot ABSTRACT ID '(' args ')' type'''
	p[0] = p[1] + ((p[2], p[3], p[4], p[8], p[6]),)

def p_attribs_4(p):
	'''attribs : attribs SEP'''
	p[0] = p[1]
	if dbg: print("SEP:", p[2])

def p_attribs_5(p):
	'''attribs : attribs SEP2'''
	p[0] = p[1]
	if dbg: print("SEP:", p[2])

def p_attribs_6(p):
	'''attribs : attribs SEP3'''
	p[0] = p[1]
	if dbg: print("SEP:", p[2])

def p_attribs_7(p):
	'''attribs : attribs SEP4'''
	p[0] = p[1]
	if dbg: print("SEP:", p[2])

def p_type_0(p):
	'''type : '''
	p[0] = None

def p_type_1(p):
	'''type : ':' ID vec'''
	p[0] = p[2]

def p_args_0(p):
	'''args : ID type'''
	p[0] = (p[1], p[2]),

def p_args_1(p):
	'''args : args ',' ID type'''
	p[0] = p[1] + ((p[3], p[4]),)

def p_prot_0(p):
	'''prot : '+' '''
	p[0] = 'PUBLIC'

def p_prot_1(p):
	'''prot : '-' '''
	p[0] = 'PRIVATE'

def p_prot_2(p):
	'''prot : '~' '''
	p[0] = 'PACKAGE'

def p_prot_3(p):
	'''prot : '#' '''
	p[0] = 'PROTECTED'

def p_prot_4(p): # remove?
	'''prot : '''
	p[0] = None

def p_vec_0(p):
	'''vec : '''
	p[0] = None

def p_vec_1(p):
	'''vec : '[' ']' '''
	p[0] = None

def p_vec_2(p):
	'''vec : '[' INT ']' '''
	p[0] = None

def p_vec_3(p):
	'''vec : TEMPLATE '''
	p[0] = None

def p_init_0(p):
	'''init : '''
	p[0] = None

def p_init_1(p):
	'''init : '=' ID'''
	p[0] = p[2]

def p_init_2(p):
	'''init : '=' STR'''
	p[0] = p[2]

def p_init_3(p):
	'''init : '=' INT'''
	p[0] = p[2]

def p_assoc_0(p):
	'''assoc : ID INHERIT ID'''
	p[0] = ('INHERIT', p[1], p[3])
	global classes
	classes |= { p[1], p[3] }
	if p[1] not in graph: graph[p[1]] = set()
	if p[3] not in graph: graph[p[3]] = { p[1] }
	else:
		if p[1] not in graph[p[3]]:
			graph[p[3]] = graph[p[3]] | { p[1] }

def p_assoc_1(p):
	'''assoc : ID INHERIT2 ID'''
	p[0] = ('INHERIT', p[3], p[1])
	global classes
	classes |= { p[1], p[3] }
	if p[3] not in graph: graph[p[3]] = set()
	if p[1] not in graph: graph[p[1]] = { p[3] }
	else:
		if p[3] not in graph[p[1]]:
			graph[p[1]] = graph[p[1]] | { p[3] }

def p_assoc_2(p):
	'''assoc : ID card aggreg card ID type'''
	p[0] = (p[3], p[1] , p[2], p[6], p[4], p[5])
	global classes
	classes |= { p[1], p[5] }
	if p[5] not in graph: graph[p[5]] = set()
	if p[1] not in graph: graph[p[1]] = set()

def p_assoc_3(p):
	'''assoc : ID card reverse card ID type'''
	p[0] = (p[3], p[5] , p[4], p[6], p[2], p[1])
	global classes
	classes |= { p[1], p[5] }
	if p[1] not in graph: graph[p[1]] = set()
	if p[5] not in graph: graph[p[5]] = set()

def p_aggreg_0(p):
	'''aggreg : AGGREG '''
	p[0] = 'AGGREG'

def p_aggreg_1(p):
	'''aggreg : COMPOSE '''
	p[0] = 'COMPOSE'

def p_aggreg_2(p):
	'''aggreg : DEPEND '''
	p[0] = 'DEPEND'

def p_aggreg_3(p):
	'''aggreg : SEP '''
	p[0] = 'ASSOC'

def p_aggreg_4(p): # no match for "o--" use ID=='o' and SEP (ply!!!)
	'''aggreg : ID SEP '''
	if p[1] != 'o': p_error(p)
	p[0] = 'AGGREG'

def p_aggreg_5(p): # no match for "o-->" use ID=='o' and SEP (ply!!!)
	'''aggreg : ID DEPEND '''
	if p[1] != 'o': p_error(p)
	p[0] = 'AGGREG'

def p_reverse_0(p):
	'''reverse : AGGREG2 '''
	p[0] = 'AGGREG'

def p_reverse_1(p):
	'''reverse : COMPOSE2 '''
	p[0] = 'COMPOSE'

def p_reverse_2(p):
	'''reverse : DEPEND2 '''
	p[0] = 'DEPEND'

def p_card_0(p):
	'''card : '''
	p[0] = None

def p_card_1(p):
	'''card : STR '''
	p[0] = p[1]

def p_error(p):
	print('Rule error:', p)

def _defined(id: str):
	try: eval(id)
	except NameError: return False
	else: return True

def _args(meth: tuple, first: bool):
	if not meth or len(meth) <= 4: return
	for arg in meth[4]:
		if first: first = False
		else: print(", ", end='')
		print(arg[0], end='')
		if arg[1]:
			print(":", arg[1], end='')

def _ctor(id: str, attr: tuple, gram: tuple):
	ctor = None
	for item in attr:
		if len(item) > 4 and item[2] == '__init__':
			ctor = item
			break
	if not ctor:
		for item in attr:
			if len(item) > 4 and item[2] == id:
				ctor = item
				#item[2] = '__init__'
				break
	print("    def __init__(self", end='')
	_args(ctor, False)
	print("):")
	cnt = 0
	for item in attr:
		if len(item) <= 4:
			cnt += 1
			print("        self."+item[1], end='')
			if item[2]:
				print(":", item[2], end='')
			if len(item) > 3 and item[3]:
				print(" =", item[3])
			else:	print(" = None")
	for item in gram:
		if item[0] in ('COMPOSE', 'AGGREG') and item[1] == id:
			cnt += 1
			name = item[3] if item[3] else "field"+str(cnt)
			print("        self."+name, ":", item[5], "= None")
			
	if not cnt: print("        pass")

def _methods(id: str, attr: tuple, gram: tuple):
	ctor = None
	for item in attr:
		if len(item) > 4:
			if item[2] == '__init__':
				ctor = item
				continue
			first = False
			if item[2] == id:
				if not ctor:
					ctor = item
					continue
				print("    @classmethod")
				print("    def", item[2], "(cls", end='')
			elif item[1] == 'STATIC':
				print("    @staticmethod")
				print("    def", item[2], "(", end='')
				first = True
			else:
				print("    def", item[2], "(self", end='')
			_args(item, first)
			if item[1] == 'ABSTRACT':
				print("):\n        raise NotImplementedError")
			else:	print("):\n        pass")

def uml2py(gram, out):
	print('# classes =', classes)
	abc = False # use abstract classes
	for id in classes:
		if not _defined(id):
			print(id, '= None # type forward declaration')
	try:
		print('## graph =',graph)
		topo = tuple(toposort(graph).static_order())
		print('## topo =',topo)
		for id in topo:
			classes.remove(id)
			nocls = True
			for data in gram:
				if data[0] in ('CLASS', 'INTERFACE') and data[1] == id:
					nocls = False
					break
			inherit = ''
			if data and data[0] == 'INTERFACE':
				if not abc:
					abc = True
					print("from abc import ABC as abstract")
				inherit = '(abstract'
			for cls in graph[id]:
				if inherit: inherit += ', ' + cls
				else: inherit = '(' + cls
			if inherit: inherit += ')'
			print("class", id, inherit, ':')
			if nocls:
				_ctor(id, (), gram)
			else:
				_ctor(id, data[2], gram)
				_methods(id, data[2], gram)
			print()
		print('## missing =', classes)
	except CycleError: print("ERROR: Inheritance dependency cyles")

def grammar(data):
	gram = yacc.yacc().parse(data, debug=False, tracking=True, lexer=lex.lex())
	return gram

if __name__ == '__main__':
	from sys import argv, stdout, exit
	if len(argv) > 1:
		with open(argv[1]) as fp: data = fp.read()
		gram = grammar(data)
		print('##', gram)
	else:
		print("USAGE: %s filename.uml [output.py]" % argv[0])
		exit(1)
	fp = stdout
	if len(argv) > 2:
		fp = open(argv[2], "w")
	uml2py(gram, fp)
