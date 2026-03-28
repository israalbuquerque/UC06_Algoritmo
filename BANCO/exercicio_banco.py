#  Banco Tabajara
# Nome do arquivo: banco_tabajara.py
# nome excel: base_BANCO_TABAJA

# Vamos criar um sistema bancário chamado banco tabajara, nosso banco terá as seguintes caracteristicas:

"""
Contas:
- Corrente
- Poupança
- Salario


Dados do cliente que vamos guardar em um excel:
- nome_cliente
- tipo_conta
- numero_conta
- cpf
- agencia
- extrato_bancario
- deposito
- saque

Obs: Esse serão os nomes das colunas no nosso excel

Seguintes regras de saque para cada conta:
Saques na conta Corrente: 5% de taxa
Saques na conta Corrente: Poupança 0% de taxa
Saques na conta Corrente: Salario 2% de taxa

DESENVOLVIMENTO

Crie um menu com as seguintes opções:
1 - Criar conta
2 - Acessar conta

Regras para cada opção no menu
1 - Criar conta > Solicitar ao usuario para digitar as seguintes informações:
- nome_cliente
- cpf
- tipo_conta

O outros campos serão gerados de forma automatica
- numero_conta = Será gerada de forma sequencial começando do 0 até 100
- agencia = será gerado de forma sequencial começando do 400 até 700
- extrato_bancario = valor inicial terá que começar em 0

Ao finalizar mostrar para o usuário o nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario


2 - Acessar conta > É necessário que o usuário passe os seguites dados:
- cpf
- numero_conta
> Precisa percorrer o excel e encontra o cliente com os mesmo dados de cpf e numero_conta caso encontre o cliente na base retornar uma mensagem: "Bem-vindo "nome_cliente" ao banco Tabajara" SENAO se o usuario não existir na base então retornamos uma mensagem "Usuário não encontrado, tentar novamente ou realizar o cadastro"
"""
'''
import pandas as pd
import os

PATH = "BANCO/cadastro_clinetes.xlsx"


print("**************** MENU ***************")

print("1- Criar conta")
print("2- Acessar conta")

print("**************************************")

escolha = input("Escolha uma das opções: ")

if escolha.isdigit():
    escolha = int(escolha)
    
    if escolha == 1:
        nome_cliente = input("Digite seu nome completo: ")
        cpf_cliente = float(input("Digite seu cpf: "))
        print("******** Escolha uma dos tipos de contas ******** ")
        print("1- Corrente ")
        print("2- Poupança ")
        print("3- Salário")
        conta_cliente = input("Digite sua conta que deseja criar: ")
        if conta_cliente.isdigit():
            conta_cliente = int(conta_cliente)
            
            dados_inclientes = {
                "nome_cliente": [nome_cliente],
                "cpf_cliente": [cpf_cliente],
                "conta_cliente": [conta_cliente]
            }

            
            if os.path.exists(PATH):
                ler_dt = pd.read_excel(PATH)
                novo_cadastro = len(ler_dt)

                ler_dt.loc[novo_cadastro, "nome_cliente"] = dados_inclientes["nome_cliente"]
                ler_dt.loc[novo_cadastro, "cpf_cliente"] = dados_inclientes["cpf_cliente"]
                ler_dt.loc[novo_cadastro, "conta_cliente"] = dados_inclientes["conta_cliente"]

                ler_dt.to_excel("BANCO\cadastro_clinetes.xlsx", index = False)

                planilha = ler_dt
                
            else:
                os.makedirs("BANCO", exist_ok=True)
                dt = pd.DataFrame(dados_inclientes)
                dt.to_excel(PATH, index = False)
            print("Ação concluida com sucesso!")

            
        else:
            print("Número invalido!")

    elif escolha == 2:
        print("*********Para acessar sua conta nos informe**********")
        usuario = input("Seu cpf:  ")
        conta = input("Número conta:  ")

        for usuario, conta in PATH:
            if usuario == usuario and conta == conta:
                print("Seja bem vindo",["nome"])

else:
    print("O que foi digitado não é um número valido!")

'''
 
#  Banco Tabajara
# Nome do arquivo: banco_tabajara.py
# nome excel: base_BANCO_TABAJA
 
# Vamos criar um sistema bancário chamado banco tabajara, nosso banco terá as seguintes caracteristicas:
 
