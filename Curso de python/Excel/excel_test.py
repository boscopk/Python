#pandas
import pandas as pd

tabela = pd.read_csv("Curso de python/Excel/Produtos - Sheet1.csv")

#Alteração dos valores de impostos
tabela.loc[tabela["Tipo"]=="Serviço","Multiplicador Imposto"] = 1.5
tabela.loc[tabela["Tipo"]=="Produto","Multiplicador Imposto"] = 1.1


#Atualização dos preços bases reais
tabela["Preço Base Reais"] = tabela["Preço Base Original"] * tabela["Multiplicador Imposto"]


print(tabela)