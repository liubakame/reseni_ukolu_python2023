"""
Stáhněte si soubor kurz.json s výše uvedeným obsahem a načtěte jej v Pythonu do proměnné kurz. Odpovězte na následující otázky:

Vypište na výstup počet účastnic na posledním konání kurzu.
Vypište na výstup jméno posledního kouče na prvním konání kurzu.
Vypište na výstup celkový počet konání kurzu.
Vypište na výstup všechna místa, na kterých se kurz konal.
Vypište na výstup součet všech účastnic.
Vypište na výstup množinu všech koučů, kteří se kdy kurzu účastnili.
"""
import json
with open("kurz.json", encoding="utf-8") as f:
    kurz = json.load(f)
#Vypište na výstup počet účastnic na posledním konání kurzu.    
print(kurz["konani"][-1]["ucastnic"])
# Vypište na výstup jméno posledního kouče na prvním konání kurzu.
print(kurz["konani"][0]["koucove"][-1])
# Vypište na výstup celkový počet konání kurzu.
print(len(kurz["konani"]))
# Vypište na výstup všechna místa, na kterých se kurz konal.
mista = []
for konani in kurz["konani"]:
    mista.append(konani["misto"])
print(", ".join(mista))
# Vypište na výstup součet všech účastnic.
pocet_ucastnic = 0
for konani in kurz["konani"]:
    pocet_ucastnic += konani["ucastnic"]
print(pocet_ucastnic)
# Vypište na výstup množinu všech koučů, kteří se kdy kurzu účastnili.
seznam_koucu = []
for konani in kurz["konani"]:
    seznam_koucu.extend(konani["koucove"])        
print(", ".join(set(seznam_koucu)))