# TODO: Crie a Função para classificar um número como positivo, negativo ou zero
def classificar_numero(numero):
    if numero > 0:
        return "positivo!"
    elif numero < 0:
        return "negativo!"

def main():
    positivos = 0
    negativos = 0

    while True:
        numero = int(input())
        
        if numero == 0:
            break
        
        classificacao = classificar_numero(numero)
        print(classificacao)
        
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

    print(f"{positivos} números positivos, {negativos} números negativos")

if __name__ == "__main__":
    main()
