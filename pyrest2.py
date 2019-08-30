####BIBLIOTECAS, DICIONÁRIOS E COISAS TÉCNICAS####

from tkinter import *
from datetime import datetime
from random import choice
import pickle

elementos = ("0", "1","2","3","4","5","6","7","8","9")

refeicoes = {}
notas = {}

####GERAÇÃO DE DATAS, ID'S E COISAS SEMELHANTES####

def dataHoje():
	data = str(datetime.now())
	dia = (data[8:10])
	mes = (data[5:7])
	ano = (data[0:4])
	data = (dia + "/" + mes + "/" + ano)
	return data
	
def id(x):
	substr = (x[0:3])
	substr = substr.upper()
	n1 = choice(elementos)
	n2 = choice(elementos)
	id = "REF" + substr + n1 + n2
	if id in refeicoes:
		id += "1"
	else:
		id = id
	return id


####FUNÇÕES TÉCNICAS####
def fec():
	janelaCad.quit()


####FUNCÕES DO PROGRAMA PRINCIPAL####

#CADASTRO DE REFEIÇÃO#
def janelaCad():
	def click_button():
		confirm["text"] = "Refeição cadastrada."
		
		listaDados = []
		name = str(entNom.get())
		price = ("R$" + str(entPre.get()))
		time = str(entTem.get())
		aux = id(name)
		listaDados.append(name)
		listaDados.append(price)
		listaDados.append(time)
		listaDados.append(aux)
		refeicoes[aux] = listaDados
		
		btfec = Button(janelaCad, width=10, text="Sair", command=fec)
		btfec.place(x=85,y=500)
		
	
	janelaCad = Tk()
	janelaCad.geometry("500x500")
	janelaCad.title("Cadastrar refeição")
	#Definindo labels:
	nom = Label(janelaCad, text="Nome: ")
	pre = Label(janelaCad, text="Preço: ")
	tem = Label(janelaCad, text="Tempo de preparo: ")
	confirm = Label(janelaCad, text="")
	
	#Definindo entradas:
	entNom = Entry(janelaCad)
	entPre = Entry(janelaCad)
	entTem = Entry(janelaCad)
	
	#Definindo button:
	bt = Button(janelaCad, width=20, text="CADASTRAR REFEIÇÃO",command=click_button)
	
	#Definindo posições:
	nom.place(x=50,y=50)
	pre.place(x=50,y=100)
	tem.place(x=50,y=150)
	entNom.place(x=150,y=50)
	entPre.place(x=150,y=100)
	entTem.place(x=290,y=150)
	bt.place(x=100,y=250)
	confirm.place(x=85,y=450)
	
	arqRef = open("ref.dat","wb")
	pickle.dump(refeicoes, arqRef)
	arqRef.close()
	
	janelaCad.mainloop()

#CHECAR REFEIÇÕES#

def janelaRe():
	janelaRe = Tk()
	janelaRe.geometry("600x600")
	janelaRe.title("Checar refeições")
	
	#Auxiliares de posicionamento
	auxY = 100
	auxXNom = 0
	auxXPre = 200
	auxXTem = 400
	auxXId = 600
	
	#Indicadores do topo da tabela, suas cores e posições
	indNome = Label(janelaRe, text="Nome                        ")
	indPreco = Label(janelaRe, text="Preço                        ")
	indTempo = Label(janelaRe, text="TdP                          ")
	indId = Label(janelaRe, text="ID                      ")
	
	indNome["bg"] = "blue"
	indPreco["bg"] = "blue"
	indTempo["bg"] = "blue"
	indId["bg"] = "blue"
	
	indNome.place(x=auxXNom, y=50)
	indPreco.place(x=auxXPre, y=50)
	indTempo.place(x=auxXTem, y=50)
	indId.place(x=auxXId, y=50)
	
	#Percorrimento do dicionário
	for i in refeicoes:
		nomRef = Label(janelaRe, text=refeicoes[i][0])
		preRef = Label(janelaRe, text=refeicoes[i][1])
		temRef = Label(janelaRe, text=refeicoes[i][2])
		idRef = Label(janelaRe, text=refeicoes[i][3])
		
		nomRef.place(x = auxXNom, y = auxY)
		preRef.place(x = auxXPre, y = auxY)
		temRef.place(x = auxXTem, y = auxY)
		idRef.place(x = auxXId, y = auxY)
		
		auxY += 50
	
	janelaRe.mainloop()

