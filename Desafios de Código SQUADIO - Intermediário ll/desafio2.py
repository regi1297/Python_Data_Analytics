import sys

def classificar_fruta(peso, textura, cor):
    if peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
    elif peso >= 130 and textura == "rough" and cor == "red":
        return "A fruta é uma maçã!"
    elif peso >= 120 and textura == "smooth" and cor == "orange":
        return "A fruta é uma laranja!"
    elif peso >= 150 and textura == "rough" and cor == "yellow":
        return "A fruta é uma banana!"
    else:
        return "Não foi possível classificar a fruta."

# Leitura das entradas do usuário usando sys.stdin.readline
peso = float(sys.stdin.readline().strip())
textura = sys.stdin.readline().strip().lower()
cor = sys.stdin.readline().strip().lower()

# Classificação da fruta
resultado = classificar_fruta(peso, textura, cor)

# Exibição da saída
print(resultado)
