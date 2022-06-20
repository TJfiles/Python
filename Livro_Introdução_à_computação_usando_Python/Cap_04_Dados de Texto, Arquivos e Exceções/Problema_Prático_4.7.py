"""
Escreva a função stringCount() que aceita duas entradas de string — um nome de arquivo
e uma string de alvo — e retorna o número de ocorrências da string alvo no arquivo.
>> stringCount('example.txt', 'line')
4
"""


def strCount(file: str, string: str):
    arquivo = open(file, 'r')
    conteudo = arquivo.read()
    print(conteudo.count(string))
    arquivo.close()

strCount('example.txt', 'line')

