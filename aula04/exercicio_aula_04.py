#Israel

#Exercico que verifica qual o maior numero


numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print("O primeiro número e maior sendo ele", numero1 ,"e o segundo sendo ", numero2)

else:
    if numero1 == numero2:
        print("Os números são igual sendo eles ", numero1, "e", numero2)
        
    else:
        print("O primeiro número é menor sendo ele ", numero1, " e o segundo sendo ", numero2)




#Exercico número par/impar

num1 =  int(input("Digite o valor: "))


if num1 % 2 == 0:
    print("O número que você digitou é ",num1,", sendo ele par", )

else:
    print("O número que você digitou é ",num1, ", sendo ele impar3 ", )

'''
'''
#Exercicio escolha numero que representa mês 

mes = int(input("Digite um numero de 1 a 12 para retornar os mês respectivo : "))

if mes == 1:
    print("Janeiro")
elif mes == 2:
    print("Fevereiro")
elif mes == 3:
    print("Março")
elif mes == 4:
    print("abril")
elif mes == 5:
    print("Maio")
elif mes == 6:
    print("Junho")
elif mes == 7:
    print("Julho")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Setembro")
elif mes == 10:
    print("Outubro")
elif mes == 11:
    print("Novembro")
elif mes == 12:
    print("Dezembro")
else:
    print("O número digitado não está dentro da sequência de 1 a 12, sendo ele: ", mes)


