'''
Escreva expressões Python correspondentes ao seguinte:
 (a)O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
 (b)O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
 (c)A área de um disco com raio a
 (d)O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está dentro de um círculo com centro (a, b) e raio r
'''

import math
# (a)O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
a = 2
b = 3

hip = math.sqrt((a**2)+(b**2))
print(hip)

# (b)O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
print((math.sqrt((a**2)+(b**2)))>5)

#  (c)A área de um disco com raio a
raio = a
area = math.pi*(raio**2)
print(area)

#(d)O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está dentro de um círculo com centro (a, b) e raio r

#Primeiro calcula-se a distância entre os dois pontos (x e y e o centro do círculo) de acordo com o plano cartesiano
#Para isso, utiliza-se o teorema de pitágoras, com os dois pontos é possível formar um triângulo retângulo e a hipotenusa é a distância entre os pontos
#Depois, se a distância entre os dois pontos for maior que o raio do círculo, significa que o ponto está fora da área do círculo
x = 8
y = 5
a = 4
b = 2
raio = 4
distancia = math.sqrt(((y-b)**2)+((x-a)**2))

print((math.sqrt(((y-b)**2)+((x-a)**2))) <= raio)