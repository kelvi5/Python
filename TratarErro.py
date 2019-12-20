passou = 1
while passou != 0:
    try:
         x = int(input('Digite sua Idade: '))
         passou = 0
    except:
         print('Você não digitou numeros.')
         passou = 1

print('A sua idade é {}'.format(x))