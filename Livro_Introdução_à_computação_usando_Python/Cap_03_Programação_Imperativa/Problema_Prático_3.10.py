"""
Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por linha, os
valores negativos na lista. A função não deverá retornar nada.
>>> negatives([4, 0, -1, -3, 6, -9])
-1
-3
-9
"""


def negatives(lista = list):
    'Aceita uma lista como entrada e imprime os valores negativos da lista'
    for n in lista:
        if n < 0:
            print(n)


lista = [4, 0, -1, -3, 6, -9]
negatives(lista)