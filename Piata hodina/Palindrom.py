def reverse_string(str):
    str1 = ""
    for i in str:
        str1 = i + str1
    return str1
def jeToPalindrom(slovo):
    otoceneslovo = slovo[::-1]
    if otoceneslovo == slovo:
        print("Slovo je palindrom")
    else:
        print("Slovo nie je palindrom")
jeToPalindrom("oko")
jeToPalindrom("radar")
jeToPalindrom("slovo")