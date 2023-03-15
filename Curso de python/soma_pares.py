#soma de numeros pares

soma = 0
cont = 0

for i in range(1, 7):
    numero = int(input("Insira um número: "))
    if numero % 2 == 0:
        soma += numero
        cont += 1

print("A soma de todos os {} números pares é: {}".format(cont, soma))