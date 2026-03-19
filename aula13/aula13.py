#importamos o pymysql para fazermos do banco com o python
import pymysql as pySQL

#para saber qual versao esta do meu pymysql
print(pySQL.version_info)


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

cursor.execute("SELECT * FROM clientes")#aqui informamos quais comandos MYSQL
todos = cursor.fetchall()#criamos uma variavel que quando usado cursor.fetchall() nos mostrara tudo o que tera dentro tabela de clientes

#usamos um for para passar por clientes e pegar todos os dados e depois de percorrer toda minha tabela clientes print todos o resgistro na coluna nome e email
for clientes in todos:
    print(clientes["nome"],"-", clientes["email"], "-", clientes["telefone"])



