import sys

for frase in sys.stdin:

    frase_final = []
    contador = 0

    for letra in frase.rstrip("\n"):
        if letra.isspace():
            frase_final.append(letra)
        else:
            if contador % 2 == 0:
                frase_final.append(letra.capitalize())
            else:
                frase_final.append(letra.lower())
            contador += 1

    print("".join(frase_final))
            






    
