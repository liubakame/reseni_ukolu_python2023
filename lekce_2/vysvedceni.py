"""
Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka z daného předmětu. Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis). Vypiš obsah slovníku pomocí funkce print().
"""
vysvedceni = {"český jazyk": 1, "matematika": 2, "dějepis": 3}
print(vysvedceni)
print("vysvědčení:")
for predmet, znamka in vysvedceni.items():
    print(f"{predmet}: {znamka}")