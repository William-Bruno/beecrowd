CONSOANTES = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'
VOGAIS = 'AaEeIiOoUu'

n = int(input())

for teste in range(n):

    nome = str(input())

    contador = 0

    for i,letra in enumerate(nome):
        for consoante in CONSOANTES:
            if letra == consoante:
                contador += 1
            for vogal in VOGAIS:
                if letra == vogal:
                    if contador >= 3:
                        break
                    else:
                        contador = 0

    if contador>2:
        print(f"{nome} nao eh facil")
        
    else:
        print(f"{nome} eh facil")

