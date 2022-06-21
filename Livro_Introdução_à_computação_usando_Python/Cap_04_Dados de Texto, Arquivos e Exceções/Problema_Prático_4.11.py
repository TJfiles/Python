import time

hora = time.time()  # segundos da época, desde 1 de janeiro de 1970
print(hora)

hora = time.gmtime()
print(hora)

hora = time.localtime()  # mesmo formato de gmtim() porém respeitando o fuso horário local
print(hora)

"""
%a Nome do dia da semana abreviado
%A Nome do dia da semana completo
%m Número do mês
%b Nome do mês abreviado
%B Nome do mês completo
%d O dia do mês como um número decimal entre 01 e 31
%H As horas como um número entre00e 23
%I As horas como um número entre 01e12
%M Os minutos como um número entre00e 59
%p AM ou PM
%S Segundos como um número entre00e61
%y O ano como um número entre00e 99
%Y O ano como um número de quatro dígitos
%Z Nome do fuso horário
"""

hora = time.strftime('%A %b/%d/%y %I:%M %p %Z', time.localtime())
print(hora)

"""
Comece definindo t como a hora local 1.500.000.000 segundos a partir do início de 1.º de janeiro
de 1970 UTC:
>>> import time
>>> t = time.localtime(1500000000)
Construa as próximas strings usando a função de hora em formato de string strftime():
(a)'Thursday, July 13 2017'
(b)'09:40 PM Hora oficial do Brasil em 13/07/2017'
(c)'Te encontro em Thu July 13 às 09:40 PM.'
"""

t = time.localtime(1500000000)

print(time.strftime('%A, %B %d %Y', t))
print(time.strftime('%I:%M %p %Z em %d/%m/%Y', t))
print(time.strftime('Te encontro em %a %B %d às %I:%M %p.', t))