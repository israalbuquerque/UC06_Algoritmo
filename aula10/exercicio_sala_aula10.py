#Exercicio
#crie um programa que: peca nome e idade, salve no arquivo cadastro.txt, cada cadastro deve ficar em uma linha
#dica: with open("aula10/cadastro.txt", "a") as arquivo:
            #arquivo.wirte(nome+ "-" idade + "/n")

while True:
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")

    def pede_dados():


        if idade.isdigit():
            idade = int(idade)
        else:
            print("Valor digitado em idade não e um numero!")



        with open("aula10/cadastro.txt", "w") as arquivo_nome:
            arquivo_nome.write(nome)
        with open("aula10/cadastro.txt", "a") as arquivo_idade:
            arquivo_idade.write("\n",idade)




    pede_dados()

    escolha = input("Você quer realizar a açaõ novamente [S/N]: ").lower()
    if escolha != "s":
        print("Ação cancelada!")
        break

