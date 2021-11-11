
zoznam_cisel = [10,9,8,7,6,5,4,3,2,1]
for cisla in zoznam_cisel:
    print(cisla)
print("-----------")

zoznam_ovocia = ["jablko", "banan", "hruska", "jahoda", "malina", "pomaranc", "mandarinka", "ceresna", "hrozno",
                 "citron"]
zoznam_zeleniny = ["brokolica","mrkva","petrzlen","kalerab"]
while(True):
        zadaj = input("Zadaj nazov ovocia alebo zeleniny")
        if zadaj in zoznam_ovocia:
            print("Zadal si ovocie")
        elif zadaj in zoznam_zeleniny:
            print("Zadal si zeleninu")
        else:
            print("Zadal si nieco ine")


