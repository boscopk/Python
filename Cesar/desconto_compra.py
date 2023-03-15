#desconto

nome = input("Insira seu nome: ")
sexo = input("Insira seu sexo: F ou M? ").upper()
valor_compras = float(input("Qual o valor da compra? "))
valor_com_desconto = 0


if (sexo == 'F'):
    valor_com_desconto =  valor_compras - (valor_compras * 0.13)

else:
    valor_com_desconto = valor_compras - (valor_compras * 0.05)


print(nome, "pagou", valor_com_desconto)
