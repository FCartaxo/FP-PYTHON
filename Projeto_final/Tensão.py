
#1 funcao para calcular a tensao 
def tensao (corrente,resistencia):
    r_Eq = 0
    print("\033[0;31mExiste mais que uma resistência? (Nao/Sim) \033[m" ,end='')
    escolha_resis = str(input())
    while escolha_resis != 'Sim' and escolha_resis != 'Nao' and escolha_resis != 'sim' and escolha_resis != 'nao':
        print("\033[0;31mInput invalido. Insira outra vez!\033[m")
        escolha_resis = str(input())
    if escolha_resis == 'Sim' or escolha_resis == 'sim':
        print("Quantas: " ,end='')
        n_resis = int(input())
        while n_resis <= 0:
            print("\033[0;31mNúmero de resistências inferior a 1!\033[m")
            print("Quantas: " ,end='')
            n_resis = int(input())
        print("\033[0;31mParalelo ou série? (P/S) \033[m" ,end='')
        escolha_direcao = input()
        while escolha_direcao != 'P' and escolha_direcao != 'S' and escolha_direcao != 'p' and escolha_direcao != 's':
            print("\033[0;31mInput invalido. Insira outra vez: \033[m")
            escolha_direcao = str(input())
        if escolha_direcao == 'S' or escolha_direcao == 's':    #resistencias em serie
            for i in range (n_resis):
                print("Qual o valor da resistência " ,end='')
                print(i+1 ,end='')
                print(": " ,end='')
                resis = float(input())
                while resis <= 0:
                    print("\033[0;31mInput invalido. Insira outra vez: \033[m",end='')
                    resis = float(input())
                r_Eq += resis
            r_Eq += resistencia
            tensao = r_Eq * corrente
            print("Tensao = " ,tensao ,end=' V')
        elif escolha_direcao == 'P' or escolha_direcao == 'p':   #resistencias em paralelo
            r_Eq = resistencia
            for i in range (n_resis):
                resistencias = []                                #lista das resistencias inseridas
                print("Qual o valor da resistência " ,end='')
                print(i+1 ,end='')
                print(": " ,end='')
                resis = float(input())
                while resis <= 0:
                    print("\033[0;31mInput invalido. Insira outra vez: \033[m",end='')
                    resis = float(input())
                resistencias.append(resis)
                r_Eq = (r_Eq * resistencias[i-1]) / (r_Eq + resistencias[i-1])
            tensao = r_Eq * corrente                               
            print("Tensao = " ,tensao ,end=' V')
    elif escolha_resis == 'Nao' or escolha_resis =='nao':
        tensao = resistencia * corrente
        print("Tensão = " ,tensao ,end=' V')
    #else:
    #    print("\033[0;31mInput inválido\033[m")