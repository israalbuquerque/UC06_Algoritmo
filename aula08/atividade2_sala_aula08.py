nomes = ["Israel","Vinicius","de","Albuquerque"]

for valor in nomes:
    print("-",valor)

remocao = input("Remova um nome: ")

if remocao in nomes:
    nomes.remove(remocao)
    print("O nome escolhido foi removido")
    print("agora a lista é: ", nomes)
else:
    print("Nome não encontrado!")