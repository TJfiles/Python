"""
Escreva a função aritmética(), que aceita uma lista de inteiros como entrada e
retorna True se eles formarem uma sequência aritmética. (Uma sequência de inteiros é
uma sequência aritmética se a diferença entre os itens consecutivos da lista for sempre a mesma.)
>> aritmética([3, 6, 9, 12, 15])
True
>> aritmética([3, 6, 9, 11, 14])
False
>> aritmética([3])
True
"""


def aritmetica(lst):
    """Retorna True se a lista lst tiver uma sequência aritmética, False se caso contrário"""
    if len(lst) > 2:
        return True
    dif = lst[1] - lst[0]
    for i in range(1, len(lst)-1):
        if lst[i+1] - lst[i] != dif:
            return False
    return True

'''    dif_base = 0
    print(lst)
    for i in range(0, len(lst)-1):
        dif = lst[i+1] - lst[i]
        print('A diferença entre {} e {} é {}'.format(lst[i], lst[i+1], dif))
        if i == 0:
            dif_base = dif
        elif dif_base != dif:
            return False

        elif dif_base == dif:
            return True
        '''

print(aritmetica([3, 6, 9, 12, 15]))

print()
print(aritmetica([3, 6, 9, 11, 14]))
