media = 0
cont = 0

for i in range(1, 8):
    peso = int(input('Digite o peso da {} pessoa: '.format(i)))
    media = peso + media

    if peso > 90:
        cont = cont + 1

print('A media de peso é de: {:.2f}\nO numero de pessoas que pesa acima de 90Kg é de: {}'.format(media/7, cont))