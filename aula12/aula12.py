#ouve a importacao da biblioteca pandas e as pd(demos o apelido para a biblioteca pandas em pd)
import pandas as pd
 #aqui criamos variaveis do tipo input para a entreda de dados do usuario


nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

#criamos um  dicionario com [] e a variavel dentro dos conchetes, quando criamos com as variaveis desta forma fica dinamica o dicionario e elimentado de forma "direta"
#EX: nome: [nome]
dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
    }

#aqui definimos uma variavel que que usara o pandas(pd) a funcao dataframe(que entende os dados no formato do excel), do nosso dicionario dados
'''excel = pd.DataFrame(dados)'''

#to.excel() serve para criar uma nova planilha, pegar os dados digitados pelo usuario em formato dataframe e gravar na planilha criada, usamos o index = false, 
# devemos executar essa linha uma vez
'''excel.to_excel("aula12\cadastro_alunos.xlsx", index = False)'''

#ler o excel do python
#aqui teremos uma variavel com nome(leitura_excel) sera lido o excel usando o pd(apelido para pandas), read_excel()(funcao que le arquivos excel), "aula12\cadastro_alunos.xlsx"(aqui esra o caminho do arquivo)
#estara dentro da pasta aula12 e no nome do arquivo e cadastro_alunos.xlsx
leitura_excel = pd.read_excel("aula12\cadastro_alunos.xlsx")

#loc precisa do numero da linha e numero da coluna
#aqui teremos uma variavel nova_linha que len(lera) a variavel leitura_excel
'''
nova_linha = len(leitura_excel)

#leitura_excel.loc(usado para modificar a proxima coluna como nome, idade e altura, adicionando uma nova linha e essa nova linha ou dado vai para o dicionario dados
#para a chave nome)

leitura_excel.loc[nova_linha, "nome"] = dados["nome"]
leitura_excel.loc[nova_linha, "idade"] = dados["idade"]
leitura_excel.loc[nova_linha, "altura"] = dados["altura"]
'''
#salvar a planilha
#aqui estamos pegando um dataframe e transformando no tipo excel, "aula12\cadastro_alunos.xlsx"(aqui e o caminho onde os dados estao sendo salvos)
leitura_excel.to_excel("aula12\Alunos.xlsx", index = False)

'''print(leitura_excel["nome"])'''

#criar, ler, editar, apagar



#apagar linhas de uma planilha
#usado para apagar a linha d excel definimos a variavel  e sera i gual a mesma varivael porem agora com o drop(3) e dentro sua linha aque tera que ser apagada
#lenbrando 
'''leitura_excel = leitura_excel.drop(3)'''

leitura_excel.loc[3, "nome"] = dados["nome"]
leitura_excel.loc[3, "idade"] = dados["idade"]
leitura_excel.loc[3, "altura"] = dados["altura"]

leitura_excel.to_excel("aula12\cadastro_alunos.xlsx", index = False)













