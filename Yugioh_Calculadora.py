HPJ1 = 8000
HPJ2 = 8000
nomejg1 = 'Jogador1'
nomejg2 = 'Jogador2'

a=0
b=0

fim_de_jogo=0

while b==0:

    nome = input(str("\nVai alterar os nomes dos jogadores? 'sim' ou 'não'?"))

    if nome == "sim":
        nomejg1 = input(str("\nQual o nome do jogador 1?"))
        nomejg2 = input(str("\nQual o nome do jogador 1?"))
        b=1

    elif nome =="não":
        print("\nOk, então os nomes serão {} e {}".format(nomejg1,nomejg2))
        b=1

    else:
        print("\nDeixa de ser besta homi...\nDiga se 'sim' ou se 'não'(E sem as aspas, seu acefalo).")


while fim_de_jogo == 0:

    print("\nPontos de vida dos jogadores:\n{}: {} pts\n{}: {} pts".format(nomejg1,HPJ1,nomejg2,HPJ2))

    while a == 0:
        print("\nVai modificar a vida de qual jogador?")
        jg = input(str("{} (1) ou {} (2)? ".format(nomejg1,nomejg2)))

        if(jg == "1" or jg == "2"):
            a = 1
        else:
            print("\nDigite um jogador válido!!!")

    if(jg =="1"):
        valor = input("\nCaso o jogador esteja perdendo pontos de vida digite '-' antes do valor.\nQuantos pontos?")
        pts = int(valor)
        HPJ1 = HPJ1+pts
        a = 0
        
        if HPJ1 == 0:
            fim_de_jogo = 1

    elif(jg == "2"):
        valor = input("\nCaso o jogador esteja perdendo pontos de vida digite '-' antes do valor.\nQuantos pontos?")
        pts = int(valor)
        HPJ2 = HPJ2+pts
        a = 0

        if HPJ2 == 0:
            fim_de_jogo = 1

if HPJ1 == 0:
    print("\nFim de jogo!!!\nO vencedor foi {}".format(nomejg2))

else:
    print("\nFim de jogo!!!\nO vencedor foi {}".format(nomejg1))
