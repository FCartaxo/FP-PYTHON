import numpy as np
import os

def limpar():
    os.system("cls")

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
         circuito 1                     -------׀|-----MWMWMWM----------        ---׀|---MWMWMWM-----●---MWMWMWM---●------------------
                                                    circuito 2                                        circuito3
""")
    lista_eletro = []                  #lista para armazenar as forças eletromotriz
    lista_resistencia = []             #lista para armazenar as resistências
    print("Escolha: " ,end='')
    escolha5 = int(input())
    while escolha5 != 1 and escolha5 != 2 and escolha5 != 3:
        print("\033[0;31mInput inválido! Introduza outra vez: \033[m" ,end='')
        escolha5 = int(input())
    if escolha5 == 1:
        for i in range (3):
            print("Qual o valor da força eletromotriz (em Volts) " ,end='')
            print(i+1 ,end='')
            print(": " ,end='')
            eletro = float(input())
            while eletro <= 0:
                print("\033[0;31mForça eletromotriz inferior a 0! Insira outra vez: \033[m",end='')
                eletro = float(input())
            lista_eletro.append(eletro)
        for i in range (6):
            print("Qual o valor da resistência " ,end='')
            print(i+1 ,end='')
            print(": " ,end='')
            resist = float(input())
            while resist <= 0:
                print("\033[0;31mResistência inferior a 0! Insira outra vez: \033[m",end='')
                resist = float(input())
            lista_resistencia.append(resist)
        e12 = lista_eletro[0] - lista_eletro[1]
        e23 = lista_eletro[1] - lista_eletro[2]
        r14 = lista_resistencia[0] + lista_resistencia[3]
        r25 = lista_resistencia[1] + lista_resistencia[4]
        r36 = lista_resistencia[2] + lista_resistencia[5]
        array1 = [[1, 1, 1,],
                  [r14, -r25, 0],
                  [0, r25, -r36]]
        array2 = [0, e12, e23]
        
        array1_inv = np.linalg.inv(array1)
        resultado = array1_inv.dot(array2)

        limpar()
        
        for i in range (3):
            if resultado[i] < 0:
                resultado[i] *= -1
            resultado[i] = round(resultado[i], 2)
            print("Corrente " ,end='')
            print(i+1 ,end='')
            print(": " ,end='')
            print(resultado[i] ,end='A')
            print()

    elif escolha5 == 2:
        for i in range (3):
            print("Qual o valor da força eletromotriz (em Volts) " ,end='')
            print(i+1 ,end='')
            print(": " ,end='')
            eletro = float(input())
            while eletro <= 0:
                print("\033[0;31mForça eletromotriz inferior a 0! Insira outra vez: \033[m",end='')
                eletro = float(input())
            lista_eletro.append(eletro)
        for i in range (6):
            print("Qual o valor da resistência " ,end='')
            print(i+1 ,end='')
            print(": " ,end='')
            resist = float(input())
            while resist <= 0:
                print("\033[0;31mResistência inferior a 0! Insira outra vez: \033[m",end='')
                resist = float(input())
            lista_resistencia.append(resist)
        e1 = lista_eletro[0]
        e23 = lista_eletro[1] + lista_eletro[2]
        r14 = lista_resistencia[0] + lista_resistencia[3]
        r6 = lista_resistencia[5]
        r235 = lista_resistencia[1] + lista_resistencia[2] + lista_resistencia[4]
        array1 = [[1, 1, 1,],
                  [-r14, 0, r6],
                  [0, r235, -r6]]
        array2 = [0, e1, e23]
        
        array1_inv = np.linalg.inv(array1)
        resultado = array1_inv.dot(array2)

        limpar()
        
        for i in range (3):
            if resultado[i] < 0:
                resultado[i] *= -1
            resultado[i] = round(resultado[i], 2)
            print("Corrente " ,end='')
            print(i+1 ,end='')
            print(": " ,end='')
            print(resultado[i] ,end='A')
            print()

    elif escolha5 == 3:
        for i in range (5):
            print("Qual o valor da força eletromotriz (em Volts) " ,end='')
            print(i+1 ,end='')
            print(": " ,end='')
            eletro = float(input())
            while eletro <= 0:
                print("\033[0;31mForça eletromotriz inferior a 0! Insira outra vez: \033[m",end='')
                eletro = float(input())
            lista_eletro.append(eletro)
        for i in range (10):
            print("Qual o valor da resistência " ,end='')
            print(i+1 ,end='')
            print(": " ,end='')
            resist = float(input())
            while resist <= 0:
                print("\033[0;31mResistência inferior a 0! Insira outra vez: \033[m",end='')
                resist = float(input())
            lista_resistencia.append(resist)
        e145 = lista_eletro[0] + lista_eletro[3] + lista_eletro[4]
        e34 = lista_eletro[3] - lista_eletro[2]
        e23 = lista_eletro[1] + lista_eletro[2]
        r115 = lista_resistencia[0] + lista_resistencia [4] + lista_resistencia[5]
        r44 = lista_resistencia[3] + lista_resistencia[8]
        r33 = lista_resistencia[2] + lista_resistencia[7]
        r0 = lista_resistencia[9]
        r22 = lista_resistencia[1] + lista_resistencia[6]
        array1 = [[1, 0, 0, -1, 0, -1],
                  [-1, 0, 0, 1, -1, 0], 
                  [0, -1, 1, 0, 0, -1],
                  [-r115, 0, 0, -r44, 0, 0],
                  [0, 0, r33, -r44, -r0, 0],
                  [0, -r22, -r33, 0, 0, 0]]

        array2 = [0, 0, 0, e145, e34 , e23]

        array1_inv = np.linalg.inv(array1)
        resultado = array1_inv.dot(array2)

        limpar()

        for i in range (6):
            if resultado[i] < 0:
                resultado[i] *= -1
            resultado[i] = round(resultado[i], 2)
            print("Corrente " ,end='')
            print(i+1 ,end='')
            print(": " ,end='')
            print(resultado[i] ,end='A')
            print()
exit()