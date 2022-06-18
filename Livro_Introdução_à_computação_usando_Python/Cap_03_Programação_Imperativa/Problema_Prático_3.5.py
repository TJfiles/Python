"""
Implemente um programa que solicite do usuário uma lista de palavras (ou seja, strings) e depois
exiba na tela, uma por linha, todas as strings de quatro letras nessa lista.
>>>
Digite a lista de palavras: ['pare', 'desktop', 'tio', 'pote']
pare pote
"""

lista = input('Digite a lista de palavras: ').split()
for palavra in lista:
    if len(palavra) == 4:
        print(palavra)