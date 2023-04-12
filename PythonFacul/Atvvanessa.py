quantSeguidores = int(input("Quantos seguidores? "))

if (quantSeguidores >= 300):

    quantCurtidas = int(input("Quantas curtidas você teve em sua foto? "))

    if (quantCurtidas > 1000):
            print("Você ganhou uma camiseta!!")

    elif (quantCurtidas >= 500 and quantCurtidas <= 1000):
                print("Você ganhou um boné!!")
            
    elif (quantCurtidas >=100 and quantCurtidas < 500):
                print("Você ganhou um chaveiro!!")

else: 
    print("Infelizmente você não tem os requisitos mínimos para participar da promoção")