# Lajota tem 1 metro de diagonal e não de lado
# se 3 largura e 5 de comprimento = 23 lajotas inteiras, logo 1 lajota inteira é 0.65

largura = int(input())
comprimento = int(input())

lajotaInteira = 0.51
lajotaMetade = 0.255
lajotaQuarto = 0.127

area = (largura * comprimento) - (lajotaQuarto * 4)
qtdLajotaInteira = int(area // lajotaInteira)
areaLajotasInteiras = qtdLajotaInteira * lajotaInteira
areaRestante = area - areaLajotasInteiras
print(areaLajotasInteiras, areaRestante)
qtdLajotaMetade = areaRestante // lajotaMetade

print(qtdLajotaInteira)
print(qtdLajotaMetade)