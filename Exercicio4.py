idade = 0
media = 0
cont = 0
while idade != -1:
    idade = int(input('Digite a idade e quando quiser parar digite -1: '))
    if idade != -1:
        media = idade + media
        cont = cont + 1

print('A idade media das pessoas é de: {}'.format(media / cont))