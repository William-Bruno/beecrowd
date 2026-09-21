variaveis = list(range(16))

octal = [f"{n:o}" for n in variaveis]

hexa = [f"{n:X}" for n in variaveis]

borda = "-" * 39

cabecalho = "|" + " decimal " + "|" + " octal " + "|" + " Hexadecimal " + "|"

print(borda)
print(cabecalho)
print(borda)

for valor in variaveis:

    linha = "|" + f"{valor:8d}" + "    |" + f"{octal[valor]:7s}" + "   |" + f"{hexa[valor]:^14}" + "|"

    print(linha)

print(borda)