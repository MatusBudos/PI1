"""
class Person:
    def __init__(self, name):
        self.name = name
        self.fatigue = 0
        self.fatigue_limit = 20

    def run(self, km):
        if km > self.fatigue_limit - self.fatigue:
            print("Si moc unavený, nemôžeš utekať")
            return
        self.fatigue += km
        print(self)
    def sleep(self, hours):
        self.fatigue -= hours * 10

        if self.fatigue < 0:
            self.fatigue = 0
        print(self)
    def __str__(self):
        return self.name + "Má únavu: " + str(self.fatigue)

person = Person("Roman")

person.run(3)
person.run(3)
person.run(3)
person.run(3)
person.run(3)
person.sleep(1)


import random
class Generator:

    def __init__(self):
        self.vlastnosti = ["Chudý", "Vysoký", "Múdry", "Modrý", "Malý"]
        self.povolanie = ["programátor", "manažér", "predavač", "T-rex", "učiteľ"]
        self.prislovka = ["veľmi", "rýchlo", "rád", "pomaly", "naporiadok"]
        self.sloveso = ["behal", "varil", "piekol", "kosil", "robil"]
        self.predložka = ["v", "u", "pod"]
        self.miesto = ["práci", "babky", "doma", "lese", "stromom"]
        self.veta = ["", "", "", "", ""]

    def vlastnost(self):
         self.veta[0] = random.choice(self.vlastnosti)
         self.veta[1] = random.choice(self.povolanie)
         self.veta[2] = random.choice(self.prislovka)
         self.veta[3] = random.choice(self.sloveso)
         self.veta[4] = random.choice(self.predložka)
         self.veta[5] = random.choice(self.miesto)
         print.self


generator = Generator()


class Garaz:
    def __init__(self, zaparkovane_auta):
        self.zaparkovane_auta = []
        print.self



class Auto:
    def __init__(self, spz, farba):
        self.farba = farba
        self.spz = spz

    def zaparkuj(self, garaz):
        self.garaz = garaz
        print.self



Auto.zaparkuj

auto = Auto("AAA123", "Modrá")
garaz = Garaz(auto)

print(garaz)



"""


class Garaz():
    auta_v_garazi = []

    def vypisanie_aut(self):
        if self.auta_v_garazi ==  []:
            print("Vgaráži nič nie je")
        else:
            print("V garáži sú autá: {}".format(", ".join(self.auta_v_garazi)))

class Auto():
    def __init__(self , spz, farba):
        self.spz = spz
        self.farba = farba

    def zaparkuj(self, garaz):
        garaz.auta_v_garazi.append("{0} {1}".format(self.spz, self.farba))

    def vyparkuj(self, garaz):
        garaz.auta_v_garazi.remove("{0} {1}".format(self.spz, self.farba))

garaz = Garaz()
bmw = Auto("123ABC", "modré")
bmw.zaparkuj(garaz)
audi = Auto("987POI", "zelené")
audi.zaparkuj(garaz)
renault = Auto ("456LAM", "žlté")
renault.zaparkuj(garaz)
renault.vyparkuj(garaz)
garaz.vypisanie_aut()












