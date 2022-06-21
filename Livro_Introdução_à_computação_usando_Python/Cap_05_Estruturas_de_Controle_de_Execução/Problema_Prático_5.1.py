"""
Implemente a função meuIMC(), que aceita como entrada a altura de uma pessoa (em metros) e
o peso (em quilos) e calcula o Índice de Massa Corporal (IMC) dessa pessoa. A fórmula do IMC
é:
Sua função deverá exibir a string 'Abaixo do peso' se o imc <
18.5, 'Normal' se 18,5 <= imc < 25, e 'Sobrepeso' se imc >= 25.
>> meuIMC *86, 1.90)
Normal
>> meuIMC (63, 1.90)
Abaixo do peso
"""


def meuIMC(altura, peso):
    imc = peso/(altura**2)
    if imc < 18.5:
        print('Abaixo do peso')
    elif 18.5 <= imc < 25:
        print('Normal')
    else:
        print('Sobrepeso')
    print(f'IMC: {imc}')


meuIMC(1.70, 72)
