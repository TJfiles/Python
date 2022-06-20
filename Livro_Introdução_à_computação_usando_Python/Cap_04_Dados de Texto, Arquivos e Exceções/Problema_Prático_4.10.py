"""
Explique o que causa o erro de sintaxe em cada instrução listada anteriormente. Depois, escreva
uma versão correta de cada instrução Python.
Erros de Sintaxe
Dois tipos básicos de erros podem ocorrer durante a execução de um programa em Python. Os
erros de sintaxe são aqueles que se devem ao formato incorreto de uma instrução Python. Esses
erros ocorrem enquanto a instrução ou programa está sendo traduzido para a linguagem de
máquina e antes que esteja sendo executado. Um componente do interpretador Python,
chamado analisador (ou parser), descobre esses erros. Por exemplo, a expressão:
>>> (3+4]
SyntaxError: invalid syntax
>>> if x == 5
SyntaxError: invalid syntax
>>> print 'hello'
SyntaxError: invalid syntax
>>> lst = [4;5;6]
SyntaxError: invalid syntax
>>> for i in range(10):
print(i)
SyntaxError: expected an indented block
Em cada uma dessas instruções, o erro se deve a uma
"""
# (3+4) erro de sintaxe, expressão aberta com parentese e fechada com colchete
# if x == 5: faltou os dois pontos ao fim da instrução if
# print('hello') a função print deve ser usada com parenteses
# lst = [4, 5, 6] os items de uma lista devem ser separados por ',', não por ';'

for i in range(10):
    print(i)  # o bloco de código deve estar endentado dentro do escopo da instrução de controle if

