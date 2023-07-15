import jogo_advinhacao
import jogo_forca

selecao_valida = False
while(True):                        # Continua a execucao ate que seja escolhida a opcao de sair
    while(not(selecao_valida)):     # Roda o While enquanto nao for selecionada uma expressao valida
        print("**********************************************")
        print("******** Bem vindo ao JogosBarretown! ********")
        print("**********************************************")
        print()

        print("Selecione o jogo que deseja jogar:")
        print("(1) Jogo da Adivinhacao  (2) Jogo da Forca  (0) Cancelar/Sair")

        jogo_selecionado = int(input("Jogo selecionado: ").strip())
        if(jogo_selecionado in range(0, 3)):
            selecao_valida = True
        else:
            print("Digite uma opcao valida!")

    print()
    # abre o respectivo jogo selecionado ou para a execucao
    if(jogo_selecionado == 1):
        jogo_advinhacao.jogar()

    elif(jogo_selecionado == 2):
        jogo_forca.jogar()

    elif(jogo_selecionado == 0):
        exit()
