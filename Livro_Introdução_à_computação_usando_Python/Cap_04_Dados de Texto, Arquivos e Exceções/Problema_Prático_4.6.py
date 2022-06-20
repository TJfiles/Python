"""
Implemente a função rol(), que recebe uma lista contendo informações de estudantes e exibe
um rol, como vemos a seguir. As informações do estudante, consistindo em seu sobrenome, nome,
nível e nota média, serão armazenadas nessa ordem em uma lista. Portanto, a lista de entrada é
uma lista de listas. Cuide para que o rol exibido tenha 10 espaços para cada valor de string e 8
para a nota, incluindo 2 espaços para a parte decimal.
estudantes = []
>> estudantes.append([ ' DeMoines', 'Jim', 'Pleno', 3.45])
>> estudantes.append([ ' Pierre', 'Sophie', 'Pleno', 4.0])
>> estudantes.append([ ' Columbus', 'Maria', 'Sênior', 2.5])
>> estudantes.append([ ' Phoenix', 'River', 'Júnior', 2.45])
>> estudantes.append([ ' Olympis', 'Edgar', 'Júnior', 3.99])
>> rol(estudantes)
Último Primeiro Classe Nota Média
DeMoines Jim Pleno 3.45
Pierre Sophie Pleno 4.00
Columbus Maria Sênior 2.50
Phoenix River Júnior 2.45
Olympia Edgar Júnior 3.99
"""

estudantes = []
estudantes.append([' DeMoines', 'Jim', 'Pleno', 3.45])
estudantes.append([' Pierre', 'Sophie', 'Pleno', 4.0])
estudantes.append([' Columbus', 'Maria', 'Sênior', 2.5])
estudantes.append([' Phoenix', 'River', 'Júnior', 2.45])
estudantes.append([' Olympis', 'Edgar', 'Júnior', 3.99])


def rol(lista):
    print(' Último     Primeiro    Classe  Nota Média')
    for est in lista:
        print('{0:11} {1:11} {2:9} {3:.2f}'.format((est[0]), (est[1]), (est[2]), (est[3])))


rol(estudantes)


