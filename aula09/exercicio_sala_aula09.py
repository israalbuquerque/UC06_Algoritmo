#Criar uma funcao que recebe 5 notas de um aluno e calcule e retorne a media de um aluno 
#Crie uma funcao para receber a media do aluno e retorne se ele esta aprovado ou reprovado

lista_notas = []
valor = 1

def recebe_nota(valor):
    
    for valor in range(5):
        nota = int(input("Digite um valor: "))
        lista_notas.append(nota)

    #return lista_notas

    valor = (sum(lista_notas) / len(lista_notas))
    print(valor)
    return valor
    

#recebe_nota(1)

def resultado_aluno(valor):
    recebe_nota(valor)
    if valor >= 5:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")


resultado_aluno(valor)
