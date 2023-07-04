from controlador_cadastros import Controlador_Cadastros

pontos = 0
jogo = Controlador_Cadastros()
while True:
    if jogo.menu():
        pontos += 1
    else:
        if jogo.replay:
            print("Você errou, mas continua podendo jogar!")
        else:
            print ("Você errou. Game over!")
            exit(0)
    print(f"Você tem {pontos} pontos")
 