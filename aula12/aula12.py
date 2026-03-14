#ouve a importacao da biblioteca pandas e as pd(demos o apelido para a biblioteca pandas em pd)
import pandas as pd

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

#criamos um  dicionario com [] e a variavel dentro dos conchetes
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

#ler o excel
leitura_excel = pd.read_excel("aula12\cadastro_alunos.xlsx")

#loc precisa do numero da linha e numero da coluna

nova_linha = len(leitura_excel)

leitura_excel.loc[nova_linha, "nome"] = dados["nome"]
leitura_excel.loc[nova_linha, "idade"] = dados["idade"]
leitura_excel.loc[nova_linha, "altura"] = dados["altura"]

leitura_excel.to_excel("aula12\cadastro_alunos.xlsx", index = False)















