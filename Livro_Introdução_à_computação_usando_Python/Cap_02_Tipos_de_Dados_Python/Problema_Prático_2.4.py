"""
Comece executando as instruções de atribuição:
"""
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# Escreva expressões Python usando s1, s2, e s3 e os operadores + e * a fim de avaliar para:

# (a) 'ant bat ant'
print(s1+s2+s1)

# (b) 'ant ant ant ant ant ant ant ant ant ant'
print(10*(s1+' '))

# (c) 'ant bat bat cod cod cod'
print(s1+' '+(2*(s2+' '))+(3*(s3+' ')))

# (d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
print(7*(s1+' '+s2+' '))

# (e) 'batbatcod batbatcod batbatcod batbatcod'
print(4*(2*s2+s3+' '))
