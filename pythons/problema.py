versenyzok = []
print(f"Versenyzők száma: {len(versenyzok)}")
biro = input("Bíró neve: ")
versenyzok.append(biro)

#még nem működik, mert nincs benne elem
#print(f"1. versenyző: {versenyzok[0]}")

vege = False
while not(vege):
    versenyzo = input(f"{len(versenyzok)}. versenyző neve (üres=vége): ")
    if versenyzo=="":
        vege = True
    else:
        versenyzok.append(versenyzo)
        print(versenyzok)

print(f"A bíró: {versenyzok[0]}")
print("A versenyzők: ")
szamlalo = 1
while szamlalo < len(versenyzok):
    print(f"{szamlalo:>2}. versenyző: {versenyzok[szamlalo]}")
    szamlalo += 1

print("\n")



#játékos+pontszám dictionary-vel, class-al otthonra, illetve két különböző tömbbel
#HF a pontok legyenk véletlenszerűek


#Ezt nem lehet ciklusba foglalni
nev0 = "Pálma"
nev1 = "Ede"
nev2 = "Ida"

nevek = ["Pálma", "Ede", "Ida"]
print(type(nev0))
print(type(nev1))
print(type(nev2))
print(type(nevek))

print(nevek[1])

szamlalo = 0

while szamlalo < len(nevek):
    print(f"{szamlalo:>2}: {nevek[szamlalo]}")
    szamlalo += 1

print()

nevek.append("Anna")

szamlalo = 0
while szamlalo < len(nevek):
    print(f"{szamlalo:>2}: {nevek[szamlalo]} (hossz: {len(nevek[szamlalo])})")
    szamlalo += 1

print()
szamlalo = 0
while szamlalo < len(nevek):
    nev = nevek[szamlalo]
    print(f"{szamlalo:>2}: {nevek[szamlalo]} (hossz: {len(nev)})")
    szamlalo += 1






