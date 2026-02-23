#Aula 04
#colocamos o input, para o usuario escrever
#feita uma conversao de string para int
#feita uma conversao de string para float




'''numeros = int(input("digite um numero de 1 ate 10: ")) 
soma = numeros + 10 

print (soma)

calculo_salario = float(input("Digite seu salario: ")) 
soma_salario = calculo_salario * 3.5


print(soma_salario)

'''
#Aqui foi usada o IF ELSE
#Necessario identar como no IF que apos a condicao colocamos oque sera printado para o usuario

"""idade = 16

if idade >= 18:
    print("sua idade é:", idade)
else:
    print("Sua idade e menor que 18 anos sendo ela:", idade)

"""
#Outro exemplo de IF ELSE


'''Valida_idade = int(input("Digite sua idade: "))

if Valida_idade < 18:
    print("Você é menor de idade e precisa da presenca dos pais")

else:
    print("Você é maior de idade, pode entra!")

'''

#Aqui foi usado o IF ELIF e ELSE
#Usamos aqui uma outra forma de print, (nao usar esse use separando com ",")

"""nota = int(input("Digite a nota do aluno: "))

nome_aluno = input("Digite o nome do aluno: ")

if nota >= 9 :
    print(f"O aluno {nome_aluno} está aprovado com a nota {nota}")

elif nota >= 7 and nota<= 8:
    print(f"O aluno {nome_aluno} está aprovado por canselho, com a nota {nota}")

else:
    print(f"O aluno {nome_aluno} está reprovado, com a nota {nota}")
"""

#Se o usuario for menor de idade entao ele precisa ter a autorizacao 
#Se o usuario for maior de idade entao ele precisa ter a altura minima
#Colocamos um IF ELSE dentro de um ELSE e nao é preciso colocar o print do primeiro ELSE, ele esta comentado 

"""idade_cliente = int(input("Digite a idade do cliente: "))
altura_cliente = float(input("Digite a altura cliente:  ")) 

if idade_cliente < 18:
    print("O cliente e menor de idade e não pode entrar no brinquedo")

else:
    if altura_cliente >= 1.50:
        print("Você é maior de idade e tem a altura minima para o brinquedo")
    else:
        print("Você mesmo sendo maior de idade tem menos que 1.50 de altura e não pode ir ao brinquedo")
    
    #print("Cliente maior de idade pode subir no brinquedo")
"""

    #Operadores ternários
    #É uma outra forma de usar o IF e ELSE 
    #Condicional ternários

valida_idades= 10
status = print("Menor de idade") if valida_idades < 18  else print("Maior de idade")
print(status)



