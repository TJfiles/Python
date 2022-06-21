"""
Implemente um programa que solicita uma lista de palavras do usuário e depois exibe cada
palavra na lista que não seja 'segredo'.
>>>
Digite lista de palavras: ['cia', 'segredo', 'mi6', 'isi', 'segredo']
cia
mi6
isi
"""
lst = input('Difite lista de palavras: ').lower().split()
for i in lst:
    if i != 'segredo':
        print(i)
