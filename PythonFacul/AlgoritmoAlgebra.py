#Criando Matriz A
print("Digite a ordem da Matriz Anxm")
numLinhas = int(input(("Número de Linhas(n):")))
numColunas = int(input(("Número de Colunas(m):")))
print("A"+ str(numColunas) + "x" + str(numColunas))
matrizA = []
print("Digite os elementos da Matriz A")
for i in range(numLinhas):
    matrizA.append(list())
for i in range(numLinhas):
   for j in range(numColunas):
       matrizA[j].append(list())
for i in range(numLinhas):
   for j in range(numColunas):
        elemento =int(input("A("+str(i+1)+str(j+1)+"):"))
        matrizA[i][j].append(elemento)
print(matrizA)

#Processo de Escalonamento
