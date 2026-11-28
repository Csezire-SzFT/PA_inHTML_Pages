def kerites(jel, ismetles):
    szoveg = ""
    szamlalo = 0
    while szamlalo < ismetles:
        szoveg += jel
        szamlalo += 1
    return szoveg

def masik_kerites(jel, ismetles):
    szoveg = ""
    szamlalo = 0
    while szamlalo < ismetles*2:
        szoveg += jel[szamlalo % 2]
        szamlalo += 1
    return szoveg

def harmadikkerites(jel, ismetles):
    szoveg = ""
    while len(szoveg) < ismetles*2:
        szoveg += jel
    return szoveg


print(kerites("X_", 3), "\n")
print(kerites("X_", 8), "\n")
print(masik_kerites(["X", "_"], 3.5))
print(masik_kerites(["X", "_"], 8.5))

print(kerites("X_", 3),kerites("O", 3), sep="")
print(kerites("X_", 3),kerites("O", 50), sep="")

print(harmadikkerites("X_", 3))
print("")

szamlalo = 1
vege = -1
lepes = -1
while szamlalo >= vege:
    print(f"|{szamlalo:>3}| = {abs(szamlalo):>3}")
    szamlalo += lepes

print("\n")

szamlalo = 0
vege = 2
lepes = 1
while szamlalo <= vege:
    print(f"|{1-szamlalo:>3}| = {abs(1-szamlalo):>3}")
    szamlalo += lepes


print("\n")
print("X_"*3, "\n")

