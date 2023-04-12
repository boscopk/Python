vetA = []
vetB = []
par = 0
impar = 0
tam_impar = 0

for a in range (5):
    vetA.append(int(input("Digite o valor: ")))

for b in range (5):
    vetB.append(int(input("Digite o valor: ")))

vetC = vetA + vetB

for c in vetC:
    if c % 2 == 0:
        par += c
    if c % 2 != 0:
        tam_impar += 1
        impar += c 


print('O menor valor da lista é: ', min(vetC))
print('A soma dos valores pares é :', par)
print(f"A media dos valores impares é: {impar/tam_impar:.2f}",)
