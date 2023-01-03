import numpy as np
import math
#funcao para calcular a tensao 
def tensao (corrente,resistencia):
    r_Eq = 0
    print("Existe mais que uma resistência? (Nao/Sim) " ,end='')
    escolha_resis = str(input())
    while escolha_resis != 'Sim' and escolha_resis != 'Nao' and escolha_resis != 'sim' and escolha_resis != 'nao':
        print("Input invalido. Insira outra vez!")
        escolha_resis = str(input())
    if escolha_resis == 'Sim' or escolha_resis == 'sim':
        print("Quantas: " ,end='')
        n_resis = int(input())
        while n_resis <= 0:
            print("Número de resistências inferior a 1!")
            print("Quantas: " ,end='')
            n_resis = int(input())
        print("Paralelo ou série? (P/S) " ,end='')
        escolha_direcao = input()
        while escolha_direcao != 'P' and escolha_direcao != 'S' and escolha_direcao != 'p' and escolha_direcao != 's':
            print("Input invalido. Insira outra vez!")
            escolha_direcao = str(input())
        if escolha_direcao == 'S' or escolha_direcao == 's':    #resistencias em serie
            for i in range (n_resis):
                print("Qual o valor da resistência " ,end='')
                print(i+1 ,end='')
                print(": " ,end='')
                resis = float(input())
                r_Eq += resis
            r_Eq += resistencia
            tensao = r_Eq * corrente
            print("Tensao =" ,tensao)
        elif escolha_direcao == 'P' or escolha_direcao == 'p':   #resistencias em paralelo
            for i in range (n_resis):
                print("Qual o valor da resistência " ,end='')
                print(i+1 ,end='')
                print(": " ,end='')
                resis = float(input())
                numerador = resistencia * resis
                denominador = resistencia + resis
            r_Eq = numerador / denominador
            tensao = r_Eq * corrente
            print("Tensao =" ,tensao)
    elif escolha_resis == 'Nao' or escolha_resis =='nao':
        tensao = resistencia * corrente
        print("Tensão = %s" %tensao)
    else:
        print("Input inválido")

#funcao para calcular a potencia util
def pot_util ():
    print("\nComo pretende calcular:")
    print("    Opção 1: tensão/corrente")
    print("    Opção 2: rendimento")
    print("Escolha: " ,end='')
    escolha2 = int(input())
    while escolha2 != 1 and escolha2 != 2:
        print("Input inválido! Introduza outra vez: " ,end='')
        escolha2 = int(input())
    if escolha2 == 1:
        print("Tensão: " ,end='')
        tensao2 = float(input())
        while tensao2 <= 0:
            print("Tensão inferior a 0! Introduza outra vez: " ,end='')
            tensao2 = float(input())
        print("Corrente: " ,end='')
        corrente2 = float(input())
        while corrente2 <= 0:
            print("Corrente inferior a 0! Introduza outra vez: " ,end='')
            corrente2 = float(input())
        pot_util_res = tensao2 * corrente2
        print("Potência útil:" ,pot_util_res)
    elif escolha2 == 2:
        print("Rendimento (Maior que 0 e menor que 100%): " ,end='')
        rend = float(input())
        while rend <= 0 and rend >= 100:
            print("Input inválido! Introduza outra vez: " ,end='')
            rend = float(input())
        rend /= 100
        print("Potência total: " ,end='')
        pot_tot = float(input())
        pot_util_res = rend * pot_tot
        print("Potência útil: " ,pot_util_res)

#funcao para o rendimento
def rendimento ():
    print()

#funcao para a potencia reativa
def pot_Reat ():
    print()

#funcao para calcular as leis de kirchoff
def kirchoff():
    #circuito 1                                   #circuito 2
    print("""
-------------●-------------             -----|׀---MWMWMWM----MWMWMWM---
|            Σ            |             |                             |
|            Σ            |             |                             |
|            Σ            |             |                             |
|            |            |             ●------------MWMWMWM----------●
_            _            _             |                             |
-            -            -             |                             |
|            |            |             -                             ≷
≷            ≷            ≷             ̅                              ≷
≷            ≷            ≷             |                             ≷
≷            ≷            ≷             ≷                             |
|            |            |             ≷                             |
---MWMWMWM---●---MWMWMWM---             ≷                             |
         circuito 1                     -------׀|-----MWMWMWM----------
                                                    circuito 2
""")
    print("Escolha: " ,end='')
    escolha5 = int(input())
    if escolha5 == 1:
        print("1")
    elif escolha5 == 2:
        print("2")
    else:
        print("Escolha uma das opções!")
    

#MENU DA CALCULADORA
print("\n   CALCULADORA DE CIRCUITOS")
print("O que pretende calcular: ")
print("    1: Tensão;") #calcular a tensao de x resistencias
print("    2: Potencia util;") #calcular pot_util a partir do UI ou rendimento
print("    3: Rendimento;") #calcular o rendimento de um gerador e um motor
print("    4: Potência reativa;") #calcular a potencia reativa com condensador bobina e resistencia
print("    5: Leis de Kirchoff;") #leis de kirchoff e representação do mesmo
print("Escolha: ",end='')
escolha = int(input())

if escolha == 1:
    print("Corrente: " ,end='')
    corrente = float(input())
    print("Resistência: " ,end='')
    resistencia = float(input())
    tensao(corrente,resistencia)
elif escolha == 2:
    pot_util()
elif escolha == 3:
    print()
elif escolha == 4:
    print()
elif escolha == 5:
    print("Pretende aplicar as leis de Kirchoff em qual circuito?")
    kirchoff()
else:
    print("Escolha uma das opções!")
