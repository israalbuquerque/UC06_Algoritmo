import pandas as pd

nome = str(input("Digite seu nome: "))
idade = str(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
}

# Lê o Excel existente
leitura_excel = pd.read_excel("aula12/cadastro_alunos.xlsx")

# Adiciona os novos dados na próxima linha disponível
linha_nova = len(leitura_excel)
leitura_excel.loc[linha_nova, "nome"] = nome
leitura_excel.loc[linha_nova, "idade"] = idade
leitura_excel.loc[linha_nova, "altura"] = altura

# Salva novamente no Excel
leitura_excel.to_excel("aula12/cadastro_alunos.xlsx", index=False)
