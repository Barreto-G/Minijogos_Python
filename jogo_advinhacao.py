import random


def welcome_message():
    print("**********************************************")
    print("****** Bem vindo ao jogo de advinhacao! ******")
    print("**********************************************")
    print("***** Tente advinhar meu numero secreto ******")
    print()


def dificulty_selector():   # Funcao para definir a dificuldade do jogo
    while(True):
        print("Selecione a Dificuldade: ")
        print("(1) Facil (2) Medio (3) Dificil")
        dificuldade = int(input("Dificuldade selecionada: "))

        if(dificuldade == 1):
            return 15
        elif(dificuldade == 2):
            return 10
        elif(dificuldade == 3):
            return 7
        else:
            print("Entrada invalida, escolha uma dificuldade valida!")


def recebe_numero():        # Recebe a entrada do jogador
    valor_digitado_str = input("Digite um numero entre 1 e 100: ")
    return int(valor_digitado_str)


def jogar():
    welcome_message()
    numero_tentativas = dificulty_selector()

    numero_secreto = random.randint(1, 100)
    valor_digitado = 0
    rodada = 1
    pontos = 200
    ganhou = False

    for rodada in range(1, numero_tentativas + 1):
        print("Rodada {} de {}".format(rodada, numero_tentativas))
        valor_digitado = recebe_numero()

        if valor_digitado < 1 or valor_digitado > 100:  # Se o jogador digitar um numero fora do escopo, perde 100 pontos
            print("Valor digitado deve ser um valor entre 1 e 100!")
            pontos = pontos - 100
            continue

        if valor_digitado == numero_secreto:    # Se o jogador acertar o numero secreto, sai do loop na hora
            ganhou = True
            break
        else:       # Se o jogador errou o numero, perde pontos equivalente a diferenca entre o numero digitado e o secreto
            pontos -= abs(numero_secreto - valor_digitado)

            if valor_digitado < numero_secreto:
                print("Voce errou! O numero secreto eh um valor maior ")
            elif valor_digitado > numero_secreto:
                print("Voce errou! O numero secreto eh um valor menor ")

    print()
    if(ganhou):
        print("Parabens, voce acertou o numero secreto!")
        print(f"Sua pontuacao foi de {pontos} pontos!")
    else:
        print("Que pena, suas rodadas acabaram e voce nao acertou o numero secreto")
        print(f"O numero secreto era {numero_secreto}")

    print()
    return


if(__name__ == "__main__"):
    jogar()
