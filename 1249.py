borda = "-" * 39
meio = "|" + " " * 37 + "|"
condicao1 = "|"+ "x = 35"+" "*31+"|"
condicao2 = "|"+ " " * 15 + "x = 35"+ " "* 16 + "|"
condicao3= "|"+ " " * 31 + "x = 35"+"|"
tela = [borda] + [condicao1] + [meio] +[condicao2] +[meio]+ [condicao3] + [borda]

# Imprime cada linha da lista
for linha in tela:
    print(linha)