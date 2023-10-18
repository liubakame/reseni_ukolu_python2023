"""
Napiš funkci, která bude jednoduchou simulací rulety. Budeme uvažovat pouze možnost sázení na řady. Uživatel si může vybrat jednu ze tří řad:

první řada (hodnoty 1, 4, 7 atd.),

druhá řada (hodnoty 2, 5, 8 atd.),

třetí řada (hodnoty 3, 6, 9 atd.).

Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.

Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky. Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36. Vyhodnoť, do které řady číslo náleží. Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.

Funkce roulette vrací hodnotu výhry. Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky, v opačném případě nevyhrává nic jeho sázka propadá.
"""
from random import randint
rada = int(input("Na kterou radu sazis? (1, 2, 3): "))
sazka = int(input("Kolik sazis? "))

def roulette(rada, sazka):

    # rady_cisla = {1: [] , 2: [], 3: []}
    # for cislo in range(37):
    #     if cislo == 0:
    #         continue
    #     elif cislo % 3 == 1:
    #         rady_cisla[1].append(cislo)
    #     elif cislo % 3 == 2:
    #         rady_cisla[2].append(cislo)
    #     else:
    #         rady_cisla[3].append(cislo)
            
    cislo = randint(0, 36)
    
    print("vypadlo cislo", cislo)
    if cislo == 0:
        return 0
    elif cislo % 3 == 1:
        vyhra = 1
    elif cislo % 3 == 2:
        vyhra = 2
    else:
        vyhra = 3
        
    if vyhra == rada:
        print(f"{cislo} je v rade {rada}, vyhravas. Vyhra: {sazka * 2}.")
    else:
        print(f"{cislo} neni v rade {rada}, prohravas.")
    # print(f"Rada {rada} obsahuje cisla: {rady_cisla[rada]}")

roulette(rada, sazka)