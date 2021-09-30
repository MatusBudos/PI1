username = input("Zadaj prihlasovacie meno")
password = input("Zadaj prihlasovacie heslo")
vek = input("Zadaj svoj vek")

if username == ("root") and password == ("password") and vek == ("18"):
    print("Úspešne si sa prihlásil")
else:
    print(" zlé meno alebo heslo alebo vek")