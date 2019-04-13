import random
import string

def gerar_nome_aleatorio():
	return''.join(
		random.choices(
			string.ascii_letters,
			k=random.randint(5, 15)
		)
	)
def gerar_email_aleatorio():
	return gerar_nome_aleatorio() + '@4linux.com'

def gerar_idade_aleatoria():
	return random.randint(24, 55)

def gerar_usuario_aleatorio():
	novo_usuario = {
		'nome': gerar_nome_aleatorio(),
		'e-mail': gerar_email_aleatorio(),
		'idade': gerar_idade_aleatoria()
	}
	return novo_usuario

if __name__ == '__main__':
	print('Rode seus testes sem erro de eles atrapalharem')
	print ('Arquivo aleatorio.py:{}'.format(__name__))
	