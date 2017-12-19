from math import sqrt
xy1 = input().split()
xy2 = input().split()
x1, y1 = xy1
x2, y2 = xy2
distancia = sqrt(((float(x2) - float(x1)) ** 2) + ((float(y2) - float(y1)) ** 2))
print('{:.4f}'.format(distancia))
