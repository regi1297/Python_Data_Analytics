texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("execução no final do laço")


for numero in range(0, 51, 5):
    print(numero, end=" ")