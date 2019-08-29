from datetime import datetime
from random import choice
import pickle
import os

elementos = ("1","2","3","4","5","6","7","8","9")
listaDeIds = []



refeicoes = {}
notas = {}

def dataHoje():
	data = str(datetime.now())
	dia = (data[8:10])
	mes = (data[5:7])
	ano = (data[0:4])
	data = (dia + "/" + mes + "/" + ano)
	return data
	
def menuAlt():
	return print("""
[1] - Nome
[2] - Preço
[3] - Receita
""")

def id():
	n1 = choice(elementos)
	n2 = choice(elementos)
	n3 = choice(elementos)
	n4 = choice(elementos)
	n5 = choice(elementos)
	n6 = choice(elementos)
	id = "REF" + n1+n2+n3+n4+n5+n6
	if id not in listaDeIds:
		listaDeIds.append(id)
		return id

def validaPreco(x):
	cont = 0
	for i in x:
		if i == ".":
			cont += 1
	if cont > 1:
		return False
	else:
		x = x.replace(".","")
		if x.isnumeric():
			return True
		else:
			return False

def mainMenu():
	print("[1] - Cadastrar nova refeição")
	print("[2] - Checar produtos")
	print("[3] - Alterar dados de uma das refeições")
	print("[4] - Buscar refeição")
	print("[5] - Deletar")
	print()
	print("[6] - Pedido")
	print("[7] - Histórico de pedidos")
	print("[8] - Calculadora")
	print("[F] - Fechar")

def cadastrarRefeicao():
	os.system("clear")
	print("CADASTRAR REFEIÇÃO")
	print()
	listaDados = []
	name = input("Digite o nome do produto: ")
	price = input("Digite o preço do produto: ")
	while (validaPreco(price) == False):
		price = input("Preço inválido, digite novamente: ")
	formatPrice = ("R$" + price)
	recipe = input("Receita: ")
	aux = id()
	listaDados.append(name)
	listaDados.append(formatPrice)
	listaDados.append(recipe)
	listaDados.append(aux)
	refeicoes[aux] = listaDados
	
def checarRefeicoes():
	os.system("clear")
	print("CHECAR REFEIÇÕES")
	print()
	for i in refeicoes:
		print("Nome: ",refeicoes[i][0])
		print("Preço: ",refeicoes[i][1])
		print("Receita: ",refeicoes[i][2])
		print("ID: ", refeicoes[i][3])
		print()

def buscarRefeicao():
	os.system("clear")
	print("BUSCAR REFEIÇÃO")
	print()
	nome = input("Digite o nome da refeição: ")
	for i in refeicoes:
		if (refeicoes[i][0].upper()).startswith(nome.upper()):
			print("Nome: ",refeicoes[i][0])
			print("Preço: ",refeicoes[i][1])
			print("Receita: ",refeicoes[i][2])
			print("ID: ",refeicoes[i][3])
			print()

def alterarDados():
	os.system("clear")
	print("ALTERAR DADOS DE UMA REFEIÇÃO")
	print()
	iden = input("Digite o ID da refeição: ")
	if iden not in refeicoes:
		print("ID não encontrado")
	else:
		for i in refeicoes:
			if (iden == refeicoes[i][3]):
				print("Nome:",refeicoes[i][0])
				print("ID: ",refeicoes[i][3])
				menuAlt()
				perg = input("O que deseja mudar? ")
				if perg == "1":
					newName = input("Digite o novo nome da receita: ")
					refeicoes[i][0] = newName
				elif perg == "2":
					newPrice = input("Digite o novo preço: ")
					while (validaPreco(newPrice) == False):
						newPrice = input("Preço inválido, digite novamente: ")
					refeicoes[i][1] = newPrice
				elif perg == "3":
					newRecipe = input("Digite a nova receita: ")
				else:
					print("Opção inválida")


def deletar():
	os.system("clear")
	print("DELETAR PRODUTO")
	print()
	iden = input("Digite o ID da refeição: ")
	if iden not in refeicoes:
		print("ID não foi encontrado")
	else:
		for i in refeicoes:
			if (iden == refeicoes[i][3]):
				print("Nome: ", refeicoes[i][0])
				print("ID: ",refeicoes[i][3])
		perg = input("Deseja mesmo deletar essa refeição? [1] - Sim/[2] - Não ")
		if perg == "1":
			del refeicoes[iden]
			print("Refeição removida")
		else:
			print("Processo encerrado")



def pedido():
	os.system("clear")
	pedido = []
	cont = 0
	conta = 0
	nome = input("Nome do cliente: ")
	perg = input("O que deseja pedir? ")
	while perg.upper() != "N":
		for i in refeicoes:
			if (perg.upper() == refeicoes[i][0].upper()):
				pedido.append(refeicoes[i][0])
				cont += 1
				auxPrice = ((refeicoes[i][1])[2:])
				conta += float(auxPrice)
		perg = input("Mais alguma coisa? ")
	print()
	print("Seu pedido: ")
	for i in range(cont):
		print(pedido[i])
	print("Total a pagar: ",conta)
	
	auxConta = str(conta)
	auxPedido = str(pedido)
	nota = ("O cliente " + nome + " frequentou o restaurante na data " + dataHoje() + ". Seu pedido foi: " + auxPedido + ",pagando um total de R$" + auxConta)
	notas[datetime.now()] = nota
	

def historico():
	print("HISTÓRICO DE VENDAS")
	print()
	for i in notas:
		print(notas[i])

def calculadora():
	return print("Calculadora em breve")


#####PROGRAMA#####

print("BEM-VINDO AO PROGRAMA PARA RESTAURANTES")
print()
print("Escolha uma das opções a seguir:")
mainMenu()
print()
opcao = input("")
while (opcao.upper() != "F"):
	if opcao == "1":
		cadastrarRefeicao()
		print()
	
	elif opcao == "2":
		checarRefeicoes()
		print()
	
	elif opcao == "3":
		alterarDados()
		print()
	
	elif opcao == "4":
		buscarRefeicao()
		print()
	
	elif opcao == "5":
		deletar()
		print()
	
	elif opcao == "6":
		pedido()
		print()
	
	elif opcao == "7":
		historico()
		print()
	
	elif opcao == "8":
		calculadora()
		print()
		
	else:
		opcao = input("Opção inválida, digite novamente: ")
		
	mainMenu()
	print()
	opcao = input("O que deseja fazer agora? ")

print("PROGRAMA ENCERRADO.")
