n = int(input())

for m in range(n):
    string1, string2 = map(str, input().split(" "))

    string_completa = ""

    tamanho = max(len(string1), len(string2))

    for i in range(tamanho):
        if i < len(string1) and i < len(string2):
            string_completa += string1[i] + string2[i]
        elif i < len(string1):
            string_completa += string1[i]
        else:
            string_completa += string2[i]


    print(string_completa)
