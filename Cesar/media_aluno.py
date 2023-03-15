#Verificar média do aluno

nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))
frequencia = float(input("Qual foi a porcetagem da sua frequencia? ")) 
media = (nota_1 + nota_2) /2
aluno = 0


if frequencia >= 0.75:
    if media >=7:
        print("Aprovado por média!")
    else:
        print("Reprovado por média!")
else:
    print("Reprovado por falta!")
