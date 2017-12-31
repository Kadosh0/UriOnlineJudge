u = int(input())
ano = u // 365
anor = u % 365
mes = anor // 30
dia = anor % 30
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))
