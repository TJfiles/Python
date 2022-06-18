"""
Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e último
elementos da lista. Você pode considerar que a lista não estará vazia. A função não deverá retornar
nada.
>>> ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
>>> trocaPU(ingredientes)
>>> ingredientes
['maçãs', 'açúcar', 'manteiga', 'farinha']
"""

ingredients = ['farinha', 'açúcar', 'manteiga', 'maçãs']


def trocaPU(lst):

    lst[0], lst[-1] = lst[-1], lst[0]


'''    last = lst.pop()
    first = lst.pop(0)
    lst.append(first)
    lst.insert(0, last)'''


trocaPU(ingredients)
print(ingredients)