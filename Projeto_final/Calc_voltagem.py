import numpy as np
import os
import math
import time
import Tensão
import Potência_Util
import Rendimento
import Potência_reativa
import Leis_kirchoff

def limpar():
    os.system("cls")

                    #MENU DA CALCULADORA
limpar()
print("\033[1;36m   CALCULADORA DE CIRCUITOS\033[m")
print("\033[0;36mO que pretende calcular:")
print("\t1: Tensão;") #calcular a tensao de x resistencias
print("\t2: Potencia util;") #calcular pot_util a partir do UI ou rendimento
print("\t3: Rendimento;") #calcular o rendimento de um gerador e um motor
print("\t4: Corrente alternada;") #calcular a potencia reativa com condensador bobina e resistencia
print("\t5: Leis de Kirchoff;") #leis de kirchoff e representação do mesmo
print("\tPressione 0 para sair!\033[m")
print("Escolha: ",end='')

escolha = int(input())
while escolha < 0 or escolha > 6:
    print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
    escolha = int(input())

if escolha == 0:
    print("\033[0;31mSaiu!\033[m")
    exit()
elif escolha == 1:
    limpar()
    time.sleep(0.5)
    print("Corrente (em Amperes): " ,end='')
    corrente = float(input())
    print("Resistência (em Ohms): " ,end='')
    resistencia = float(input())
    Tensão(corrente,resistencia)
elif escolha == 2:
    limpar()
    time.sleep(0.5)
    print("\033[0;36mComo pretende calcular:")
    print("\tOpção 1: tensão/corrente")
    print("\tOpção 2: rendimento\033[m")
    print("Escolha: " ,end='')
    escolha2 = int(input())
    while escolha2 != 1 and escolha2 != 2:
        print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
        escolha2 = int(input())
    Potência_Util(escolha2)
elif escolha == 3:
    limpar()
    time.sleep(0.5)
    print("\033[0;36mComo pretende calcular:")
    print("\tOpção 1: potências útil/total")
    print("\tOpção 2: tensão/corrente/força eletromotriz\033[m")
    escolha3 = int(input("Escolha: "))
    while escolha3 != 1 and escolha3 != 2:
        print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
        escolha3 = int(input())
    Rendimento(escolha3)
elif escolha == 4:
    limpar()
    time.sleep(0.5)
    print("\033[0;36mPotência aparente, Potência ativa, Potência reativa?")
    print("Opção 1, 2, 3?\033[m")
    escolha4 = int(input("Escolha: "))
    while escolha4 != 1 and escolha4 != 2 and escolha4 != 3:
        print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
        escolha4 = int(input())
    Potência_reativa(escolha4)
elif escolha == 5:
    limpar()
    time.sleep(0.5)
    print("\033[0;36mPretende aplicar as leis de Kirchoff em qual circuito?\033[m")
    Leis_kirchoff()
else:
    time.sleep(0.5)
    print("\033[0;31mEscolha uma das opções!\033[m")