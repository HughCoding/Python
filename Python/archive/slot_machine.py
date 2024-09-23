import random
import time

def girar_coluna():
    simbolos = ['🍒', '🍉', '🍋', '🔔', '⭐']
    
    return [random.choice(simbolos) for _ in range(3)]

def animar_giro():
    simbolos = ['🍒', '🍉', '🍋', '🔔', '⭐']
    coluna_final = girar_coluna() 
    for _ in range(10):  
        coluna_aleatoria = [random.choice(simbolos) for _ in range(3)]
        print(" | ".join(coluna_aleatoria), end="\r") 
        time.sleep(0.1)  
    print(" | ".join(coluna_final)) 
    return coluna_final 

def receber_pagamento(coluna, aposta):
    if coluna[0] == coluna[1] == coluna[2]:
        if coluna[0] == '🍒':
            return aposta * 3
        elif coluna[0] == '🍉':
            return aposta * 4
        elif coluna[0] == '🍋':
            return aposta * 5
        elif coluna[0] == '🔔':
            return aposta * 10
        elif coluna[0] == '⭐':
            return aposta * 20
        
    return 0

def main():
    saldo = 100
    
    print("Bem-Vindo ao Cassino Python")
    print("Símbolos: 🍒 🍉 🍋 🔔 ⭐")
    
    while saldo > 0:
        print(f"Saldo atual: ${saldo}")
        
        aposta = input("Digite sua aposta: ")
        
        if not aposta.isdigit():
            print("Por favor, digite um número válido.")
            continue
        
        aposta = int(aposta)

        if aposta > saldo:
            print("Saldo insuficiente.")
            continue
        
        if aposta <= 0:
            print("A aposta deve ser maior que 0.")
            continue
        
        saldo -= aposta
        
        print("Girando...\n")
        coluna = animar_giro() 
        
        pagamento = receber_pagamento(coluna, aposta)
        
        if pagamento > 0:
            print(f"Você ganhou ${pagamento}")
        else:
            print()
            print("Desculpe, você perdeu esse round.")
            
        saldo += pagamento
        
        jogar_novamente = input("Deseja jogar novamente? (S/N): ").upper()
        
        if jogar_novamente != 'S':
            break
        
    print(f"Fim de jogo! Seu saldo final é ${saldo}")

if __name__ == '__main__':
    main()
