questoes = ("Quantos elementos há na tabela periodica?: ",
            "Qual animal põe o maior ovo?: ",
            "Qual é o gás mais abundante na atmosfera terrestre?: ",
            "Quantos ossos tem o corpo humano?: ",
            "Qual planeta do sistema solar é mais quente?: ",)
            

opcoes = (("A. 116 ", "B. 117", "C. 118", "D. 119"),
          ("A. Baleia", "B. Crocodilo", "C. Elefante", "D. Avestruz"),
          ("A. Nitrogênio", "B. Oxigênio", "C. Carbono", "D. Hidrogenio"),
          ("A. 206", "B. 207", "C. 208", "D. 209"),
          ("A. Mercurio", "B. Venus", "C. Terra", "D. Marte"))

respostas = ("C", "D", "A", "A", "B")
tentativas = []
placar = 0
numero_da_questao = 0

for questao in questoes:
    print()
    print(questao)
    for opcao in opcoes[numero_da_questao]:
        print(opcao)
        
    tentativa = input("Selecione (A, B, C, D): ").upper()
    tentativas.append(tentativa)
    if tentativa == respostas[numero_da_questao]:
        placar += 1
        print("CORRETO!")
    else:
        print("INCORRETO!")
        print(f"{respostas[numero_da_questao]} é a resposta correta.")
    numero_da_questao += 1
    
print()
print("       RESULTADOS      ")
print()


print("respostas:", end="")
for resposta in respostas:
    print(resposta, end=" ")
print()

print("tentativas:", end="")
for tentativa in tentativas:
    print(tentativa, end=" ")
print()

placar = int(placar / len(questoes) * 100)
print(f"Resultado final: {placar}%")