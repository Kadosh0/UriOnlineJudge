valor = int(input())

horas = valor // 3600 # // pega a parte inteira da divisão do valor/3600
minutos = (valor % 3600) // 60 # % pega o resto da divisão do valor/3600
segundos = valor % 60

print('{}:{}:{}'.format(horas, minutos, segundos))
