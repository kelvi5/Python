cont = 0
aux = 0
for i in range(1000, 2001):
    cont = i % 11

    if cont == 5:
        aux = aux + 1
        print(i)
        
print('O numero de divisores com resto 5 é igual a: {}'.format(aux))