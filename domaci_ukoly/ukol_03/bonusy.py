"""
Krom souboru s body si ulož a načti do druhého slovníku ještě soubor bonusy.json. Obsahuje bonusové body získané během semestru. Pozor, bonusové body získali jen někteří žáci.

Tvým úkolem je žákům přiřadit známky na základě součtu bodů z písemky a bonusových bodů. Bodová rozhraní (vztahují se na součet) najdeš zde:

1: 90 a více
2: 70-89
3: 50-69
4: 30-49
5: 29 a méně

Výsledný slovník ulož jako JSON do souboru znamky.json.
"""
import json
with open("body.json", encoding = "utf-8") as file:
    body = json.load(file)

with open("bonusy.json", encoding = "utf-8") as file:
    bonusy = json.load(file)
    
znamky = {}

for jmeno, body in body.items():
    bonus = 0
    if jmeno in bonusy:
        bonus = bonusy[jmeno]
    body += bonus
    if body >= 90:
        znamka = 1
    elif body >= 70:
        znamka = 2
    elif body >= 50:
        znamka = 3
    elif body >= 30:
        znamka = 4
    else:
        znamka = 5
    znamky[jmeno] = znamka
    
with open("znamky.json", mode = "w", encoding = "utf-8") as file:
    json.dump(znamky, file, ensure_ascii=False, indent=4)