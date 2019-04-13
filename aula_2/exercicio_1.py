# Missão 1:
# Criar uma função 'cadastrar_usuario' que retorne um dicionário de usuário.
# O dicionário deve conter a propriedades:
# - nome
# - email
# - idade
# e os valores devem ser digitados pelo usuário do através do terminal (input)
import datetime

def cadastrar_usuario():
	novo_usuario = {
		'data_cadastro': datetime.datetime.now(),
		'nome': input('Digite seu nome: '),
		'email': input('Digite seu email: '),
		'idade': input('Digite sua idade:'),
	}
	return novo_usuario

novo_usuario = cadastrar_usuario()
print(novo_usuario)

d = novo_usuario['data_cadastro']
print(d.strftime('%B %d, %Y'))




