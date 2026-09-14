linhas = 7
colunas = 39
tabela = [["" for _ in range(colunas)] for _ in range(linhas)]

for i in range(linhas):
    for j in range(colunas):
        if i == 0 or i == 6:
            tabela[i][j] =  "-"
        else:
            if j == 0 or j == 38:
                tabela[i][j] = "|"
            else:
                tabela[i][j] = " "
    
for linha in tabela:
    print("".join(linha))
    
