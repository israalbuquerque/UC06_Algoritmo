#APIs(aplication programan interface)
#por padrao as APIS vem em dois padroes XML e  Jason
#teremos que ter campos com nome de meio termo EX: em um sistema tem o campo nome_aluno e no outro sistema esta nome_pessoa, teremos que definir no XML 
#com um nome meio termo podendo ser só nome no XML informando que os campos sao iguais 
#|Em Jason a forma de escrever e parecida com uma dicionario em python 
# Jason EX: 
#[{
# "time": "Corinthians"
#}]

#no gov.br temos varias apis governamentais
#para comsumir uma api, podemos usar uma linguagem de programacao para comsumi-la
#podemos pesquisar no google "lista de APIs", e podemos consumilas
#https://publicapis.io/ podemos usar esta URL para verificar APIs a serem consumidas
#gereneration brasil oportunidade de fazer curso, uma outra opcao e a 42Sp

#retronos em ti 200 = ok, 400 = erro do lado do cliente, 500 = erro no servidor so lado da empresa

#para requests  e necessario realizar a instalacao no terminal usando os comandos "pip install requests", sera feita a instalacao
import requests

url =  "https://rickandmortyapi.com/api/character"

#resquests estamos usando o biblioteca e get para pegar um terminado dados como no exemplo minha url
resposta =  requests.get(url)

#vai nos retornar 200 que significa OK
print(resposta)

#pedimos para retornar as informacoes que estao no formato status code em json da variavel resposta que guarda busca nossa ULR
json = resposta.json()
'''print(json)'''

#criamos uma variavel que recebe os dados em json
personagem = json["results"]

'''print(personagem)'''

#laco de repeticao para consultar os nomes dos personagens
for nome_personagem in personagem:
    print(nome_personagem["name"])

#retornar mais informacoes alem do nome
'''
for mais_info in personagem:
    print("Nome: ", mais_info["name"])
    print("Status: ", mais_info["status"])
    print("Especies: ", mais_info["species"])
    print("---------------------------------")
'''

#pedir ao usuario para digitar um ID e retornar da API personagem referente a esse id
id = int(input("Digite um número inteiro: "))

#colocamos um f para poder trabalhar dentro de uma string a passagem de uma variavel, podendo adicionar um novo conteudo na variavel

link_api =  f"https://rickandmortyapi.com/api/character/{id}"

resposta = requests.get(link_api)



novo_json = resposta.json()

print("Nome: ", novo_json["name"])
print("Status: ", novo_json["status"])
print("Especies: ", novo_json["species"])
print("---------------------------------")


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

site =  "https://rickandmortyapi.com/api/character"
resultado =  requests.get(url)






