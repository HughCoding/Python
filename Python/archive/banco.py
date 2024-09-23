def mostrar_saldo(saldo):
    print(f"Seu Saldo é de ${saldo:2f}")

def depositar():
    quantia = float(input("Digite uma quantia para ser depositada: "))
    
    if quantia < 0:
        print("Não é uma quantia valida.")
        return 0
    else:
        return quantia

def sacar(saldo):
    quantia = input("Digite uma quantia para sacar:")

    if quantia > saldo: 
        print("Saldo insuficiente.")
        return 0
    elif quantia < 0:
        print("Quantia deve ser maior do que 0.")
        return quantia


def main():
    saldo = 0
    esta_rodando = True

    while esta_rodando:
        print("Banco")
        print("1.Mostrar saldo")
        print("2.Depositar")
        print("3.Sacar")
        print("4.Sair")

        escolha = input("Selecione uma opção (1-4): ")
        
        if escolha == '1':
            mostrar_saldo(saldo)    
        elif escolha == '2':
            saldo += depositar()
        elif escolha == '3':
            saldo -= sacar(saldo)
        elif escolha == '4':
            esta_rodando = False
        else:
            print("Não é uma escolha válida.")

    print("Tenha um ótimo dia!")
    
    
if __name__ == '__main__':
    main()