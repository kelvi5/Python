nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))
print('Bem vindo {}.'.format(nome))
n1 = int(input('Digite a nota da sua primeira prova: '))
n2 = int(input('Digite a nota da segunda prova: '))
media = (n1 + n2) / 2
if idade >= 18 and media >= 6:
    print('Parabens você esta aprovado {}'.format(nome.title()))
else:
    print('Vocé esta reprovado, lamento')

