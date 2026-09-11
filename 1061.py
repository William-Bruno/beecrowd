entrada_dia = int(input().split()[1])
entrada_h, entrada_m, entrada_s = map(int, input().split(":"))

saida_dia = int(input().split()[1])
saida_h,saida_m,saida_s = map(int,input().split(":"))

inicial = entrada_s + (entrada_m*60)+(entrada_h*3600)+(entrada_dia*86400)
final = saida_s + (saida_m*60)+(saida_h*3600)+(saida_dia*86400)

tempo_total = final - inicial

dia = tempo_total // 86400
tempo_total %= 86400

h = tempo_total // 3600
tempo_total %= 3600

m = tempo_total // 60
s = tempo_total % 60


print(f"{dia} dia(s)\n{h} hora(s)\n{m} minuto(s)\n{s} segundo(s)")



