#lista_populada = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#lista_vazia = []

#Para inserir elementos em uma lista 
#lista_vazia.append(1)
#lista_vazia.append(2)
#lista_vazia.append(3)
#lista_vazia.append(4)
#lista_vazia.append(5)
#lista_vazia.append(6)
#lista_vazia.append(7)
#lista_vazia.append(8)
#lista_vazia.append(9)
#lista_vazia.append(10)

#print(lista_populada)
#print(lista_vazia)

#Imprimir APENAS O QUINTO ELEMENTO da lista
#print(lista_vazia[4])


#for n in lista_vazia:
#	print('Imprimindo numero' + str(n))



#exercicio: 
#escreva um programa que cadastre 10 usuarios
# e salve em uma lista.
#Após cadastrar, exiba os dados dos usuarios cadastrados

lista = []

for n in range(10):
	usuario = {
			'nome': input ('Digite seu nome:'),
		'idade': input ('Digite sua idade:'),
		'email': input ('Digite seu email:')
	}
	lista.append(usuario)


for n in lista:
	print('Usuario Cadastrado:{}'.format(n['nome']))


	