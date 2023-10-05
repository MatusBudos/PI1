import random
teploty = []
pocetDni = input("Zadaj počet dní: ")
for i in range(int(pocetDni)):
    teplota =random.randint(-25,30)
    teploty.append(teplota)
for i in range(int(pocetDni)):
    print("V " + str(i+1) + ". deň bolo " + str(teploty[i]) + " stupňov.")
sucetTeplot = sum(teploty)
priemerTeplot = int(sucetTeplot)/int(pocetDni)
najvyssia = max(teploty)
najnizsia = min(teploty)
print("Priemer teplôt bol " + str(priemerTeplot) + " stupňov.")
print("Najmenej bolo " + str(najnizsia) + " stupňov.")
print("Najviac bolo " + str(najvyssia) + " stupňov.")