#BUSCAR REFEIÇÕES#

def buscarRe():
	def click_button():
		#Auxiliares de posicionamento
		auxY = 200
		auxXNom = 0
		auxXPre = 200
		auxXTem = 400
		auxXId = 600
		
		#Variável que recebe o resultado da busca:		
		pesquisa = str(busca.get())
		
		#Indicadores do topo da tabela, suas cores e posições:		
		indNome = Label(buscarRe, text="Nome                        ")
		indPreco = Label(buscarRe, text="Preço                        ")
		indTempo = Label(buscarRe, text="TdP                          ")
		indId = Label(buscarRe, text="ID                      ")
					
		indNome["bg"] = "blue"
		indPreco["bg"] = "blue"
		indTempo["bg"] = "blue"
		indId["bg"] = "blue"
					
		indNome.place(x=auxXNom, y=150)
		indPreco.place(x=auxXPre, y=150)
		indTempo.place(x=auxXTem, y=150)
		indId.place(x=auxXId, y=150)
		
		#Percorrimento do dicionário com a busca aplicada:
		for i in refeicoes:
			if (pesquisa.upper()) in (refeicoes[i][0].upper()):
				nomRef = Label(buscarRe, text=refeicoes[i][0])
				preRef = Label(buscarRe, text=refeicoes[i][1])
				temRef = Label(buscarRe, text=refeicoes[i][2])
				idRef = Label(buscarRe, text=refeicoes[i][3])
						
				nomRef.place(x = auxXNom, y = auxY)
				preRef.place(x = auxXPre, y = auxY)
				temRef.place(x = auxXTem, y = auxY)
				idRef.place(x = auxXId, y = auxY)
						
				auxY += 50
	
	buscarRe = Tk()
	buscarRe.geometry("700x700")
	buscarRe.title("Buscar refeição")
		
	instr = Label(buscarRe, text="Digite o nome da refeição que está procurando: ")
	instr.place(x=115, y=30)
		
		
	busca = Entry(buscarRe)
	busca.place(x=250, y=70)
		
		
	bt = Button(buscarRe, width=20, text="PESQUISAR", command = click_button)
	bt.place(x= 220, y=120)
		
	buscarRe.mainloop()

#DELETAR#
def deletar():
	#Botão que confirma a instrução:
	def bt2_click():
		aux = str(iden.get())
		del refeicoes[aux]
		aviso = Label(deletar, text="Refeição deletada com sucesso.")
		aviso.place(x=400, y=575)
	
	#Botão que nega a instrução:
	def bt3_click():
		deletar.quit()
	
	#Comando do botão de pesquisa:
	def bt1_click():
		aux = str(iden.get())
		if aux not in refeicoes:
			aviso = Label(deletar, text="Esse ID não foi encontrado.")
			aviso.place(x=250, y=275)
		else:
			aviso = Label(deletar, text="A seguinte refeição foi encontrada: ")
			aviso.place(x=250, y=325)
			aviso2 = Label(deletar, text=refeicoes[aux][0])
			aviso2.place(x=250, y=375)
			aviso3 = Label(deletar, text="Deseja mesmo deletá-la?")
			aviso3.place(x=250, y=425)
				
			bt2 = Button(deletar, width = 10, text="SIM", command = bt2_click)
			bt2.place(x=200, y=475)
				
			bt3 = Button(deletar, width = 10, text="NÃO", command = bt3_click)
			bt3.place(x=400, y=475)
		
	deletar = Tk()
	deletar.geometry("700x700")
	deletar.title("Deletar")
		
	instr = Label(deletar, text="Digite o ID da refeição que deseja deletar: ")
	instr.place(x=150, y=75)
		
	iden = Entry(deletar)
	iden.place(x=250, y=125)
		
	bt1 = Button(deletar, width=20, text="PESQUISAR", command=bt1_click)
	bt1.place(x=220, y=175)
	
	arqRef = open("ref.dat","wb")
	pickle.dump(refeicoes, arqRef)
	arqRef.close()
	
	deletar.mainloop()

