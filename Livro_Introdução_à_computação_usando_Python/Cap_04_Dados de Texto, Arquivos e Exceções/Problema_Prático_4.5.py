"""
Suponha que as
variáveis primeiro, último, rua, número, cidade, estado, codPostal já tenham
sido atribuídas. Escreva uma instrução print que crie uma etiqueta de correspondência:
John Doe
123 Main Street
AnyCity, AS 09876
supondo que:
"""

primeiro = 'John'
ultimo = 'Doe'
rua = 'Main Street'
numero = 123
cidade = 'AnyCity'
estado = 'AS'
codPostal = '09876'
print('{} {}\n{} {}\n{}, {} {}'.format(primeiro, ultimo, numero, rua, cidade, estado, codPostal))
