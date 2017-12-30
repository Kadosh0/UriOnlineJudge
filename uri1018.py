u = int(input())
n100 = u // 100
n100r = u % 100
n50 = n100r // 50
n50r = n100r % 50
n20 = n50r // 20
n20r = n50r % 20
n10 = n20r // 10
n10r = n20r % 10
n5 = n10r // 5
n5r = n10r % 5
n2 = n5r // 2
n2r = n5r % 2
n1 = n2r // 1
print('{}'.format(u))
print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(n1))
