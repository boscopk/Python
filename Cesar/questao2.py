#João e Maria e seus carros
continuar = 's'
cont = 0
ano_carros = []

while continuar != 'n':
    marca_carro = input("Digite a marca do carro: ")
    ano_carro = int(input("Digite o ano do carro: "))
    ano_carros.append(ano_carro)
    velocidade_carro = float(input("Digite a velocidade do carro: "))
    
    continuar = input("Você deseja digitar as informações de mais carros? S/N: ").lower()

    cont+=1

    print(f"A quantidade de carros foram{cont} e o carro mais novo lido é o de ano {max(ano_carros)}")
