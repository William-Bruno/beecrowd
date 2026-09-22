n = int(input())

for i in range(n):
    texto = list(input())
    metade = len(texto) // 2
    parte1 = texto[:metade]
    parte2 = texto[metade:]
    print("".join(parte1[::-1]+parte2[::-1]))
    
    
    

    
