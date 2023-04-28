#Media ponderada de um aluno
nome = input("Qual é o seu nome? ")
nota1 = float(input("Qual é a sua primeira nota? "))
nota2 = float(input("Qual é a sua segunda nota? "))
nota3 = float(input("Qual é a sua terceira nota? "))

media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
print("Sua media ficou: ", media_ponderada)

if media_ponderada <= 4.9:
    print(f"{nome}, você está reprovado!")

elif (media_ponderada) >= 5 and (media_ponderada) <= 6.9:
    print(f"{nome}, você está de recuperação!")

elif media_ponderada >= 7:
    print(f"{nome}, você está aprovado!")