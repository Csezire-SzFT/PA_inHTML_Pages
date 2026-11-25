import random

def tabla_rajzol (harcos_pozicio, varazslo_pozicio):
    elvalaszto = "-"
    tabla = ""
    if harcos_pozicio < varazslo_pozicio:
        tabla = "H" + elvalaszto * (varazslo_pozicio - harcos_pozicio - 1) + "V" + elvalaszto * (3 - varazslo_pozicio)
    if harcos_pozicio > varazslo_pozicio:
        tabla = "V" + elvalaszto * (harcos_pozicio - varazslo_pozicio - 1) + "H" + elvalaszto * (3 - harcos_pozicio)
    if harcos_pozicio == varazslo_pozicio:
        harc_pozicio = harcos_pozicio
        tabla = elvalaszto * (harc_pozicio - 1) + "*" + elvalaszto * (3 - harc_pozicio ) + " Harc!!! "
    else:
        if min(harcos_pozicio, varazslo_pozicio) > 1:
            tabla = elvalaszto + tabla
    return tabla

harcos_pozicio_aktualis = 1
harcos_sorrend = 0
harcos_HP = 9
varazslo_pozicio_aktualis = 3
varazslo_sorrend = 0
varazslo_HP = 9

print(tabla_rajzol(harcos_pozicio_aktualis, varazslo_pozicio_aktualis), f"(Harcos HP: {harcos_HP}), (varazslo HP: {varazslo_HP})")

while (harcos_HP>0) and (varazslo_HP>0):
    harcos_pozicio_aktualis = random.randint(1,3)
    varazslo_pozicio_aktualis = random.randint(1,3)
    if harcos_pozicio_aktualis == varazslo_pozicio_aktualis:
        harcos_sorrend = random.randint(1,6)
        varazslo_sorrend = random.randint(1,6)
        if harcos_sorrend < varazslo_sorrend:
            varazslo_HP -= random.randint(1,6)
        elif harcos_sorrend > varazslo_sorrend:
            harcos_HP -= random.randint(1,6)
        else:
            varazslo_HP -= random.randint(1, 6)
            harcos_HP -= random.randint(1, 6)
    print(tabla_rajzol(harcos_pozicio_aktualis, varazslo_pozicio_aktualis), f"(Harcos HP: {harcos_HP}), (varazslo HP: {varazslo_HP})")

if harcos_HP <= 0:
    print(f"A varázsló nyert!!! HP: {varazslo_HP}")
else:
    print(f"A harcos nyert!!! HP: {harcos_HP}")
print("A program vége...")