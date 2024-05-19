# Desafio: A Aventura do Explorador

# Entrada
import sys

# Lê a entrada do usuário usando sys.stdin.readline
quantidade_passos = int(sys.stdin.readline().strip())

# Verifica se a quantidade de passos é zero ou negativa
if quantidade_passos <= 0:
    print("Nenhum passo dado na floresta.")
else:
    # Utiliza um loop para imprimir a mensagem do explorador para cada passo
    for passo in range(1, quantidade_passos + 1):
        if passo == 1:
            print(f"Explorador: {passo} passo")
        else:
            print(f"Explorador: {passo} passos")