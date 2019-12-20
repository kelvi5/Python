n1 = int(input('Digite o numero que deseja saber o fatorial: '))
fat = 1
aux = n1
for i in range(n1, 0, -1):
    fat = (n1 * fat)
    n1 = n1 - 1

print('O fatorial de {} é {:.2f}'.format(aux, fat))