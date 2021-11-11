zoznam_prazdny =[]
zoznam_cisel =[1,5,8,9,7,15]
zoznam_pismen =["a","t","b"]
zoznam_mix =["slovo", 14, "a","@",55]

zoznam_cisel[0] = 9999
print(zoznam_cisel[4])
print(zoznam_mix[-1])
print(zoznam_pismen[2])

print("------------")
print(zoznam_cisel)
print(zoznam_mix)
print(zoznam_pismen)

zoznam = list()
print(zoznam)
zoznam_range = list(range(3,7))
print(zoznam_range)
print("---------")
#Orezavanie zoznamu#
neorezany_zoznam = list(range(10))
print(neorezany_zoznam)

print(neorezany_zoznam[0:5])
print(neorezany_zoznam[2:8])
print(neorezany_zoznam[1:7:2])
print(neorezany_zoznam[2:9:3])

print("---------------")
#Velkost zoznamu#
x = [5,8,1,3,"slovo"]
print(len(x))
print("-----------")

#Prechadzanie zoznamu#
#1.
zoznam_prvkov = ["jablko","hruska","banan","jahoda"]
for prvok in zoznam_prvkov:
    print(prvok)
#2.
for index in range(len(zoznam_prvkov)):
    print(zoznam_prvkov[index])
print("-------------")
#Metody pre zoznamy#
mojZoznam = [1,5,8,55,500]
#append- prida nakoniec novy prvok
mojZoznam.append(99)
print(mojZoznam)
#pop
mojZoznam.pop()
print(mojZoznam)
print("--------")
#Funkcie pre zoznamy
#len
#min/max
mojZoznam2 = [1,5,65,7,52,-16]
print("minimum",min(mojZoznam2))
print("maximum",max(mojZoznam2))
print("suma",sum(mojZoznam2))


print(mojZoznam2)
print(sorted(mojZoznam2))