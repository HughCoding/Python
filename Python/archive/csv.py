import csv
import time
import sys

class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'
    VALID = '\033[32m'

usuarios = []

def mensagem_inicial(mensagem, color_code, delay=0.05):
    cor_inicial = f"\033[{color_code}m"
    cor_final = "\033[0m"  
    mensagem_formatada = f"{cor_inicial}{mensagem}{cor_final}"
    
    for char in mensagem_formatada:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    while True:
        email = input("Digite o email do usuário: ")
        if '@' in email:
            break
        else:
            print(
                TerminalColor.ERRO +
                "Email inválido. O email deve conter o caractere '@'. Tente novamente."
                + TerminalColor.NORMAL)

    user_id = len(usuarios) + 1
    usuarios.append([user_id, nome, email])
    print(TerminalColor.VALID + "Cadastrado com sucesso!" + TerminalColor.NORMAL)

def listar_usuarios():
    if usuarios:
        print("\nLista de Usuários Cadastrados:")
        for user in usuarios:
            print(f"ID: {user[0]}, Nome: {user[1]}, Email: {user[2]}")
            time.sleep(1)
    else:
        print(TerminalColor.ERRO + "Nenhum usuário cadastrado." +
              TerminalColor.NORMAL)

def consultar_usuario():
    user_id = int(input("Digite o ID do usuário para consultar: "))
    for user in usuarios:
        if user[0] == user_id:
            print(f"ID: {user[0]}, Nome: {user[1]}, Email: {user[2]}")
            time.sleep(1)
            return
    print(TerminalColor.ERRO + "Usuário não encontrado." +
          TerminalColor.NORMAL)

def excluir_usuario():
    user_id = int(input("Digite o ID do usuário a ser excluído: "))
    for user in usuarios:
        if user[0] == user_id:
            usuarios.remove(user)
            print(TerminalColor.VALID + "Usuário excluído com sucesso!" + TerminalColor.NORMAL)
            return
    print(TerminalColor.ERRO + "Usuário não encontrado." +
          TerminalColor.NORMAL)

def salvar_lista_csv():
    with open('usuarios.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nome", "Email"])
        writer.writerows(usuarios)
    print("Lista de usuários salva no arquivo 'usuarios.csv'.")

def index():
    mensagem_inicial("Olá! Ao preencher as informações de cadastro, selecione a opção '0' para salvar o arquivo .csv", 35)
    while True:
        print("\nMenu:")
        print("0 - Sair (criar arquivo csv)")
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Consultar Usuário")
        print("4 - Excluir Usuário")

        opcao = input("Escolha uma opção: ")

        if opcao == '0':
            salvar_lista_csv()
            print("Programa encerrado.")
            break
        elif opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            listar_usuarios()
        elif opcao == '3':
            consultar_usuario()
        elif opcao == '4':
            excluir_usuario()
        else:
            print(TerminalColor.ERRO + "Opção inválida. Tente novamente." +
                  TerminalColor.NORMAL)

if __name__ == "__main__":
    index()
