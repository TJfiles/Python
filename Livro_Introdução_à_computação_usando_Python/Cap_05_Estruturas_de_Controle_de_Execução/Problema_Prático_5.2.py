"""
Escreva uma função chamada potências() que apanhe um inteiro positivo n como entrada e
exiba, na tela, todas as potências de 2 desde 21 até 2n.
>> potências(6)
2 4 8 16 32 64
"""


def potencias(n):
    for i in range(n+1):
        print(2**i, end=' ')


potencias(6)
