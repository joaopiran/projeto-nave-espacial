combustivel = 110
tripulantes = []

##definir funçoes

def viajar():
    ##codigo gastar combustivel
    global combustivel ## avisa a funçao que vamos modificar a variavel externa
    if (combustivel >=30):
        combustivel = combustivel - 30
        print("a nave viajou")
    else:
        print("Você está sem combustivel")

def abastecer():
    global combustivel
    combustivel = 110
    print("Você está com tanque cheio⛽")

def status_nave():
    ##mostra a quantidade de tripulantes e combustivel
    print("-------status da nave------\n")
    print(f"temos {combustivel} de combustivel")
    print(f"Os tripulantes sao: {tripulantes}")
    print("\n---------------------------------")

def registrartripulante():
    novotripulante = input("qual o nome dos tripulantes?:")
    tripulantes.append(novotripulante)
    print("Tripulante inserido com sucesso")

##Cria um menu

print("Bem vindo ao menu interativo da nave. Por favor selecione uma opção:")
while True: 
    print("\n1- mostra status da nave | 2- Viajar | 3- Abastecer | 4- Novo tripulante | 5- sair")
    opcao = input("escolha:")
    if(opcao =="1"):
        status_nave()
    elif(opcao =="2"):
        viajar()
    elif(opcao =="3"):
       abastecer()
    elif(opcao =="4"):
       registrartripulante()
    elif(opcao =="5"):
       print("viagem encerrada")
       break








# status_nave()
# registrartripulante()
# status_nave()


# status_nave()
# viajar()
# viajar()
# viajar()
# status_nave()
# viajar()
# abastecer()
# viajar()
