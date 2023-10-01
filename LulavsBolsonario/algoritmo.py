from classes import *
import os
import time

def bolsonaros():
    print("Qual golpe você deseja:")
    print("[1]Soco \n[2]Esquivar \n[3]Facada no Estomago \n[4]Tosse Covid \n[5]Toma Cloroquina")
    opção = input("-")
    if opção == "1":
        bolsonaro.atacar(lula)
        print(f"HP Bolsonaro: {bolsonaro.getvida()} e o HP Lula: {lula.getvida()}") 
        os.system("pause")
        os.system("cls")       
    elif opção == "2":
        bolsonaro.esquivar()
        print(f"HP Bolsonaro: {bolsonaro.getvida()} e o HP Lula: {lula.getvida()}") 
        os.system("pause")
        os.system("cls")             
    elif opção == "3":
        bolsonaro.Facadanoestomago()
        print(f"HP Bolsonaro: {bolsonaro.getvida()} e o HP Lula: {lula.getvida()}")  
        os.system("pause")
        os.system("cls")            
    elif opção == "4":
        bolsonaro.Tossedacovid()
        print(f"HP Bolsonaro: {bolsonaro.getvida()} e o HP Lula: {lula.getvida()}")  
        os.system("pause")
        os.system("cls")            
    elif opção == "5":
        bolsonaro.Tomacloroquina()
        print(f"HP Bolsonaro: {bolsonaro.getvida()} e o HP Lula: {lula.getvida()}")
        os.system("pause")
        os.system("cls")              

def lulas():
    print("Qual golpe você deseja:")
    print("[1]Soco \n[2]Esquivar \n[3]Amizade \n[4]Picanha e Cervejinha \n[5]Ajuda dos gays")
    opção = input("-")
    if opção == "1":
        lula.atacar(bolsonaro) 
        print(f"HP Bolsonaro: {bolsonaro.getvida()} e o HP Lula: {lula.getvida()}")
        os.system("pause")
        os.system("cls")                   
    elif opção == "2":
        lula.esquivar()
        print(f"HP Bolsonaro: {bolsonaro.getvida()} e o HP Lula: {lula.getvida()}") 
        os.system("pause")
        os.system("cls")             
    elif opção == "3":
        lula.amizade()
        print(f"HP Bolsonaro: {bolsonaro.getvida()} e o HP Lula: {lula.getvida()}") 
        os.system("pause")
        os.system("cls")             
    elif opção == "4":
        lula.Picanhaecervejinha()
        print(f"HP Bolsonaro: {bolsonaro.getvida()} e o HP Lula: {lula.getvida()}")  
        os.system("pause")
        os.system("cls")            
    elif opção == "5":
        lula.AjudaLGBTQIAPN()
        print(f"HP Bolsonaro: {bolsonaro.getvida()} e o HP Lula: {lula.getvida()}")
        os.system("pause")
        os.system("cls")              


print("Esse é um jogo de luta: Bolsonaro vs Lula")
print("Qual personagem você deseja escolher?")
print("Jogador 1\n[1] Bolsonaro\n[2] Lula")
escolha = input("-")

if escolha == "1":
    print("Você escolheu o Bolsonaro!")
    print("Jogador 2 é o Lula")
    time.sleep(3)
    os.system("cls")
    print("Você está no campo de batalha, à sua frente, caminhando em sua direção, Lula aparece furioso. Ele quer lutar contra você, está preparado?")
    bolsonaros()        


if escolha == "2":
    print("Você escolheu o Lula!")
    print("Jogador 2 é o Bolsonaro")
    time.sleep(3)
    os.system("cls")
    print("Você está no campo de batalha, à sua frente, caminhando em sua direção, Bolsonaro aparece furioso. Ele quer lutar contra você, está preparado?")
    lulas()

o = 1
while o == 1:
    if escolha == "1":
        lulas()
        bolsonaros()
        if lula.getvida() <= 0:
            print("Bolsonaro venceu! Tente em uma proxima :(")
            time.sleep(3)
            os.system("cls")
            print(F"Bolsonaro está evoluindo.... {time.sleep(2)} SUPER BOLSONARO MAÇOM!!")
            o = 0
        elif bolsonaro.getvida() <= 0:
            print("Lula venceu, FAZ O L! Tente em uma proxima :(")
            time.sleep(3)
            os.system("cls")
            print(F"Lula está evoluindo.... {time.sleep(2)} LULA BOTEQUEIRO TOMANDO UMA CERVEJINHA!!")
            o = 0
        else:
            escolha = "1"
    elif escolha == "2":
        bolsonaros()
        lulas()
        if lula.getvida() <= 0:
            print("Bolsonaro venceu! Tente em uma proxima :(")
            time.sleep(3)
            os.system("cls")
            print(F"Bolsonaro está evoluindo.... {time.sleep(2)} SUPER BOLSONARO MAÇOM!!")
            o = 0
        elif bolsonaro.getvida() <= 0:
            print("Lula venceu, FAZ O L! Tente em uma proxima :(")
            time.sleep(3)
            os.system("cls")
            print(F"Lula está evoluindo.... {time.sleep(2)} LULA BOTEQUEIRO TOMANDO UMA CERVEJINHA!!")
            o = 0
        else:
            escolha = "2"