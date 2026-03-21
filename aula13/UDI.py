import pymysql as pySQL# importamos a biblioteca pymysql para trabalharmos com SQL

#Aquivo para trabalhar com banco de dados para fazer as operacoes UPDATE, INSERT e DELETE

#conexao com banco de dados passando os parametros
conexao = pySQL.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_livrariaonline",
    port=3306

)

#cursor insere e busca informacoes como select e insert, pySQL.cursors.DictCursor(quando colocamos desta forma receberemos as informacoes como dicionario)
cursor = conexao.cursor(pySQL.cursors.DictCursor)#cursor e como se fosse um tradutor de ambos os lados tanto SQL e PYthon


try:
    '''
    sql_insert = "INSERT INTO clientes(nome, email) VALUES (%s, %s)"#aqui foi criada uma variavel que nele tera o insert na tabela 
    #clientes nas colunas nome e email com valores %s que serao variaveis futuras
    
    cursor.execute(sql_insert, ("Ana Limaee", "antt@email.com"))#O cursor vai chamar o execute e execute chama o sql_insert e dentro dele
    #teremos os dados que serao inseridos de forma chubada
    
    conexao.commit()#confirmar o insert, e a forma de forcar esse salvamento no banco de dados, caso isso nao seja feito nao e salvo no banco
    print("Inserindo com sucesso! ID: ", cursor.lastrowid) #aqui printamos usando o "cursor.lastrowid" que e o id criado para esse usuario
    '''
    '''
    sql_update = "UPDATE clientes SET email = %s WHERE id_cliente = %s"#criada uma variavel que tera comandos sql set(para gravar)
    # na coluna email e no id_cliente, lembrando que usamos o %s para que possamos futuramente passar dados ou variaveis 
    
    cursor.execute(sql_update,("novo@email.com", 1))#cursor chama o execute que tera o sql_update que passa o nono email e o id que sera alterado
    
    conexao.commit()#usado para salvar a alterecao no banco
    
    print("Linhas afetadas:", cursor.rowcount)#printamos e colocamos o "cursor.rowcount"(contas as linha) para nos mostrar as linhas que foram afetadas
    '''
    cursor.execute("DELETE FROM compras WHERE id_compra = %s", (2,))
    conexao.commit()
    print("Linhas  afetadas", cursor.rowcount)

except Exception as erro:
    conexao.rollback()
    print("Erro! Operação revertida: ", erro)


finally:#usamos este finally para fechar nossa conexao como banco de dados e fechamos o cursor como descrito dentro dele usando o .close()
    cursor.close()
    conexao.close()


