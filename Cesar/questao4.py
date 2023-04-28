#Valores em ordem decrescente
vetor = []

for i in range(0, 11):
   vetor.append(int(input(f'Digite um valor para a posição {i}: ')))

vetor.sort(reverse = True)

print(f'Os valores em ordem decrescente são: {vetor}')