#importamos o pymysql para fazermos do banco com o python
import pymysql as pySQL

#para saber qual versao esta do meu pymysql
'''print(pySQL.version_info)'''


#dados dos bancos de dados para conexao
conexao = pySQL.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_livrariaonline",
    port=3306

)

#cursor insere e busca informacoes como select e insert, pySQL.cursors.DictCursor(quando colocamos desta forma receberemos as informacoes como dicionario)
cursor = conexao.cursor(pySQL.cursors.DictCursor)#cursor e como se fosse um tradutor

#estamos buscando todos os resgistros
'''
cursor.execute("SELECT * FROM clientes")#aqui informamos quais comandos MYSQL
todos = cursor.fetchall()#criamos uma variavel que quando usado cursor.fetchall() nos mostrara tudo o que tera dentro tabela de clientes

#usamos um for para passar por clientes e pegar todos os dados e depois de percorrer toda minha tabela clientes print todos o resgistro na coluna nome e email
for clientes in todos:
    print(clientes["nome"],"-", clientes["email"], "-", clientes["telefone"])
'''

'''
cursor.execute("SELECT id_cliente, nome FROM clientes WHERE id_cliente = 1")#neste comando SQL selecionamos id_cliente e nome
#que estao em tabela clientes onde o id_cliente e igual a 1

clientes = cursor.fetchone()#pedimos para retornar somente um dado diferente do fetchall que retorna varios dados, vai funcionae com os dois
#porem em questao de organizar o codigo o ideal sera usar o fetchone por so querer retornar alguns dados em especifico e nao varios

print(clientes)
'''

nome_busca = "Ursula%"
cursor.execute("SELECT * FROM clientes WHERE nome LIKE %s", (nome_busca), )# aqui usamos o like para parar em nome e tudo apos ursula 
#sera ignorado como segundo nome e sobrenome, usamos esse %s para passar uma variavel como fizemos em (nome_busca)

resultado = cursor.fetchall()#aqui criamos uma variavel que tera cursor nela com o fetchall que retorna tudo no nosso cursor que 
#esta buscando informacoes no banco usando o execute que vai executar os comandos dentro dos () like por ser string e %s para usarmos 
#uma variavel

print(resultado)


