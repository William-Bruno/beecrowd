borda = "-" * 39
meio = "|" + " " * 37 + "|"
condicao1 = "|"+ " " * 8 + "R"+"o"+"b"+"e"+"r"+"t"+"o"+" "* 22 + "|"
condicao2 = "|"+ " " * 8 + "5"+"7"+"8"+"6"+" "* 25 + "|"
condicao3= "|"+ " " * 8 + "U"+"N"+"I"+"F"+"E"+"I"+" " * 23 + "|"
tela = [borda] + [condicao1] + [meio] +[condicao2] +[meio]+ [condicao3] + [borda]

# Imprime cada linha da lista
for linha in tela:
    print(linha)