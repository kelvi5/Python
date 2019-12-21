import pymysql.cursors

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'curso',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = conexao.cursor()

'''cursor.execute('create table pessoas( nome varchar(30), idade int, endereco varchar(100))')
x = 'drop table pessoas'
cursor.execute(x)
cursor.close()
conexao.close()
'''

x = 'create table testandoWith(nome varchar(100))'

with conexao.cursor() as cursor:
    cursor.execute(x)

print('Saiu!')