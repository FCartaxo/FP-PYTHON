#3 funcao para o rendimento
def rendimento (escolha3):
    if escolha3 == 1:                       #potências útil/total
        pot_util3 = float(input("Potência útil (em Watts): "))
        while pot_util3 < 0:
            print("\033[0;31mPotência útil inferior a 0! Introduza outra vez: \033[m" ,end='')
            pot_util3 = float(input())
        pot_total = float(input("Potência útil (em Watts): "))
        while pot_total < 0:
            print("\033[0;31mPotência total inferior a 0! Introduza outra vez: \033[m" ,end='')
            pot_total = float(input())
        while pot_total <= pot_util3:
            print("\033[0;31mPotência util > Potência total! Introduza outra vez: \033[m" ,end='')
            pot_total = float(input())
        rend3 = pot_util3 / pot_total
        rend3 *= 100
        rend3 = round(rend3, 1)
        print("Rendimento =" , rend3, end='%')
    elif escolha3 == 2:                     #tensão/corrente/força eletromotriz
        tensao3 = float(input("Tensão (em Volts): "))
        while tensao3 <= 0:
            print("\033[0;31mTensão inferior a 0! Introduza outra vez: \033[m" ,end='')
            tensao3 = float(input())
        corrente3 = float(input("Corrente (em Volts): "))
        while corrente3 <= 0:
            print("\033[0;31mCorrente inferior a 0! Introduza outra vez: \033[m" ,end='')
            corrente3 = float(input())
        f_motriz3 = float(input("Corrente (em Volts): "))
        while f_motriz3 <= 0:
            print("\033[0;31mForça eletromotriz inferior a 0! Introduza outra vez: \033[m" ,end='')
            f_motriz3 = float(input())
        while f_motriz3 <= tensao3:
            print("\033[0;31mForça eletromotriz < Tensão! Introduza outra vez: \033[m" ,end='')
            f_motriz3 = float(input())
        pot_util3 = tensao3 * corrente3
        pot_total = f_motriz3 * corrente3
        rend3 = pot_util3 / pot_total
        rend3 *= 100
        rend3 = round(rend3, 1)
        print("Rendimento =" , rend3, end='%')