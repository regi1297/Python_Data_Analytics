#Descrição
#Com as máquinas pesadas agrupadas estrategicamente, graças ao seu algoritmo de cálculo energético, agora a mineração está muito mais eficiente! Com isso, os CodeMiners logo terão que aumentar a capacidade de armazenamento de dados em seus discos de Mithril. Atualmente, cada máquina tem uma capacidade em teraflops e todas terão um upgrade! Escreva um programa que calcule a nova capacidade total de todas as máquinas após um aumento percentual específico.

#Entrada
#Dois valores inteiros positivos, representando a capacidade atual total em teraflops e o aumento percentual, separados por espaço.

#Saída
#A nova capacidade total em teraflops.

#Exemplos
#A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

#Entrada	Saída
# 100 20	120
# 50 10	55
# 200 50	300

# Leitura dos valores de entrada
entrada = input().strip()
capacidade_atual, aumento_percentual = map(int, entrada.split())

# Cálculo do aumento em teraflops
aumento = capacidade_atual * aumento_percentual / 100

# Cálculo da nova capacidade total
nova_capacidade_total = capacidade_atual + aumento

# Impressão da nova capacidade total
print(int(nova_capacidade_total))


