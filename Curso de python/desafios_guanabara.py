#imprimindo números na tela

numero = int(input("Insira quantos números você quer na tela: "))

for i in range(0, numero+1):
    print(i)


#números pares

for p in range(0, 51, 2):
    print(p)
 
#data de nascimento

soma = 0
cont = 0

for i in range(1, 8):
    nascimento = int(input("Qual a sua data de nascimento? "))
    if nascimento <= 2005:
        soma += nascimento
        cont += 1
    
print("das {}, {} são maiores de idade!".format(cont,soma))