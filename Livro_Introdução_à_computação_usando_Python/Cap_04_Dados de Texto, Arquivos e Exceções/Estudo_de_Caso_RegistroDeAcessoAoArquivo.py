import time


def openlog(file, modo='r'):
    '''Abre arquivo file em certo modo e retorna referência ao arquivo aberto; registra o acesso ao arquivo log.txt'''

    arqentrada = open(file, modo)

    # Obtém a hora atual
    now = time.localtime()
    nowformat = time.strftime('%A %b/%d/%y %I:%M %p', now)

    # Abre o arquivo log.txt no modo de acréscimo e acrescenta log
    arqsaida = open('log.txt', 'a')
    log = '{}: Arquivo {} aberto.\n'
    arqsaida.write(log.format(nowformat, file))
    arqsaida.close()

    return arqentrada

openlog('example.txt', 'r')
openlog('log.txt', 'r')
