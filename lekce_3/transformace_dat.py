"""
Stáhněte si soubor words.txt a zpracujte z něj výstupní soubor ve formátu JSON obsahující slovník. Klíče budou písmena a hodnoty seznamy slov, které začínají písmenem v klíči. Pokud na nějaké písmeno žádná slova nezačínají, tak ve výstupu toto písmeno nebude. Seřaďte tyto seznamy podle abecedy. Zajistěte, aby i klíče ve výstupním JSON souboru byly seřazeny a data byla odsazena čtyřmi mezerami pro lepší čitelnost člověkem.

Vzorový výstup: output.json.
"""
import json
with open("words.txt", encoding="utf-8") as file:
    words = file.read().splitlines()

# words = words.split()
output = {}

for word in words:
    if word[0] not in output:
        output[word[0]] = []
    output[word[0]].append(word)
    
for value in output.values():
    value.sort()

with open("output.json", "w", encoding="utf-8") as file:
    json.dump(output, file, indent=4, sort_keys=True, ensure_ascii=False)