
vazeni = [
    [4, 33],
    [2, 19],
    [3, 29],
    [3, 27],
    [5, 53],
    [5, 51],
    [2, 20],
]
def spocitej_pokutu(pocet_naprav, hmotnost):
    limity = {2: 18, 3: 25, 4: 32, 5: 48}
    pokuta = 0
    max_hmotnost = limity[pocet_naprav]
    if hmotnost > max_hmotnost:
        pokuta = (hmotnost - max_hmotnost)*1000
    return pokuta

celkova_pokuta = 0
for item in vazeni:
    pokuta = spocitej_pokutu(item[0], item[1])
    print(pokuta)
    celkova_pokuta += pokuta
    
print(celkova_pokuta)
