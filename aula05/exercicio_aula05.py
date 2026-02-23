#Exercicio da tabuada
#numero_tabuada()
'''
numero_escolhido  = input("Digite um número para te mostrar a tabuada respectiva ao número de 1 a 10: ")
resultado = 0
multiplicacao = 0


if numero_escolhido.isdigit() == 1 or numero_escolhido.isdigit() == 2  or numero_escolhido.isdigit() == 3  or numero_escolhido.isdigit() == 4  or numero_escolhido.isdigit() == 5  or numero_escolhido.isdigit() == 6 or numero_escolhido.isdigit() == 7  or numero_escolhido.isdigit() == 8  or numero_escolhido.isdigit() == 9  or numero_escolhido.isdigit() == 10:
    
    
    while multiplicacao <= 10:
        numero_escolhido = int(numero_escolhido) # necessaria uma conversao para
        resultado = multiplicacao *  numero_escolhido
        print(multiplicacao, "X ", numero_escolhido , "=", resultado)

        multiplicacao += 1

else:
    print("Número invalido, por favor digite um número valido de 1 a 10")
'''
numero_escolhido  = input("Digite um número para te mostrar a tabuada respectiva ao número de 1 a 10: ")
resultado = 0
multiplicacao = 0
escolha = ""


if numero_escolhido.isdigit() == 1 or numero_escolhido.isdigit() == 2  or numero_escolhido.isdigit() == 3  or numero_escolhido.isdigit() == 4  or numero_escolhido.isdigit() == 5  or numero_escolhido.isdigit() == 6 or numero_escolhido.isdigit() == 7  or numero_escolhido.isdigit() == 8  or numero_escolhido.isdigit() == 9  or numero_escolhido.isdigit() == 10:
    
    
    while multiplicacao <= 10:
        numero_escolhido = int(numero_escolhido) # necessaria uma conversao para
        resultado = multiplicacao *  numero_escolhido
        print(multiplicacao, "X ", numero_escolhido , "=", resultado)

        multiplicacao += 1

else:
    print("Número invalido, por favor digite um número valido de 1 a 10")


while escolha == "S" or "s":
    if escolha == "S" or "s":
        escolha = input("Você deseja digitar um novo número? S/N: ")
        numero_escolhido  = input("Digite um número para te mostrar a tabuada respectiva ao número de 1 a 10: ")
    
        resultado = 0
        multiplicacao = 0
        escolha = ""


        if numero_escolhido.isdigit() == 1 or numero_escolhido.isdigit() == 2  or numero_escolhido.isdigit() == 3  or numero_escolhido.isdigit() == 4  or numero_escolhido.isdigit() == 5  or numero_escolhido.isdigit() == 6 or numero_escolhido.isdigit() == 7  or numero_escolhido.isdigit() == 8  or numero_escolhido.isdigit() == 9  or numero_escolhido.isdigit() == 10:
    
    
            while multiplicacao <= 10:
                numero_escolhido = int(numero_escolhido) # necessaria uma conversao para
                resultado = multiplicacao *  numero_escolhido
                print(multiplicacao, "X ", numero_escolhido , "=", resultado)

                multiplicacao += 1
        #escolha = input("Você deseja digitar um novo número? S/N: ")
        else:
            print("Número invalido, por favor digite um número valido de 1 a 10")

    else:
        print("Obrigado!")