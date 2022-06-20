"""
Escreva a função palavras() que aceita um argumento de entrada — um nome de arquivo —
e retorna a lista de palavras reais (sem símbolos de pontuação !,.:;?) no arquivo.
>> palavras('example.txt')
['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with',
'the', 'new', 'line', 'character', 'There', 'is', 'a',
'blank', 'line', 'above', 'this', 'line']
"""


def palavras(file):
    arquivo = open(file, 'r')
    conteudo = arquivo.read()
    for i in conteudo:
        if i in '!,.:;?':
            conteudo = conteudo.replace(i, '')
    arquivo.close()
    return conteudo.split()

