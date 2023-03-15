#Distancia

distancia = float(input("Insira a distância da viagem: "))
passagem = 0


if distancia <= 200:
    passagem = 0.50 * distancia

elif distancia >= 200 and distancia <400 :
    passagem = 0.45 * distancia

else:
    passagem = 0.40 * distancia


print("\nA distância foi de ", distancia,"KM", ",por isso, a passagem é do preço de ", passagem, "centavos")