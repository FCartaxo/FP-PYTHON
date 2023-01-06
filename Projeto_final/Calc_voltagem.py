import numpy as np
import os
import math
import time

def limpar():
    os.system("cls")

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

#2 funcao para calcular a potencia util
def pot_util (escolha2):
    if escolha2 == 1:
        print("Tensão: " ,end='')
        tensao2 = float(input())
        while tensao2 <= 0:
            print("\033[0;31mTensão inferior a 0! Introduza outra vez: \033[m" ,end='')
            tensao2 = float(input())
        print("Corrente: " ,end='')
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
        rend /= 100                                                    #transforma em percentagem
        print("Potência total = " ,end='')
        pot_tot = float(input())
        pot_util_res = rend * pot_tot
        print("Potência útil = " ,pot_util_res ,end=' W')

#3 funcao para o rendimento
def rendimento ():
    print()

#4 funcao para potencia corrente alternada
def pot_Reat (escolha4):
    tupla = (3.1416 , 50)    #valor de pi e frequncia (constantes)
    if escolha4 == 1:                         #potencia aparente
        #S=U*I
        tensao4 = float(input("Tensão: "))
        while tensao4 <= 0:
            print("\033[0;31mTensão inferior a 0! Introduza outra vez: \033[m" ,end='')
            tensao4 = float(input())
        corrente4 = float(input("Corrente: "))
        while corrente4 <= 0:
            print("\033[0;31mTensão inferior a 0! Introduza outra vez: \033[m" ,end='')
            corrente4 = float(input())
        pot_apar = tensao4 * corrente4
        print("Potência aparente = " ,pot_apar ,end='VA')
    elif escolha4 == 2:                       #potencia ativa
        #P=R*(I*I)
        resis4 = float(input("Resistência: "))
        while resis4 <= 0:
            print("\033[0;31mTensão inferior a 0! Introduza outra vez: \033[m" ,end='')
            resis4 = float(input())
        corrente4 = float(input("Corrente: "))
        while corrente4 <= 0:
            print("\033[0;31mTensão inferior a 0! Introduza outra vez: \033[m" ,end='')
            corrente4 = float(input())
        pot_ativ = resis4 * (corrente4**2)
        print("Potência aparente = " ,pot_ativ ,end='VA')
    elif escolha4 == 3:                       #potencia reativa
        #Q=X(I*I)
        print("\033[1;36mQuais os elementos do circuito?")
        print("    Opção 1: Só bobine;")                #bobine: Xl=2(pi)fL
        print("    Opção 2: Só condensador;")           #condensador: Xc=1/(2(pi)fC)
        print("    Opção 3: Bobine e condensador;\033[m")     #os dois: Xl-Xc
        escolha_X = int(input("Escolha: "))
        while escolha_X != 1 and escolha_X != 2 and escolha_X != 3:
            print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
            escolha_X = int(input())
        if escolha_X == 1:                          #bobine
            l = float(input("Qual o valor de L(coeficiente de auto-indução da bobine): "))
            while l <= 0:
                print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
                l = int(input())
            corrente4 = float(input("Corrente: "))
            while corrente4 <= 0:
                print("\033[0;31mTensão inferior a 0! Introduza outra vez: \033[m" ,end='')
                corrente4 = float(input())
            xL = 2 * tupla[0] * tupla[1] * l
            q = xL * (corrente4 ** 2)
            print("Valor da potência reativa = " ,q)
        elif escolha_X == 2:                        #condensador
            c = float(input("Qual o valor de C(capacitância 0<C<=1 ): "))
            while c <= 0 or c > 1:
                print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
                c = int(input())
            corrente4 = float(input("Corrente: "))
            while corrente4 <= 0:
                print("\033[0;31mTensão inferior a 0! Introduza outra vez: \033[m" ,end='')
                corrente4 = float(input())
            xC = 1 / (2 * tupla[0] * tupla[1] * c)
            q = xC * (corrente4 ** 2)
            print("Valor da potência reativa = " ,q)
        else:                                       #os dois
            l = float(input("Qual o valor de L(coeficiente de auto-indução da bobine): "))
            while l <= 0:
                print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
                l = int(input())
            c = float(input("Qual o valor de C(capacitância 0<C<=1 ): "))
            while c <= 0 or c > 1:
                print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
                c = int(input())
            corrente4 = float(input("Corrente: "))
            while corrente4 <= 0:
                print("\033[0;31mTensão inferior a 0! Introduza outra vez: \033[m" ,end='')
                corrente4 = float(input())
            xL = 2 * tupla[0] * tupla[1] * l
            xC = 1 / (2 * tupla[0] * tupla[1] * c)
            x = xL - xC
            q = x * (corrente4 ** 2)
            print("Valor da potência reativa = " ,q)