"""
Contas:
- Corrente
- Poupança
- Salario
 
 
Dados do cliente que vamos guardar em um excel:
- nome_cliente
- tipo_conta
- numero_conta
- cpf
- agencia
- extrato_bancario
- deposito
- saque
 
Obs: Esse serão os nomes das colunas no nosso excel
 
Seguintes regras de saque para cada conta:
Saques na conta Corrente: 5% de taxa
Saques na conta Corrente: Poupança 0% de taxa
Saques na conta Corrente: Salario 2% de taxa
 
DESENVOLVIMENTO
 
Crie um menu com as seguintes opções:
1 - Criar conta
2 - Acessar conta
 
Regras para cada opção no menu
1 - Criar conta > Solicitar ao usuario para digitar as seguintes informações:
- nome_cliente
- cpf
- tipo_conta
 
O outros campos serão gerados de forma automatica
- numero_conta = Será gerada de forma sequencial começando do 0 até 100
- agencia = será gerado de forma sequencial começando do 400 até 700
- extrato_bancario = valor inicial terá que começar em 0
 
Ao finalizar mostrar para o usuário o nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario
 
 
2 - Acessar conta > É necessário que o usuário passe os seguites dados:
- cpf
- numero_conta
> Precisa percorrer o excel e encontra o cliente com os mesmo dados de cpf e numero_conta caso encontre o cliente na base retornar uma mensagem: "Bem-vindo "nome_cliente" ao banco Tabajara" SENAO se o usuario não existir na base então retornamos uma mensagem "Usuário não encontrado, tentar novamente ou realizar o cadastro"
"""
import pandas as pd
import os
import random as rd

PATH = "BANCO/cadastro_clinetes.xlsx"

print("**************** MENU ***************")

print("1- Criar conta")
print("2- Acessar conta")

print("**************************************")

escolha = input("Escolha uma das opções: ")

if escolha.isdigit():
    escolha = int(escolha)

    if escolha == 1:
        nome_cliente = input("Digite seu nome completo: ")
        cpf_cliente = int(input("Digite seu cpf: "))
        print("******** Escolha uma dos tipos de contas ******** ")
        print("1- Corrente ")
        print("2- Poupança ")
        print("3- Salário")
        conta_cliente = input("Digite sua conta que deseja criar: ")

        if conta_cliente.isdigit():
            conta_cliente = int(conta_cliente)

            if conta_cliente == 1:
                conta_cliente = "Corrente"
            elif conta_cliente == 2:
                conta_cliente = "Poupança"
            elif conta_cliente == 3:
                conta_cliente = "Salário"

            
            
            numero_conta = 0
            agencia = 400
            extrato = 0
            dados_inclientes = {
                "nome_cliente": [nome_cliente],
                "cpf_cliente": [cpf_cliente],
                "conta_cliente": [conta_cliente],
                "numero_conta": [numero_conta],
                "agencia": [agencia],
                "extrato": [extrato]
            }

            if os.path.exists(PATH):
                ler_dt = pd.read_excel(PATH)
                
                
                numero_conta = len(ler_dt) + 1
                agencia = 400 + len(ler_dt)
                extrato = 0

                dados_inclientes = {
                "nome_cliente": nome_cliente,
                "cpf_cliente": cpf_cliente,
                "conta_cliente": conta_cliente,
                "numero_conta": numero_conta,
                "agencia": agencia,
                "extrato": extrato
    }

                if numero_conta > 100:
                    print("Número de contas atingidos")
                    exit()
                
                

                novo_cadastro = len(ler_dt)

                ler_dt.loc[novo_cadastro, "nome_cliente"] = dados_inclientes["nome_cliente"]
                ler_dt.loc[novo_cadastro, "cpf_cliente"] = dados_inclientes["cpf_cliente"]
                ler_dt.loc[novo_cadastro, "conta_cliente"] = dados_inclientes["conta_cliente"]
                ler_dt.loc[novo_cadastro, "numero_conta"] = dados_inclientes["numero_conta"]
                ler_dt.loc[novo_cadastro, "agencia"] = dados_inclientes["agencia"]
                ler_dt.loc[novo_cadastro, "extrato"] = dados_inclientes["extrato"]

                ler_dt.to_excel(PATH, index = False)

            
            
            else:
                os.makedirs("BANCO", exist_ok=True)
                dt = pd.DataFrame(dados_inclientes)
                numero_conta = 0
                dt.to_excel(PATH, index = False)
            print("Ação concluida com sucesso!")

        else:
            print("Número invalido!")
        print("----------Os dados são---------- ", "\nNome: ",nome_cliente,"\nCPF: ", cpf_cliente, "\nTipo conta: ",conta_cliente,"\nNumero conta: ", numero_conta,"\nAgência: ", agencia, "\nExtrato: ", extrato)
        #nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario


    elif escolha == 2:
        print("*********Para acessar sua conta nos informe**********")
        cpf_digitado = str(input("Seu cpf:  "))
        conta = str(input("Número conta:  "))
        encontrado = False

        ler_dt = pd.read_excel(PATH)

        for i, linha in ler_dt.iterrows():
            if str(int(linha["cpf_cliente"])) == cpf_digitado and str(int(linha["numero_conta"])) == conta:
                encontrado = True
                nome =  linha["nome_cliente"]
                break
        if encontrado:
            print("------------Bem vindo", nome, "----------------------")
            print("1- Saque")
            print("2- Deposito")
            print("3- Saldo")
            opcao = input("Digite uma opção: ") 
            print("-----------------------------------------------------")

            ler_dt = pd.read_excel(PATH)
            extrato = float(linha["extrato"])
            taxa_corrente = 0.05
            taxa_salario = 0.02

            if opcao.isdigit():
                opcao = float(opcao)
                if opcao == 1:
                    print("---------Você escolheu a opção saque---------------")
                    valor_saque = float(input("Digite o valor que quer saquar: "))
                    if valor_saque <= extrato:
                        if ler_dt.loc[i,"conta_cliente"] == "Corrente":
                            atualizacao_extrato = extrato - (valor_saque +(valor_saque * taxa_corrente))
                            ler_dt.loc[i, "extrato"] = atualizacao_extrato
                            ler_dt.to_excel(PATH, index = False)
                        
                            print("Saque realizado com sucesso!")
                            print("Saque: ", valor_saque)
                            print("Valor em conta: ", atualizacao_extrato)
                            print("Taxa para saque: 5%")
                            print("Valor de desconto saque: ", atualizacao_extrato)
            
                        elif ler_dt.loc[i,"conta_cliente"] == "Salário":
                            atualizacao_extrato = extrato - (valor_saque +(valor_saque * taxa_salario))
                            ler_dt.loc[i, "extrato"] = atualizacao_extrato
                            ler_dt.to_excel(PATH, index = False)
                        
                            print("Saque realizado com sucesso!")
                            print("Saque: ", valor_saque)
                            print("Valor em conta: ", atualizacao_extrato)
                            print("Taxa para saque: 2%")
                            print("Valor de desconto saque: ", atualizacao_extrato)
            else:
                print("Opção invalida!")    

        else:
            print("Usuário não encontrado!")

