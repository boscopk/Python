#União de Vetores
vetA = []
vetB = []

for a in range (5):
    vetA.append(int(input("Digite o valor: ")))

for b in range (5):
    vetB.append(int(input("Digite o valor: ")))

vetC = vetA + vetB

print('O menor valor da lista é: ', min(vetC))
print('A soma dos valores no vetor C é :', sum(vetC))
