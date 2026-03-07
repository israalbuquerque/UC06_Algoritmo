#Criar uma funcao que recebe 5 notas de um aluno e calcule e retorne a media de um aluno 
#Crie uma funcao para receber a media do aluno e retorne se ele esta aprovado ou reprovado

lista_notas = []
valor = 1


def recebe_nota():
    
    for valor in range(5):
        nota = int(input("Digite um valor: "))
        lista_notas.append(nota)

    #return lista_notas

    valor = (sum(lista_notas) / len(lista_notas))
    print(valor)
    return valor
    
    

#recebe_nota(1)

def resultado_aluno():
    
    valor = recebe_nota()
    if valor >= 5:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")


resultado_aluno()


#----------------------------------------------------------------------------------------


# lista_nota = []
# lista_nota.clear()
 
 
# def calcular_media():
#     resultado = sum(lista_nota) / len(lista_nota)
#     print(resultado)
#     return resultado
 
# def resultado_numero():
#     calcular_media()
#     resultado = calcular_media()
#     if resultado >= 7:
#         print("Excelente")
#     elif resultado > 5 and resultado < 7:
#         print("Bom")
#     else:
#         print("Precisa melhorar")
 
 
 
# for i in range (5):
   
   
#     nota = input("Digite uma nota: ")
#     if nota.isdigit():
#         nota = int(nota)
#         lista_nota.append(nota)    
   
#     else:
#         print("Valor digitado e invalido!")
#         break
# if len(lista_nota) == 5:
#     print(lista_nota)
#     resultado_numero()
   
# else:
#     ("Numero de dados digitados esta incorreto!")
   
# while True:
#     escolha = input("Deseja realizar a acao novamnete [S/N]: ").lower()
#     if escolha != "s":
#         print("Açao cancelada!")
#         break