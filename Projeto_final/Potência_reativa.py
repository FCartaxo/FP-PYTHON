#4 funcao para potencia corrente alternada
def pot_Reat (escolha4):
    tupla = (3.1416 , 50)                     #valor de pi e frequncia (constantes)
    if escolha4 == 1:                         #potencia aparente
        #S=U*I
        tensao4 = float(input("Tensão (em Volts): "))
        while tensao4 <= 0:
            print("\033[0;31mTensão inferior a 0! Introduza outra vez: \033[m" ,end='')
            tensao4 = float(input())
        corrente4 = float(input("Corrente (em Amperes): "))
        while corrente4 <= 0:
            print("\033[0;31mCorrente inferior a 0! Introduza outra vez: \033[m" ,end='')
            corrente4 = float(input())
        pot_apar = tensao4 * corrente4
        print("Potência aparente = " ,pot_apar ,end=' VA')
    elif escolha4 == 2:                       #potencia ativa
        #P=R*(I*I)
        resis4 = float(input("Resistência (em Ohms): "))
        while resis4 <= 0:
            print("\033[0;31mResistência inferior a 0! Introduza outra vez: \033[m" ,end='')
            resis4 = float(input())
        corrente4 = float(input("Corrente (em Amperes): "))
        while corrente4 <= 0:
            print("\033[0;31mCorrente inferior a 0! Introduza outra vez: \033[m" ,end='')
            corrente4 = float(input())
        pot_ativ = resis4 * (corrente4**2)
        print("Potência ativa = " ,pot_ativ ,end=' W')
    elif escolha4 == 3:                       #potencia reativa
        #Q=X(I*I)
        print("\033[1;36mQuais os elementos do circuito?")
        print("\tOpção 1: Só bobine;")                #bobine: Xl=2(pi)fL
        print("\tOpção 2: Só condensador;")           #condensador: Xc=1/(2(pi)fC)
        print("\tOpção 3: Bobine e condensador;\033[m")     #os dois: Xl-Xc
        escolha_X = int(input("Escolha: "))
        while escolha_X != 1 and escolha_X != 2 and escolha_X != 3:
            print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
            escolha_X = int(input())
        if escolha_X == 1:                          #bobine
            l = float(input("Qual o valor de L(coeficiente de auto-indução da bobine): "))
            while l <= 0:
                print("\033[0;31mL menor que 0! Introduza outra vez: \033[m" ,end='')
                l = float(input())
            corrente4 = float(input("Corrente (em Amperes): "))
            while corrente4 <= 0:
                print("\033[0;31mCorrente inferior a 0! Introduza outra vez: \033[m" ,end='')
                corrente4 = float(input())
            xL = 2 * tupla[0] * tupla[1] * l
            q = xL * (corrente4 ** 2)
            q = round(q,2)
            print("Valor da potência reativa = " ,q ,end=' VAr')
        elif escolha_X == 2:                        #condensador
            c = float(input("Qual o valor de C(capacitância 0<C<=1 ): "))
            while c <= 0 or c > 1:
                print("\033[0;31mC menor que 0! Introduza outra vez: \033[m" ,end='')
                c = float(input())
            corrente4 = float(input("Corrente (em Amperes): "))
            while corrente4 <= 0:
                print("\033[0;31mCorrente inferior a 0! Introduza outra vez: \033[m" ,end='')
                corrente4 = float(input())
            xC = 1 / (2 * tupla[0] * tupla[1] * c)
            q = xC * (corrente4 ** 2)
            q = round(q,2)
            print("Valor da potência reativa = " ,q ,end=' VAr')
        else:                                       #os dois
            l = float(input("Qual o valor de L(coeficiente de auto-indução da bobine): "))
            while l <= 0:
                print("\033[0;31mL menor que 0! Introduza outra vez: \033[m" ,end='')
                l = float(input())
            c = float(input("Qual o valor de C(capacitância 0<C<=1 ): "))
            while c <= 0 or c > 1:
                print("\033[0;31mC menor que 0! Introduza outra vez: \033[m" ,end='')
                c = float(input())
            corrente4 = float(input("Corrente: "))
            while corrente4 <= 0:
                print("\033[0;31mCorrente inferior a 0! Introduza outra vez: \033[m" ,end='')
                corrente4 = float(input())
            xL = 2 * tupla[0] * tupla[1] * l
            xC = 1 / (2 * tupla[0] * tupla[1] * c)
            x = xL - xC
            q = x * (corrente4 ** 2)
            q = round(q,2)
            print("Valor da potência reativa = " ,q ,end=' VAr')
exit()