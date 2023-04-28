from random import radiant

def sorteia(numeros):
    numeros = []

    for n in range(0,5):
        numeros.append(radiant(1, 20))
    return numeros

def soma_par(lista_numeros):
    par = []

    for n in lista_numeros:
        if n % 2 == 0:
            par.append(n)
    print("Os numeros pares são: ", par)

print(soma_par(sorteia))
