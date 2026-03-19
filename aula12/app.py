import pandas as pd

print("================================================")
print("        BEM - VINDO AO PORTAL DE ALUNOS")
print("================================================\n")
print("     Digite uma opção no menu")
print("         1 > Criar")
print("         2 > Adicionar")
print("         3 > Apagar")
opcao = int(input("R: "))

if opcao == 1:
    print("Opção 1 selecionada")
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    
    dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
    }

    excel = pd.DataFrame(dados)

    excel.to_excel("aula12\Alunos.xlsx", index = False)
    print("Ação finalizada...")

elif opcao == 2:
    print("Opção 2 selecionada...")
    
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))
    
    dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
    }
    leitura_excel = pd.read_excel("aula12\Alunos.xlsx")#estamos lendo o arquivo excel
    
    nova_linha = len(leitura_excel)#uma variavel e nela usamos o len para ler a quantidade de dados na variavel

    leitura_excel.loc[nova_linha, "nome"] = dados["nome"] # aqui estamos pegando aquele dataframe que foi criado informando linha e coluna que recebera do dicionario dados a variavel nome que recebe-ra do usuario
    leitura_excel.loc[nova_linha, "idade"] = dados["idade"]
    leitura_excel.loc[nova_linha, "altura"] = dados["altura"]

    leitura_excel.to_excel("aula12\Alunos.xlsx", index = False)

    print("Ação finalizada...")

elif opcao == 3:
    print("Opção 3 selecionada...")
    linha_apagada = int(input("Digite um número inteiro: "))#pede para o usuario digitar
    leitura_excel = pd.read_excel("aula12\Alunos.xlsx")#estamos lendo o arquivo excel(dataframe)
    leitura_excel = leitura_excel.drop(linha_apagada)#aqui usamos nossa cariavel que armazena o dataframe que sera ela mesmo com um drop para apaga-la, passando a variavel que o usuario digitou que sera a linha que foi digitada pelo usuario

    leitura_excel.to_excel("aula12\Alunos.xlsx", index = False)

    print("Ação finalizada...")






#streamlist()