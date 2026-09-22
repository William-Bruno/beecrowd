total = int(input())
compradas = int(input())

figurinhas = list(range(1, total+1))
faltantes = []

for i in range(compradas):
    m = int(input())
    faltantes.append(m)

comuns = [el for el in figurinhas if el in faltantes]

print(total-len(comuns))
