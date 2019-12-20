import Modulos as mo

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

soma = mo.soma(n1, n2)
dividir = mo.dividir(n1, n2)

print('A soma é igual à: {} \nA divisão é igual à: {}'.format(soma, dividir))