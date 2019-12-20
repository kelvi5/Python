nome = 'Kelvin'
idade = 23
flu = 1.2
ver = True
fal = False
print(nome, idade)
print(f'O seu nome é {nome} e você tem {idade} anos')
print('O seu nome é {} e você tem {} anos'.format(nome, idade))
print(type(nome), type(idade), type(flu), type(ver), type(fal), type(True))

str = 'Kelvin pereira da silva'
str = str.upper()
print(str)
str = str.lower()
print(str)
str = str.title()
print(str)
print(len(str))
str = str.replace('Kelvin', 'Kel')
print(str)
print(str.count('l'))
print(str.find('a'))

nome = input(print('Digite o seu nome: '))
idade = input(print('Digite sua idade: '))

print('Olá {} vocé tem {} anos'.format(nome, idade))