def codifica(s):
    n_frase = ''
    for letra in s:
        if letra == ' ':
            n_frase += ' '

        if letra.isalpha() and letra.isupper():
            n_frase += chr(abs(25-ord(letra)+ord('A'))+ord('A'))
        
    return n_frase
    
print(codifica('ESTA E UMA PERGUNTA BOA PARA O TESTE DE FP'))


def descodifica(s):
    n_frase = ''
    for letra in s:
        if letra == ' ':
            n_frase += ' '

        if letra.isalpha() and letra.isupper():
            n_frase += chr(abs(25-ord(letra)+ord('A'))+ord('A'))
        
    return n_frase

print(descodifica('VHGZ V FNZ KVITFMGZ YLZ KZIZ L GVHGV WV UK'))