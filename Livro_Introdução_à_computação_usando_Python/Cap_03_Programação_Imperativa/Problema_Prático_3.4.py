"""
Implemente um programa que comece pedindo ao usuário para digitar uma identificação de login
(ou seja, uma string). O programa, então, verifica se a identificação informada pelo usuário está
na lista ['joe', 'sue', ' hani', 'sophie' ] de usuários válidos. Dependendo do
resultado, uma mensagem apropriada deverá ser impressa. Não importando o resultado, sua
função deverá exibir 'Fim.' antes de terminar. Aqui está um exemplo de um login bemsucedido:
>>>
Login: joe
Você entrou!
Fim.
E aqui está um que não tem sucesso:
>>>
Login: john
Usuário desconhecido.
Fim.
"""
login = input('Login: ')
users = ['joe', 'sue', ' hani', 'sophie']
if login.lower() in users:
    print('Você entrou!')
else:
    print('Usuário desconhecido.')
print('Fim')
