valor_cliente = float(input("Qual o preço do produto? "))
valor_total = 0

while valor_cliente !=0:

    if valor_cliente > 0:
        valor_total = valor_total + valor_cliente
        
    else:
        print("Valor inválido!")

        valor_cliente = float(input("Qual o preço do produto? "))
   
if valor_total > 1000.00:
    valor_total = valor_total * 0.9


print("O valor total a pagar é: R$ %.2f" % valor_total)
