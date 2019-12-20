x = {'nome': 'Kelvin', 'idade': 18, 'telefone': '123456789'}

print(x)
print(x['nome'])
print(len(x))
x.pop('idade')
print(x)

cadastroPessoas = [{'nome': 'Kelvin', 'idade': 23, 'telefone': '12345678'},
                   {'nome': 'Jurema', 'idade': 27, 'telefone': '98765432'},
                   {'nome': 'Fulano', 'idade': 54, 'telefone': '45456565'}]

print(cadastroPessoas[2]['nome'])

for i in cadastroPessoas:
    print(i)

