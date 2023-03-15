#Conta de energia eletrica

kw = float(input("Insira a quantidade de kw: "))
taxa_basica = 5

if kw <= 500 : 
    kw = (kw * 0.02) + taxa_basica
    print("Seu consumo foi de ", kw)

elif kw >500 and kw <=1000 :
    kw = (kw * 10) + taxa_basica
    print("Seu consumo foi de ", kw)

else :
    kw = (kw * 35) + taxa_basica
    print("Seu consumo foi de ", kw)