"""
Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

Soubor si načti do slovníku.

Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

Výsledný slovník ulož jako JSON do souboru prospech.json.
"""
import json
with open("body.json", encoding = "utf-8") as file:
    data = json.load(file)

for jmeno, body in data.items():
    if body >= 60:
        data[jmeno] = "Pass"
    else:
        data[jmeno] = "Fail"
        
with open("prospech.json", mode = "w", encoding = "utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)