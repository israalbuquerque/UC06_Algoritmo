#Criar um menu para selecao
 
#1 - consutar por id
#2 - consultar por ID
#3 - lista de personagens
 
#se for opcao 1: pedir ao usuario para digitar um ID(numero intetero) e retornar de dentro da da API personagem referente a esse id
#Se selecionar a opcao 2: pedir ao usuario para digitar um nome e retornar de dentro da API o personagem refente ao nome digitado
#OBS:para percorrer o json e retornar o nome digitado
#for personagem in dados ["results"]:
    #print(personagem["name"])
#Se selecionar a opcao 3: retornar todos os personagens, lista das informacoes que deverao ser retornados
'''
"id": 1,
      "name":
      "status":
      "species":
      "type": "",
      "gender":
      "origin": {
        "name": "Earth",
       
      },
      "location": {
        "name": "Earth",
       
      },
      "image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
'''
 
import requests
'''
def menu():
    print("=================================================")
    print("1 - Consultar por ID")
    print("2 - Consultar pelo nome")
    print("3 - Lista de personagens completa")
    print("=================================================")
 
    escolha = input("Digite uma opção: ")
 
 
    if escolha.isdigit():
   
        escolha = int(escolha)
        return escolha
        

    else:
        print("Número digitado incorreto!")
    escolhas()
'''
def escolhas(escolha):
    # funcao_menu = menu()
    if escolha == 1:
        escolha_id = input("Digite um id para saber qual o personagem: ")

        if escolha_id.isdigit():
            escolha_id = int(escolha_id)
            site =  f"https://rickandmortyapi.com/api/character/{escolha_id}"
            resultado =  requests.get(site)
            json_id = resultado.json()
            # id = json["results"]
            # for id_personagem in id:
            print(json_id["name"])
        else:
            print("Número digitado incorreto!")

    elif escolha == 2:
        escolha_name = input("Digite o nome do personagem: ")
        site =  f"https://rickandmortyapi.com/api/character/?name={escolha_name}"
        resultado =  requests.get(site)
        json_id = resultado.json()
        id = json_id["results"]
        for personagem in id:
            print(personagem["name"])

    elif escolha == 3:
        site =  "https://rickandmortyapi.com/api/character"
        resultado = requests.get(site)
        json_tudo = resultado.json()
        tudo = json_tudo["results"]
        for personagem in tudo:
            print(personagem["name"]) 
            print(personagem["status"])
            print(personagem["species"])
            print(personagem["type"])
            print(personagem["gender"])
            print(personagem["origin"]["name"])
            print(personagem["location"]["name"])
            print(personagem["image"])
            print("====================================")
            # print(personagem["gender"])

        # for personagem in tudo:
        #      print(personagem["results"])
def menu():
    print("=================================================")
    print("1 - Consultar por ID")
    print("2 - Consultar pelo nome")
    print("3 - Lista de personagens completa")
    print("=================================================")

    escolha = input("Digite uma opção: ")


    if escolha.isdigit():

        escolha = int(escolha)
        return escolha
        
    else:
        print("Número digitado incorreto!")
    escolhas(escolha)
    



while True:
    opcao = menu()
    escolhas(opcao)
    escolher_novamente = input("Deseja voltar ao menu [S/N]: ").lower()


    if escolher_novamente != "s":
        
        print("Ação cancelada!")
        break

        

        