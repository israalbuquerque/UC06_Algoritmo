#biblioteca random e usada para gerar numeros aleatorios
#random.randint(1, 10), esta pedindo para gerar numeros aleatoiros de 1 ate 10, so gera sorteio de numeros inteiros aleatorios
#EX: numeros = random.randint(1, 10)
#print(numero)

#math retorna calculos matematicos como raiz quadrada

#datetime usamos para trabalhar com datas, hora, etc

import random
import math 
import datetime
'''
numero_aleatorio = random.randint(1000, 2000)

print(numero_aleatorio)

#Sorteio de alunos
alunos = ["Israel", "Adenilson", "Anna", "Wellington", "Jonathan", "Isabelly", "João Pedro", "Luis Felipe", "Vanessa","Daniel", 
        "João Paulo", "Lucas", "Bernardo", "Camila",  "Stefany", "Guilherme", "Micael", "Kauan"]


#Aqui usamos o random.choice(alunos), para sortear dados do tipo list tendo string
sorteado = random.choice(alunos)
sorteado2 = random.choice(alunos)
print("Dupla dinamica", sorteado, "e",sorteado2)

numero = 13890
#Aqui usamos uma variavel que guarda a funcao math.sqrt que e raiz quadrada de determinado numero como colocamos a variavel numero
raiz = math.sqrt(numero)
print(raiz)

#Pow uasdo para elevar um numero ao outro
elevado = math.pow(2,4)
print(elevado),


print(math.pow(2, 2)) 

agora = datetime.datetime.now()
print(agora.month)
'''
#Exercicio
#Solicitar ao usuario um numero de 1 ate 5 
#gerar um nuemro aleatorio usando biblioteca random.randint
# verificar se o usuario digitou mesmo valor que o resultado da funcao

numero_usuario = int(input("Digite um numero de 1 até 5: "))
numero_aleatoria = random.randint(1, 5)
print(numero_aleatoria, numero_usuario)

if numero_aleatoria == numero_usuario:
        print("Você acertou!")
else:
        print("tente novamente!")

#APIs(aplication programan interface)
#por padrao as APIS vem em dois padroes XML e  Jason
#teremos que ter campos com nome de meio termo EX: em um sistema tem o campo nome_aluno e no outro sistema esta nome_pessoa, teremos que definir no XML 
#com um nome meio termo podendo ser só nome no XML informando que os campos sao iguais 
#|Em Jason a forma de escrever e parecida com uma dicionario em python 
# Jason EX: 
#[{
# "time": "Corinthians"
#}]







