arquivo = open('aulaPython.txt', 'r')
'''
arquivo.write('Ola tudo bem!')

texto = '\nasdasdasdasdasdasdsad'
arquivo.write(texto)
'''
escreve  = arquivo.readlines()

print(escreve)

arquivo.close()