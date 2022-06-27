"""
Implemente a função fatorial(), que toma como entrada um inteiro não negativo e retorna
seu fatorial. O fatorial de um inteiro não negativo n, indicado por n!
Logo, 0! = 1,3! = 6 e 5! = 120.
>> fatorial(0)
1
>> fatorial(3)
6
>> fatorial(5)
120
"""


def fatorial(n):
    fat = 1
    for i in range(2, n+1):
        fat *= i
    return fat

