"""
Escreva a função contaVogal(), que aceita uma string como entrada e conta e exibe o
número de ocorrências de vogais na string.
>> contaVogal('Le Tour de France')
a, e, i, o e u aparecem, respectivamente, 1, 3, 0, 1, 1 vezes.
"""
soma = 0
def contavogal(string):
    string = string.lower()
    print('a, e, i o e u aparecem, respectivamente, {}, {}, {}, {}, {} vezes'.format(string.count('a'), string.count('e'), string.count('i'), string.count('o'), string.count('u')))

string = 'Le Tour de France'
contavogal(string)
