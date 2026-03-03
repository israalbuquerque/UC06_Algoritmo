#Aula Funcao

nome = "Israel"#È uma varivale global

#Aqui definimos uma funcao de saudacao com print de saudacao
def saudacao(nome):
    print("Olá, seja bem vindo", nome,"!") 

#Necessario chamar a funcao para que ela apareca na compilacao
saudacao("Jose")


#Parametros sao variaveis dentro dos parenteses de uma funcao, quando passado um paremetro dentro dos () como passamos as variaveis 

#Usamos o retorno usado para retornar um valor em tela
#

def soma(valor1, valor2):
    return valor1 + valor2#Aqui pedimos para retornar o resultado de valor1 + valor2

print(soma(1457, 10))


#Como ja temos a funcao de soma basta definir uma nova variavel e ela recebe a funcaoi soma com novos valores(parametros) deninidos
salario_funcionario = 1500
beneficio = 200

novo_salario = soma(salario_funcionario, beneficio)
print(novo_salario)

#soma dois valores se idade do usuario for igual ou maior que  18
# se nao mostrar mensagem "sua idade e menor que 18"
#usamos a a variavel  resultado que recebe a funcao soma com os novos dois valores  digitados pelo usuario sendo var1 e var2 e printamos seu 
#resultado
'''
idade_usuario = int(input("Digite sua idade: "))

if idade_usuario >= 18:
    
    var1 = int(input("Digite o primeiro valor: "))
    var2 = int(input("Digite o primeiro valor: "))
    
    resultado = soma(var1, var2)
    
    print(resultado)

else:
    print("Sua idade é menor que 18 anos!")

'''
#Funcoes nativas no python, nao e necessario realizar sua montagem, ela ja vem pronta, funcao sempre vem acompanhada de parenteses

lista = [10,20,30,40,1,15]
palavra = "Anoa"
numero = "100021"

#Usamos a len para percorrer a lista e contar quantos dados estao presentes na lista, quando colocado string contara a quantidade de caracteres
#conta a quantidade de posicoes presentes no variavel
print(len(lista))
print(len(palavra))
print(len(numero))

#usamos sum para soma toda minha lista numerica

print(sum(lista))

#Usamos max para retorna o maior valor e min para retornar o menor valor

print("Maior numero em uma lista: ", max(lista))
print("Menor numero em uma lista", min(lista))

#usamos o sorted para ordenar numeros em uma lista e numeros e string das variaveis organizando as posicoes

print(sorted(lista))
print(sorted(palavra))
print(sorted(numero))

#Usamos o type para retornar o tipo da variavel como no exemplo variaveis do tipo INT e List
tipo = 10
print(type(tipo))
print(type(lista))

#Usamos int, str e float no print usamos para converter o tipo de dado que o usuario digitou para que seja printado  daquela 
# forma que definimos como no exemplo que alteramos o tipo int para float 

print(tipo)

print (float(tipo))









