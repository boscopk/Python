def TestaCompatibilidade(nome1, data1, nome2,data2):
    dataReal1 = data1.split("/")
    dataReal2 = data2.split("/")
    if(dataReal2[2] == dataReal1[2]):
        if(nome1[0] == nome2[0]):
            return True
        else:
            return False
    return False