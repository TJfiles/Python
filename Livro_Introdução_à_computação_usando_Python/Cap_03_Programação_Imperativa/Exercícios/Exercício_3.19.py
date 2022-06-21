"""
Escreva um laço for que percorra uma lista de strings lst e exiba os três primeiros
caracteres de cada palavra. Se 1st for a lista ['Janeiro' , 'Fevereiro' , 'Março'],
então o seguinte deve ser exibido na tela:
Jan
Fev
Mar
"""

lst = ['Janeiro' , 'Fevereiro' , 'Março']

for i in lst:
    print(i[0:3])