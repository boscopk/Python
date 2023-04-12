notas = []

for n in range (5):
    notas.append(float(input("Digite sua nota: ")))

media = sum(notas)/len(notas)

for nota in notas:
    if nota > media:
        print(nota)

print("A soma de todas as notas é: ",sum(notas))
print("A média de todas as notas é: ", media)
print("A maior nota da sala é: ", max(notas))