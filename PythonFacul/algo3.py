quant = 10 
lista = []
for i in range(1, quant,3):
    x = i + 1
    if(x > 3):
        lista.append(x + 2)
    else:
        lista.append(4 * 2)
print(lista)