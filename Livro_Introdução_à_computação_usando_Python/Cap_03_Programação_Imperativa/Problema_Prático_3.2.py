'''
Traduza estas instruções condicionais em instruções if do Python:
(a)Se idade é maior que 62, exiba 'Você pode obter benefícios de
pensão'.
(b)Se o nome está na
lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], exiba 'Um
dos 5 maiores jogadores de beisebol de todos os tempos!'.
(c)Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.
(d)Se pelo menos uma das variáveis
booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.
'''

# (a)Se idade é maior que 62, exiba 'Você pode obter benefícios de pensão'
'''if idade > 62:
    print('Você pode obter benefícios de pensão')
'''

# (b)Se o nome está na
# lista ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], exiba 'Um
# dos 5 maiores jogadores de beisebol de todos os tempos!'.
'''lista = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
if nome in lista:
    print('Um dos 5 maiores jogadores de beisebol de todos os tempos!')'''

# (c)Se golpes é maior que 10 e defesas é 0, exiba 'Você está morto…'.
'''
if golpes > 10 and defesas == 0:
    print('Você está morto...')
'''

# (d)Se pelo menos uma das variáveis
# booleanas norte, sul, leste e oeste for True, exiba 'Posso escapar.'.
'''
if norte or sul or leste or oeste:
    print('Posso escapar')
'''