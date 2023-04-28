def media_num(num1,num2):
    media_calculo = (num1 + num2) /2
    return media_calculo

def status_aluno(media_num):
    if media_num > 6:
        print("Aprovado!")
    elif media_num >= 4 and media_num < 6:
        print("Verificação Suplementar!")
    else:
        print('Reprovado!')

num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))

media_num = media_num(num1, num2)
status_aluno(media_num)
