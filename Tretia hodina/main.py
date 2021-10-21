samohlasky = "aáeéiíoóuúůyý"
spoluhlasky = "bcdfghjklmnpqrstvwxz"
cisla = "0123456789"
slovo = input("Zadaj slovo")
pocet_samohlasok = 0
pocet_ostatnych = 0
pocet_cisel = 0
pocet_spoluhlasok = 0
for znak in slovo:
    if znak in samohlasky:
        pocet_samohlasok += 1
    elif znak in cisla:
        pocet_cisel += 1
    elif znak in spoluhlasky:
        pocet_spoluhlasok += 1
    else:
        pocet_ostatnych += 1
print("Pocet ostatnych",pocet_ostatnych)
print("Pocet cisel", pocet_cisel)
print("Pocet spoluhlasok", pocet_spoluhlasok)
print("Slovo obsahuje samohlasky", pocet_samohlasok)

riadky = int(input("Zadaj pocet riadkov"))
stlpce = int(input("Zadaj pocet stlpcov"))

for i in range(0,stlpce):
    for j in range(0,riadky):
        print("*", end = "")
        print()

