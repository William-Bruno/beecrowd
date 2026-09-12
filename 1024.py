import sys

input = sys.stdin.readline


n = int(input())

for i in range(n):
    senha = list(input().strip('\n'))

    for j in range(len(senha)):
        if senha[j].isalpha():
            senha[j] = chr(ord(senha[j]) + 3)
    senha.reverse()
    metade = len(senha) // 2
    for r in range(metade, len(senha)):
        senha[r] = chr(ord(senha[r]) - 1)

    senha = "".join(senha)
    print(senha)

        
