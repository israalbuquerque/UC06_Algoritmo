#O [] foi usado para buscar um caracter, após digitar a posicção como no exemplo a posição 3 nos troxe o "a" pois comecamos a contar do 0
#quando colocado -1 bucar de forma regressiva, usando o -1 vai buscar e nos mostrar o ultimo caracter, podendo ser um ponto final
#EX:
'''
texto1= "senac"

print(texto1[3])
print() 

'''

#usanso o len para uma variavel vai retornar a quantidade de caracteres e espacos presente na variavel
#no exemplo vai retornar 7 caracteres, seis letras no python mais o espaco que esta no final
#EX:

'''
texto = "ola"

print(len(texto))

'''

#upper = tudo maiusculo
#lower = tudo minusculo
#capitalize = primeira letra maiuscula
#title = primeira de cada palavra em maiuscula
#EX:

'''
texto_2 = "ola mundo"
print(texto_2.upper())#tudo maiusculo

print(texto_2.lower())#tudo minusculo

print(texto_2.capitalize())#primeira letra maiuscula

print(texto_2.title())#primeira de cada palavra maiuscula

'''

#substring
#
'''
texto = "Python"

print(texto[0:2]) # aqui vai retornar da primeira a segunda string nas posicoes 0 e 1, ela para e ignora a posicao 2
print(texto[2:]) # aqui vai retornar a posicoes apos as posicoes 0 1 e mostra as outras posicoes que estao as strings 
print(texto[:2])# aqui vai retornar somnete as dua primeiras 2 posicoes de strigs, a outras nao mostrarao

'''
'''
#replace
#usado para mudar o coteudo de uma variavel usando o .replace()
texto = "Eu gosto de java"

novo_texto = texto.replace("de java", "do python")#o primeiro o que sera alterado e o segundo aspas a sera a atualizacao do que ja tinha

print(novo_texto)
'''

'''
#espaco em branco

texto = "       Ola    mundo  "

print(texto.strip()) # remove  espacos direita e esquerda 
print(texto.lstrip())# remove eapacos a esquerda
print(texto.rsplit())# remove espacos a direita

'''

'''
#bucar caraccter, texto dentro de uma variavel
#case sensitive(sensivel a letras maiusculas e minusculas)
texto = "python incrivel"

print("python" in texto) #  busca determinada palalavra letra ou texto qur foi descrito e uma dtermiada variavel, ser for verdadeiro retorna true caso contrario false

'''

'''
#aqui vai mostrar onde se inicia a palavra pesquisada, como no exemplo a palavra 'sabia', sendo ele tambem case sensitive
texto = "voce e lindo e maravilhoso, voce sabia."
print(texto.find("sabia"))

'''

'''
#aqui podemos contar quantas palavras estao naquele texto, como no exemplo a palavra banana, tbm podendo ser uma palavra como "a"
texto = "banana, maca, banana e melancia "

print(texto.count("banana"))

'''

'''
#aqui verificamos em startswith para saber de comecamos com aquelas letras descritas dentro do "py", 
#o mesmo foi feito em endswitch para saber se termina com aquelas letras dentro das "on"
texto = "python"

print(texto.startswith("py"))
print(texto.endswith("on"))

'''