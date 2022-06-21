"""
Escreva um laço for que percorre uma lista de números lst e exibe na tela os números na
lista cujo quadrado seja divisível por 8. Por exemplo, se lst for [2, 3, 4, 5, 6, 7, 8,
9], então os números 4 e 8 devem ser exibidos.
"""

lst = [2, 3, 4, 5, 6, 7, 8, 9]
for i in lst:
    if (i**2)%8 == 0:
        print(i)
