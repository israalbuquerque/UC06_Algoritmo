#listas
#Em dicionario usamos {} e para acessar dados usamos o nome da chave
#listas usamos [] e para acessar dados usamos a posicao da lista
#quando quizer definir uma lista no python apos o nome da variavel e o sinal de igual colocamos "[]"

notas = [10, 8, 5, 10, True, 7, "Andre"]

#Metodos e como se fosse ações, cada acao tera uma tarefa
#coloca a palavra "SENAC" por ultimo usando o metodo append, entao na listas notas adicione por ultimo o dado para ultima posicao
notas.append("SENAC")

print(notas)

#Usando .insert teremos que colocar primeiro a posicao que o dado sera adicionado e apos isso o dado que sera adicionado
notas.insert(0, False)

print(notas)

#Usando o metodo .extend mesclamos as listas colocamos os dados da listas nova_lista(a primeira) para a lista notas, entao agora notas tera os
#dados das duas listas

'''
nova_lista = ["Ola mundo", 1980, 24.7]

nova_lista.extend(notas)

print(nova_lista)

'''

#Usando o  .remove remove o que for descrito dentro do (), se tiver dado duplicado so sera removido o primeiro dado o segundo duplicado nao, 
# e case sensitive entao caso o dado informado para ser apagado seja diferente do que estiver na lista vai gerar um erro
notas.remove(10)
notas.remove(True)
notas.remove("SENAC")
notas.remove("Andre")

print(notas)

#Usando o .pop podemos apagar um dado de uma lista usando o indice, porem quando nao colocado a posicao do indice sempre sera removida a ultima
#informacao


nomes_numeros = [390, "Adenilson", 19, "Anna", 40, "Iara", 390, 390, 19]
'''
nomes_numeros.pop(2)
print(nomes_numeros)
'''
#Usamos clear para limpar todos os dados da lista
'''
print(nomes_numeros.clear())
'''
#Usamos o .index usado para informar a posicao que esta o dado informado, como descrito no terminal se encontra na posicao 0, e caso tenha dado 
#repetido ele so mpstrara somente a primeira posicao de dado encontrada

print(nomes_numeros.index(390))
print(nomes_numeros)

#Usamos o .count para retenar quatas vezes se repete o valor descrito em (), como no exemplo (390) 

print(nomes_numeros.count(390))


#Usamos .sort para realizar uma ordenacao, geralmnete so funciona com numeros, colocar em uma ordem crescente

numeros = [34, 45, 25, 44, 100, 51, 69, 10, 1]

numeros.sort()

print(numeros)

#Usamos .sort tambem podemos usar para ordenar pelo alfabeto dados do tipo STR
nome = ["Israel", "vini", "Albuquerque"]

nome.sort()

print(nome)

#Usamos  o .reverse para desordenar por posicoes do ultimo se torna primeiro e primeiro se torna ultimo eo mesmo se repete aos dados do tipo STR

numeros.reverse()
print(numeros)

nome.reverse()
print(nome)



