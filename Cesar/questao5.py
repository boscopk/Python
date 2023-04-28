#Função auxilio

from datetime import date

ano_atual = date.today().year

def auxilio(ano_nascimento):
    idade = ano_atual - ano_nascimento
    
    if 4 <= idade <= 16:
        return f"Devido a sua idade ({idade}), você está incluso no auxílio escolar!!"
    else:
        return f"Devido a sua idade ({idade}), você não está incluso no auxílio escolar!!"

ano_nascimento = int(input("Em qual ano você nasceu? "))
print(auxilio(ano_nascimento))