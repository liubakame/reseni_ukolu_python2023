"""
Napiš funkci total_price, která vypočte cenu noci v hotelu. Funkce bude mít dva parametry - persons a breakfast. Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).
"""

def total_price(persons, breakfast = False):
    price = persons * 850
    if breakfast:
        price += persons * 125
    return price

print(total_price(3))
print(total_price(2, True))