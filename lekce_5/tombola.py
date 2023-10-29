"""
V tombole bylo prodáno celkem 1000 lístků. Naším úkolem je vylosovat náhodně tři výherce. Napište program, který vygeneruje a vypíše tři čísla mezi 1 a 1000. Využijte funkci randint, nezapomeňte ale, že si ji musíte importovat z modulu random.

Neřešte, že jedno číslo může být vygenerováno dvakrát.
"""
#random - nahodny vyber
#range - rozsah
import random
for cislo_vyherce in range(1, 4):
    nahodne_cislo = random.randint(1, 1000)
    print(f"Vyherce {cislo_vyherce}: {nahodne_cislo}")

















# from random import randint
# for vyherni_cislo in range(1, 4):
#     print(f"vyherni cislo {vyherni_cislo} {randint(1, 1000)}")