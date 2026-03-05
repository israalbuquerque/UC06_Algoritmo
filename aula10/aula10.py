#Abrir arquivos
#Usamos o open para abrir um arquivo e dentro do () colocamos nome do arquivo e sua extencao, e precisamos dizer o que sera feito 
#apos a , colocamos o modo podendo ser w, a, e r
#w(apaga tudo e escreve novamnete), a(adiciona o conteudo no final), r(ler o arquivo)
#se o arquivo nao existe ele cria o arquivo, caso contrario ele exista nao sera feito nada, ha nao ser que voce 
#EX: open("nome-arquivo.txt", "modo")
#para escrever dentro do arquivo temos que usar o with que garante que apos adicionar o conteudo sera fechado usamos "as arquivos" usamos
# como uma definicao de variavel que sera armazenado o texto que digitamos e apos ser executado vai passar aquele conteudo para o arquivo, e 
#colocamos o arquivo.write("ola") para adicionar o conteudo no arquivo


#EX: with open("dados.txt", "w") as arquivos:
#       arquivo.write("Ola mundo") 

#open("nota.txt", "w")

with open("aula10/nota.txt", "w") as nota_aluno:
    nota_aluno.write("Ola mundo")


#Podemos mudar o mode para r para ler o que esta no arquivo, mudamos o modo para "r" e presisamos ter duas variaveis tanto a arquivo quanto a 
#conteudo .read()


#EX: with open("dados.txt", "r") as arquivos:
#       conteudo = arquivos.read()
#       print(conteudo)

with open("aula10/nota.txt", "r") as leitura_arquivo:
    recebe_texto = leitura_arquivo.read()
    print(recebe_texto)


#podemos adiconar o conteudo sem apagar tudo. somente adicionar, mudamos o modo para "a", e colocamos um \n dentro do "" do texto para 
# quebra a linha

#EX: with open("dados. txt", "a") as arquivos:
        #arquivo.write("\n seja bem vindo")

with open("aula10/nota.txt", "a") as adiciona_novo_texto:
    adiciona_novo_texto.write("\n Aqui tem uma nova linha de texto!")
