"""
Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.
Příklad: Pro hodnotu 9555125899
"""

def month_of_birth(rc):
    month = int(rc[2:4])
    if month > 50:
        month -= 50
    return month

print(month_of_birth("9207054439"))