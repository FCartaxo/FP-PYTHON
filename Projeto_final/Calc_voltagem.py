import numpy as np
import math
#funcao para calcular a tensao 
def tensao (corrente,resistencia,):
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
def pot_util (corrente2,tensao2):
    print()

#funcao para o rendimento
def rendimento ():
    print()

#funcao para a potencia reativa
def pot_Reat ():
    print()

#funcao para calcular as leis de kirchoff
def kirchoff():
    #circuito 1
    print("""
---MWMWMWM---.---MWMWMWM---
|            |            |
|            |            |
_            _            _
-            -            -
|            |            |
|            |            |
|            Σ            |
|            Σ            |
|            Σ            |
|------------.------------|
""")
    #circuito 2

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
    print("Corrente: " ,end='')
    corrente2 = float(input())
    print("tensao: " ,end='')
    tensao2 = float(input())
    pot_util(corrente2,tensao2)
elif escolha == 3:
    print()
elif escolha == 4:
    print()
elif escolha == 5:
    print()
else:
    print("Escolha uma das opções!")
