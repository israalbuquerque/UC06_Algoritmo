#Exercicio
#crie um programa que: peca nome e idade, salve no arquivo cadastro.txt, cada cadastro deve ficar em uma linha
#dica: with open("aula10/cadastro.txt", "a") as arquivo:
            #arquivo.wirte(nome+ "-" idade + "/n")

while True:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    def pede_dados(nome, idade):



        if idade.isdigit():
            idade = int(idade)
        else:
            print("Valor digitado em idade não e um numero!")


        if type(nome) == str and type(idade) == int:
            with open("aula10/cadastro.txt", "a") as arquivo_nome:
                arquivo_nome.write(nome + "-" + str(idade) + "\n")


        # else:
        #     print("O tipo de dado inserido foi incorreto!")




    pede_dados(nome, idade)

    escolha = input("Você quer realizar a açaõ novamente [S/N]: ").lower()
    if escolha != "s":
        print("Ação cancelada!")
        break