else:
    print("O que foi digitado não é um número valido!")

'''
Quando o usuário selecionar a opção "2 - Acessar conta" e o campo cpf e numero_conta forem encontrados na base, além de mostrar a mensagem acima, mostre um menu com as seguintes opções:

1 - Saque
2 - Deposito
3 - Saldo

Regras para cada opção
1 - Saque > solicitar ao usuário que digite um valor, podendo ser inteiro ou de ponto flutuante:
- O valor solicitado para saque não pode ser maior que o valor em conta(coluna extrato_bancario), se for digitado um valor maior encerre o fluxo e mostre a mensagem "Valor maior que o disponivel em conta";
- Se o valor for menor que o disponivel em conta, realizar a subitração (do valor solicitado - o valor na coluna extrato_bancario - taxa de saque), quando a operação for realizada com sucesso mostre a mensagem 
print("================================================")
print(      Saque realizado com sucesso!)
print(      Saque: (valor Solicitado)
print(      Valor em conta: (coluna extrato_bancario))
print(      Taxa para saque: (seguir regras para cada conta))
print(      Valor de desconto saque: (seguir regras para cada conta))
print("================================================\n")

OBS: Criar a logica de desconto da taxa para cada conta especifica



2 - Deposito > solicitar ao usuário que digite um valor, podendo ser inteiro ou de ponto flutuante, se o valor for valido então somar com o valor já existente na coluna "extrato_bancario"  ao finalizar mostrar o seguinte template
print("================================================")
print("   	Valor depositado: (Variavel do valor depositado)")
print("   	Saldo em conta: (Coluna extrato_bancario)
print("================================================\n")
valor final da conta bancaria(coluna extrato_bancario);
- Se o usuário digita um número negativo então encerre o fluxo e mostre a mensagem "Numero invalido, operação encerrada";



3 - Saldo > Mostre em tela o seguinte template
print("================================================")
print("   Tipo conta: (coluna tipo_conta)")
print("   Saldo em conta: (Coluna extrato_bancario)
print("================================================\n")

'''
