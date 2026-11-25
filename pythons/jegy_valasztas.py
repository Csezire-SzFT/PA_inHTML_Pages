def get_int(prompt):
    while True:
        valasz = input (prompt)
        if valasz.isdigit():
            return int(valasz)
        else:
            print ("Pozitív egész számot kérek megadni!")

def igennem (prompt):
    while True:
        valasz = input (prompt)
        if (valasz == "igen") or (valasz == "nem"):
            return valasz
        else:
            print ("A válasz igen vagy nem lehet.")

def jegy_valasztas(nev, kor, hetvege, diakigazolvany):
    szoveg = nev
    if kor < 18:
        if (hetvege == "igen") and (diakigazolvany =="igen"):
            szoveg += ": kedvezményes jegy."
        else:
            szoveg += ": normál jegy."
    else:
        szoveg += ": felnőtt jegy."
    return szoveg



diak_nev = input("Kérem a diák nevét: ")
diak_kor = get_int("Kérem a diák korát: ")
diak_diakigazolvany = igennem("Van diákigazolványa (igen/nem): ")
diak_hetvege = igennem("Hétvége van (igen/nem): ")

print(jegy_valasztas(diak_nev, diak_kor, diak_hetvege, diak_diakigazolvany))

print ("Program vége...")