#CALCULADORA#
def calculadora():
	#Definições das 4 operações:
	def soma():
		valor1 = float(vlr1.get())
		valor2 = float(vlr2.get())
		resultado = valor1 + valor2
		lbR["bg"] = "white"
		lbR["text"] = resultado
	
	def sub():
		valor1 = float(vlr1.get())
		valor2 = float(vlr2.get())
		resultado = valor1 - valor2
		lbR["bg"] = "white"
		lbR["text"] = resultado
	
	def mult():
		valor1 = float(vlr1.get())
		valor2 = float(vlr2.get())
		resultado = valor1 * valor2
		lbR["bg"] = "white"
		lbR["text"] = resultado
	
	def div():
		valor1 = float(vlr1.get())
		valor2 = float(vlr2.get())
		if valor2 == 0:
			lbR["text"] = "Você não pode dividir por 0"
			lbR["foreground"] = "red"
		else:
			resultado = valor1 / valor2
			lbR["bg"] = "white"
			lbR["text"] = resultado
	
	calculadora = Tk()
	calculadora.geometry("300x400")
	calculadora.title("Calculadora")
	
	#Instrução dos valores:
	inst1 = Label(calculadora, text="Valor 1:")
	inst2 = Label(calculadora, text="Valor 2:")
	
	#Criação dos botões:
	btSom = Button(calculadora, width=5, text="+", command = soma)
	btSub = Button(calculadora, width=5, text="-", command = sub)
	btMult = Button(calculadora, width=5, text="×", command = mult)
	btDiv = Button(calculadora, width=5, text="÷", command = div)
	
	#Entrada de dados:
	vlr1 = Entry(calculadora)
	vlr2 = Entry(calculadora)
	
	#Exibição:
	lbRIns = Label(calculadora, text="Resultado: ")
	lbR = Label(calculadora, text="")
	
	#Posições:
	inst1.place(x=5, y=10)
	inst2.place(x=5, y=60)
	
	vlr1.place(x=105, y=10)
	vlr2.place(x=105, y=60)
	
	btSom.place(x=15, y=110)
	btSub.place(x=155, y=110)
	btMult.place(x=15, y=170)
	btDiv.place(x=155, y=170)
	
	lbRIns.place(x=50, y=260)
	lbR.place(x=85, y=310)
	
	
	calculadora.mainloop()

#PEDIDO#
def pedido():
	def button_click():
		aviso = Tk()
		aviso.geometry("500x500")
		
		aten = Label(aviso, text="Opção fazer pedido em breve")
		aten.place(x=100, y=100)
		
		aviso.mainloop()
	
	pedido = Tk()
	pedido.geometry("600x600")
	
	auxY = 100
	
	for i in refeicoes:
		sele = Checkbutton(pedido, text=refeicoes[i][0])
		sele.place(x=50, y = auxY)
		auxY += 50
	
	bt = Button(pedido, text="FAZER PEDIDO", command = button_click)
	bt.place(x=75, y=auxY)
	
	pedido.mainloop()

####PROGRAMA####

try:
	arqRef = open("ref.dat","rb")
	refeicoes = pickle.load(arqRef)
	arqRef.close()
except IOError:
	print()

janelaPrin = Tk()
janelaPrin.geometry("800x800")
janelaPrin["bg"] = "white"
janelaPrin.title("Sistema do Restaurante Sertão Sabores")

#icone = PhotoImage#(file="/storage/emulated/0/Download/Calc2.png")

#imagem = PhotoImage#(file="/storage/emulated/0/Download/Imagem.png")
#ima = Label(janelaPrin, image=imagem)
#ima.place(x=100, y=100)

butCad = Button(janelaPrin, width = 15, text="CADASTRAR REFEIÇÃO", command = janelaCad)
butCad.place(x=50, y=5)

butChe = Button(janelaPrin, width=15, text="CHECAR REFEIÇÕES", command = janelaRe)
butChe.place(x=320, y=5)

butBus = Button(janelaPrin, width=15, text="BUSCAR REFEIÇÃO", command = buscarRe)
butBus.place(x=590, y=5)

butDel = Button(janelaPrin, width=15, text="DELETAR REFEIÇÃO", command = deletar)
butDel.place(x=500, y=100)

butPed = Button(janelaPrin, width=15, text="FAZER PEDIDO", command = pedido)
butPed.place(x=500, y=180)

#butCal = Button(janelaPrin, image = icone, command = #calculadora)
#butCal.place(x=500, y=260)

credits = Label(janelaPrin, text="Desenvolvido por @danrleydaniel")
credits.place(x=40, y=400)
credits["bg"] = "white"


janelaPrin.mainloop() 

arqRef = open("ref.dat","wb")
pickle.dump(refeicoes, arqRef)
arqRef.close()
