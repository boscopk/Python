matriz = [[], [], [], []]
soma = 0

for linha in range (4):
    for coluna in range (5):
        matriz[linha].append(float(input(f"Digite a quantidade de garrafas vendidas do trimestre [{linha+1}][{coluna+1}]: ")))
        soma += matriz[linha][coluna]

print(soma)