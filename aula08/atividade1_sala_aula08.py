'''
Crie uma lista vazia cahamada compra peca ao usuario para digitar 3 itens adicione cada item na lista mostretodos os itens da lista ao final
'''

#Laco de repeticao
#metodo para manupular lista
#lista

lista_compra = []

for i in range (3):
    item = int(input ("Digite um item: "))
    lista_compra.append(item)
    
print(sum(lista_compra) / len(lista_compra))
    

for valor in lista_compra:
    print("-",valor)

