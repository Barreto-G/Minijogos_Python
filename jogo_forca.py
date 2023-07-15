import random


def def_palavra_secreta():  # Abre o arquivo palavras na mesma pasta do arquivo python
    arquivo_palavras = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo_palavras:  # Passa todas as palavras do arquivo para uma lista
        palavras.append(linha.strip())

    arquivo_palavras.close()
    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()  # Seleciona uma posicao aleatoria da lista
    return palavra_secreta      # a palavra secreta sera selecionada de acordo com a posicao aleatoria


def mensagem_abertura():
    print("**********************************************")
    print("******** Bem vindo ao jogo da forca! *********")
    print("**********************************************")


def cria_palavra_vazia(palavra_secreta):    # Cria uma palavra vazia com o mesmo tamanho da palavra secreta
    palavra_vazia = ['_' for letra in palavra_secreta]
    return palavra_vazia


def pede_chute():   # Funcao para receber as entradas do jogador
    return input("Chute uma letra ou palavra:").strip().upper()


def imprime_mensagem_vitoria():     # Imprime a mensagem de vitoria
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_derrota():     # Imprime a mensagem de derrota
    print("Que pena, suas chances acabaram\n")
    print("Voce foi enforcado!")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def desenha_forca(erros):       # Imprime a forca de acordo com o numero de erros do jogador
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def loop_do_jogo(palavra_secreta):
    palavra_aux = cria_palavra_vazia(palavra_secreta)

    enforcou = False
    acertou = False
    letra_encontrada = False
    erros_disponiveis = 7

    while(not enforcou and not acertou):
        print(palavra_aux)

        index = 0
        letra_encontrada = False

        chute = pede_chute()

        if(chute in palavra_secreta):   # Verifica se o chute eh uma substring da palavra
            letra_encontrada = True
            if chute == palavra_secreta:    # Se o chute for a palavra secreta, sai do loop
                acertou = True
            else:                           # Se o chute for apenas uma letra, procura na palavra secreta se existe a mesma letra
                for letra in palavra_secreta:
                    if chute == letra:
                        palavra_aux[index] = letra  # Substitui a letra na palavra_auxiliar
                    index += 1

        if(not letra_encontrada):           # Se o chute do jogador nao for uma letra da palavra e nem a palavra em si
            print(f"A letra {chute} nao esta na palavra")
            erros_disponiveis -= 1          # incrementa o numero de erros
            desenha_forca(erros_disponiveis)    # desenha a forca
            if erros_disponiveis != 0:          # Imprime os erros restantes se o jogador ainda nao perdeu
                print(f"Voce tem {erros_disponiveis} chances sobrando")

        if('_' not in palavra_aux):             # Se o jogador adivinhou todas as letras da palavra, ele ganhou
            acertou = True

        if acertou: # se o jogador ganhou, imprime a mensagem de vitoria
            imprime_mensagem_vitoria()

        enforcou = erros_disponiveis == 0   # Se as chances do jogador acabaram, ele perdeu
        if enforcou:                        # Se o jogador perdeu, imprime a mensagem de derrota
            imprime_mensagem_derrota()

    print(f"A palavra secreta era: {palavra_secreta}")


def jogar():
    mensagem_abertura()
    palavra_secreta = def_palavra_secreta()
    loop_do_jogo(palavra_secreta)

    return


if(__name__ == "__main__"):
    jogar()
