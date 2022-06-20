"""
Implemente a função meuGrep(), que toma como entrada duas strings, um nome de arquivo e
uma string alvo, e exibe cada linha do arquivo que contém a string alvo como uma substring.
>> meuGrep('example.txt', 'line')
The 3 lines in this file end with the new line character.
There is a blank line above this line.
"""


def meuGrep(file: str, string: str):
    arquivo = open(file, 'r')
    conteudo = arquivo.readlines()
    print(conteudo)
    for linha in conteudo:
        if string in linha:
            print(linha, end='')  # o ultimo caractere de cada linha do arquivo é \n, então devemos mudar o end= padrão
    arquivo.close()


meuGrep('example.txt', 'line')
