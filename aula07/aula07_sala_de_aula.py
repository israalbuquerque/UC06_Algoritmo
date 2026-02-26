
"""
while True:
    escolha = ""
    nome_valor =  input("Digite seu nome: ")
    idade_valor =  input("Digite sua idade: ")
    cidade_valor =  input("Digite sua cidade: ")

    


    cadastro = {
        "nome": "",
        "idade": "",
        "cidade": "",
    }

    cadastro["nome"] = nome_valor
    cadastro["idade"] = idade_valor
    cadastro["cidade"] = cidade_valor

    for chave, valor in cadastro.items():
        print(chave, ":", valor)

    
    escolha = input("Deseja repetir esta ação [S/N]: ").lower()
    if escolha != "s":
        print("Ação cancelada!")
        break
        
"""

while True:
    nome_do_aluno = input("Digite o nome do aluno: ")
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    nota4 = int(input("Digite a quarta nota: "))
    nota5 = int(input("Digite a quinta nota: "))

    dados_aluno = {
        "nome_aluno": "",
        "primeira_nota": "",
        "segunda_nota": "",
        "terceira_nota": "",
        "quarta_nota": "",
        "quinta": "",

    }

    dados_aluno["nome_aluno"] = nome_do_aluno
    dados_aluno["primeira_nota"] = nota1
    dados_aluno["segunda_nota"] = nota2
    dados_aluno["terceira_nota"] = nota3
    dados_aluno["quarta_nota"] = nota4
    dados_aluno["quinta_nota"] = nota5

    media = (nota1 + nota2 + nota3 + nota4 + nota5) /5

    for chave, valor in dados_aluno.items():
        print(chave, ":" , valor)

    print("A média da notas do aluno ",nome_do_aluno," é ", media)



    escolha = input("Deseja realizar novamnete a açaõ [S/N]: ")
    if escolha != "s":
        print("Ação cancelada!")

