#2 funcao para calcular a potencia util
def pot_util (escolha2):
    if escolha2 == 1:
        print("Tensão (em Volts): " ,end='')
        tensao2 = float(input())
        while tensao2 <= 0:
            print("\033[0;31mTensão inferior a 0! Introduza outra vez: \033[m" ,end='')
            tensao2 = float(input())
        print("Corrente (em Amperes): " ,end='')
        corrente2 = float(input())
        while corrente2 <= 0:
            print("\033[0;31mCorrente inferior a 0! Introduza outra vez: \033[m" ,end='')
            corrente2 = float(input())
        pot_util_res = tensao2 * corrente2
        print("Potência útil = " ,pot_util_res ,end=' W')
    elif escolha2 == 2:
        print("\033[0;31mRendimento (Maior que 0 e menor que 100%): \033[m" ,end='')
        rend = float(input())
        while rend <= 0 or rend >= 100:                                    
            print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
            rend = float(input())
        rend /= 100                                              #transforma em percentagem
        print("Potência total (em Watts): " ,end='')
        pot_tot = float(input())
        while pot_tot <= 0:
            print("\033[0;31mCorrente inferior a 0! Introduza outra vez: \033[m" ,end='')
            pot_tot = float(input())
        pot_util_res = rend * pot_tot
        print("Potência útil = " ,pot_util_res ,end=' W')
