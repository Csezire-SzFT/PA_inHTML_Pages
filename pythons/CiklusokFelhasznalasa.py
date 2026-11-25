import random

i = 3 #kezdet
while i <= 9:
    print(i, end=" ")
    i += 3 #léptetés
print("\nCiklus vége...") # \n = sortörés, azaz ENTER

print("X" * 3)

# "X__" kiírása
i = 1
while i <= 3:
    if i == 1:
        print("X", end="")
    else:
        print("_", end="")
    i += 1
print("\n")

i = 1
while i <= 3:
    if i == 2:
        print("X", end="")
    else:
        print("_", end="")
    i += 1
print("\n")

i = 1
while i <= 3:
    if i == 3:
        print("X", end="")
    else:
        print("_", end="")
    i += 1
print("\n")


def amobaegysora (X_poz, O_poz, hossz):
    szoveg = ""
    i = 1
    if X_poz != O_poz:
        while i <= hossz:
            karakter = "-"
            if i == X_poz:
                karakter = "X"
            if i == O_poz:
                karakter = "O"
            szoveg += karakter
            i += 1
    return szoveg

sor = 1
while sor <= 5:
    kiiras = amobaegysora(random.randint(1,5),random.randint(1,5),5)
    if kiiras != "":
        print(kiiras)
        sor += 1
