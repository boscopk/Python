#Calculando o maior e o menor peso

maior = 0
menor = 0

for i in range(1,6):
    peso = float(input("Insira o {}º peso: ".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("O maior peso lido foi de {} Kg e o menor foi de {} Kg".format(maior,menor))