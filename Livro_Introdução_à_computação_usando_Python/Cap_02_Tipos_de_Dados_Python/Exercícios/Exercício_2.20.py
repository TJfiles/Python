"""
Uma escada encostada diretamente contra uma parede cairá a menos que colocada em um
certo ângulo menor que 90 graus. Dadas as variáveis comprimento e ângulo armazenando o
comprimento da escada e o ângulo que ela forma com o solo enquanto encostada na parede,
escreva uma expressão Python envolvendo comprimento e ângulo, que calcule a altura
alcançada pela escada. Avalie a expressão para estes valores de comprimento e ângulo:
(a)16 pés e 75 graus
(b)20 pés e 0 graus
(c)24 pés e 45 graus
(d)24 pés e 80 graus
Nota: Você precisará usar a fórmula trigonométrica:
A função sin() do módulo math toma sua entrada em radianos. Assim, você precisará
converter o ângulo dado em graus para o ângulo dado em radianos, usando:
"""
import fractions
import math
# A função sin() do módulo math toma sua entrada em radianos. Assim é necessário converter o ângulo dado em graus para o
# o ângulo em radianos



def calc_altura(comprimento, angulo):
    radianos = (math.pi*angulo) / 180
    altura = comprimento*radianos
    return altura

print(calc_altura(16, 75))