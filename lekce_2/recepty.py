"""
Uložte si tuto strukturu do proměnné recept na začátek nového programu. Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru.
"""
recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

cena_jidla = 0
for ingredient in recept["ingredience"]:
    cena_jidla += float(ingredient[2].split()[0])# * float(ingredient[1]) kdybychom chteli vypocitat cenu jidla podle mnozstvi
# import ceil
# print(f"Cena jídla je {ceil(cena_jidla)} Kč.") 
print(f"Cena jídla je {round(cena_jidla)} Kč.") 