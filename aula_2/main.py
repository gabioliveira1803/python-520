import json

import aleatorio

def imprimir_bonito(obj):
	print(json.dumps(obj, indent=2))

def gerar_lista_de_usuarios(n):
	lista = []
	for i in range (n):
		u = aleatorio.gerar_usuario_aleatorio()
		lista.append(u)
	return lista

lista_de_usuarios = gerar_lista_de_usuarios(10)

for usuarios in lista_de_usuarios:
	if usuarios['idade'] > 30:
		imprimir_bonito ('usuario: {}'.format(usuarios['nome']))
		imprimir_bonito ('idade: {}'.format(usuarios['idade']))

def gerar_csv(lista):
	TEMPLATE = '{};{};{};'
	cabecalho = TEMPLATE.format('NOME', 'EMAIL', 'IDADE')
	imprimir_bonito(cabecalho)
	for usuarios in lista_de_usuarios:
		usuario_formatado = TEMPLATE.format(
			usuarios['nome'],
			usuarios['e-mail'],
			usuarios['idade']
		)
		imprimir_bonito(usuario_formatado)

def filtrar_usuarios(usuarios):
	usuario_email = usuarios['e-mail'].lower()
	if 'd' in usuario_email.lower() or 'a' in usuario_email.lower():
		return True
	return False

gerar_csv(u for u in lista_de_usuarios if filtrar_usuarios(u))	

