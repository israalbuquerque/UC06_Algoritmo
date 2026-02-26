#dicionario python
#antes dos ":" sempre chave e depois valor
aluno = {
    "nome_aluno": "Pedro",
    "idade": 19,
    "nota": 8,
    "curso": "TECNICO EM INFORMATICA PARA INTERNET",
    #aqui foi colocado um array
    "array": [1, True, "texto"],
    #aqui foi colocado um dicionario, podemos observar que este dicionario endereco esta dentro do dicionario aluno(como um ani)
    "endereco" :{
        "rua": "clementina",
        "numero": 10,
        "estado": "SP"
    }

}

#para acessar um valor de um dicionario usamos desta forma, nome dicionario "aluno" -> comchetes  e com o nome da chave["nome_aluno"]
print(aluno["nome_aluno"])
#aqui vai retornar todos os dados dentro do array
print(aluno["array"])
#para printar somente um dado dentro do array alem de colocar o dicionario principal e sua chave voce deve colocar em [] sua posicao, como [1]
print(aluno["array"][1])
#para acessar um valor dentro do dicionario aninhado basta colocar o dicinario principal -> depois o dicionario que voce quer dentro 
#do conchetes ["endereco"] -> para buscar um valor dentro deste dicionario aninhado colocamos por terceiro o conchetes o noma da chave ["estado"]
print(aluno["endereco"]["estado"])


#para alterar o valor de uma chave podemos descrever o dicionario -> dentro dos conchetes a chave ["nome_aluno"] -> e com o sinal de = colocar 
#o novo dado atualizado
aluno["nome_aluno"] = "Israel"
print(aluno["nome_aluno"])

#altera dados dentro de array, que esta dentro dum dicionario
#para alterar um dado do array, colocamos o dicionario principal -> a chave com os conchetes ["array"] -> a posicao que sera alterada com o uso 
#dos conchetes [2] posicao dois -> colocar = com um valor para que seja auterado 
aluno["array"][2] = "voce"
print([aluno["array"][2]]) 

#alterar dados  do dicionario endereco que esta dentro do dicionario aluno
#para alterar um valor de uma chave de um dicionario que esta aninhado colocamos o dicionario principal -> conchetes com o dicionario escolhido 
#que esta aninhado ["endereco"] -> agora colocamos a chave dentro dos conchetes ["cidade"] -> com o = difinimos um novo valor para a nossa chave
# que e cidade
aluno["endereco"]["cidade"] = "São Paulo"
print(aluno["endereco"]["cidade"])


#aqui foi colocado uma chave e um valor que nao existe, quando isso acontece sera adicionado dentro do dicionario essa chave e seu conteudo por 
# nao existirem chubados no dicionario e so serem definidos depois  
aluno["periodo"] = "Noturno"
print(aluno)

# para apagar podemos usar o del na frente do dicionario aluno e colocar sua chave nos conchetes que vao ser  chave que sera excluida[idade""]
#colocando uma "," apos o primeiro delete podemo repetir colocando o dicionario aluno e sua chave ["endereco"] 
del aluno["idade"], aluno["endereco"]
#print(aluno)

#para percorrer as chaves presentes em uma dicionario basta usar o for -> palavra "chave" palavra "in" no dicionario desejado que é alunos
for chave in aluno:
    print(chave)
#aqui estamos percorrendo somante os valores 
for valor in aluno.values():
    print(valor)

#percorrer um dicionario com chave e valor
for chave, valor in aluno.items():
    print(chave, ":", valor)




#---------------------------------------------------------------------------------------------------
