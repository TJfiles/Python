"""
2.19 Um alvo de dardos de raio 10 e a parede em que está pendurado são representados usando o
sistema de coordenadas bidimensionais, com o centro do alvo na coordenada (0,0). As
variáveis x e y armazenam as coordenadas x e y de um lançamento de dardo. Escreva uma
expressão usando as variáveis x e y que avalia como True se o dardo atingir o (estiver dentro
do) alvo, e avalie a expressão para estas coordenadas do dardo:
(a)(0, 0)
(b)(10, 10)
(c)(6, –6)
(d)(–7, 8)
"""
import math

raio = 10
alvo_x = 0
alvo_y = 0

def mira(x, y):
    distancia = math.sqrt(((y - alvo_y) ** 2) + ((x - alvo_x) ** 2))
    if distancia <= raio:
        return True
    else:
        return False

print(mira(0, 0))
print(mira(10, 10))
print(mira(6, -6))
print(mira(-7, 8))