#5 funcao para calcular as leis de kirchoff
def kirchoff():
    #circuito 1                                   #circuito 2                                        #circuito3
    print("""
-------------●-------------             -----|׀---MWMWMWM----MWMWMWM---        -----MWMWMWM---|׀---●-------------●---׀|---MWMWMWM---
|            ≷            |             |                             |        |                   |             |                 |
|            ≷            |             |                             |        |                   |             |                 |
|            ≷            |             |                             |        |                   ≷             ≷                 |
|            ≷            |             ●------------MWMWMWM----------●        |                   ≷             ≷                 |
_            _            _             |                             |        ≷                   |             |                 |
-            -            -             |                             |        ≷                   _             _                 |
|            |            |             -                             ≷        |                   -             -                 |
≷            ≷            ≷             ̅                              ≷        |                   |             |                 |
≷            ≷            ≷             |                             ≷        |                   ≷             ≷                 ≷
≷            ≷            ≷             ≷                             |        |                   ≷             ≷                 ≷
|            |            |             ≷                             |        |                   |             |                 |
---MWMWMWM---●---MWMWMWM---             ≷                             |        |                   |             |                 |
         circuito 1                     -------׀|-----MWMWMWM----------        --------------------●---MWMWMWM---●------------------
                                                    circuito 2                                        circuito3
""")
    lista_eletro = []                  #lista para armazenar as forças eletromotriz
    lista_resistencia = []             #lista para armazenar as resistências
    print("Escolha: " ,end='')
    escolha5 = int(input())
    while escolha5 != 1 and escolha5 != 2 and escolha5 != 3:
        print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
        escolha5 = int(input("Escolha: "))
    if escolha5 == 1:
        print("1")
    elif escolha5 == 2:
        print("2")
    elif escolha5 == 3:
        for i in range (5):
            print("Qual o valor da força eletromotriz " ,end='')
            print(i+1 ,end='')
            print(": " ,end='')
            eletro = float(input())
            while eletro <= 0:
                    print("\033[0;31mInput invalido. Insira outra vez: \033[m",end='')
                    eletro = float(input())
            lista_eletro.append(eletro)
        for i in range (10):
            print("Qual o valor da resistência " ,end='')
            print(i+1 ,end='')
            print(": " ,end='')
            resist = float(input())
            while resist <= 0:
                    print("\033[0;31mInput invalido. Insira outra vez: \033[m",end='')
                    resist = float(input())
            lista_resistencia.append(resist)

#MENU DA CALCULADORA
limpar()
print("\033[1;36m   CALCULADORA DE CIRCUITOS\033[m")
print("\033[0;36mO que pretende calcular:")
print("    1: Tensão;") #calcular a tensao de x resistencias
print("    2: Potencia util;") #calcular pot_util a partir do UI ou rendimento
print("    3: Rendimento;") #calcular o rendimento de um gerador e um motor
print("    4: Corrente alternada;") #calcular a potencia reativa com condensador bobina e resistencia
print("    5: Leis de Kirchoff;\033[m") #leis de kirchoff e representação do mesmo
print("Escolha: ",end='')
escolha = int(input())

if escolha == 1:
    limpar()
    time.sleep(0.5)
    print("Corrente: " ,end='')
    corrente = float(input())
    print("Resistência: " ,end='')
    resistencia = float(input())
    tensao(corrente,resistencia)
elif escolha == 2:
    limpar()
    time.sleep(0.5)
    print("\033[0;36mComo pretende calcular:")
    print("    Opção 1: tensão/corrente")
    print("    Opção 2: rendimento\033[m")
    print("Escolha: " ,end='')
    escolha2 = int(input())
    while escolha2 != 1 and escolha2 != 2:
        print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
        escolha2 = int(input())
    pot_util(escolha2)
elif escolha == 3:
    limpar()
    time.sleep(0.5)
    rendimento()
elif escolha == 4:
    limpar()
    time.sleep(0.5)
    print("\033[0;36mPotência aparente, Potência ativa, Potência reativa?")
    print("Opção 1, 2, 3?\033[m")
    escolha4 = int(input("Escolha: "))
    while escolha4 != 1 and escolha4 != 2 and escolha4 != 3:
        print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
        escolha2 = int(input())
    pot_Reat(escolha4)
elif escolha == 5:
    limpar()
    time.sleep(0.5)
    print("\033[0;36mPretende aplicar as leis de Kirchoff em qual circuito?\033[m")
    kirchoff()
else:
    time.sleep(0.5)
    print("\033[0;31mEscolha uma das opções!\033[m")
