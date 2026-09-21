import sys
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    MAX = 10000000

    is_primo = bytearray([1] * (MAX +1))
    is_primo[0] = 0
    is_primo[1] = 0

    for i in range(2, int(MAX**0.5) + 1):
        if is_primo[i]:
            is_primo[i*i : MAX + 1 : i] = b'\x00' * len(is_primo[i*i:MAX+1:i])

    primos = [0] * (MAX + 1)
    qtd = 0
    for i in range(1, MAX + 1):
        if is_primo[i]:
            qtd += 1
        primos[i] = qtd

    del is_primo

    saida = []
    indice = 1
    for _ in range(n):
        a = int(input_data[indice])
        b = int(input_data[indice+1])
        indice+=2

        resposta = primos[b] - primos[a-1]
        saida.append(str(resposta))
    sys.stdout.write('\n'.join(saida) + '\n')

if __name__ == '__main__':
    main()
