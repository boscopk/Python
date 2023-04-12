from datetime import date

ano_atual = date.today().year
menor = 0
maior = 0

for i in range(1, 6):
    nascimento = int(input("Qual a sua data de nascimento? "))
    if ano_atual - nascimento >= 18:
        maior +=1
    else:
        menor +=1
    
print("{} são maiores de idade!".format(i))