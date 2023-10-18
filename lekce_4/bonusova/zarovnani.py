"""
Vypište seznam čísel každé na nový řádek zarovnané vpravo na délku nejdelšího čísla.
"""
numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
nejvetsi_cislo = max(numbers)
delka_max_cisla = len(str(nejvetsi_cislo))

def serad_cisla(seznam_cisel, delka_max_cisla, znak = " "):
    for cislo in seznam_cisel:
        delka_cisla = len(str(cislo))
        pocet_znaku = delka_max_cisla - delka_cisla
        print(f"{znak*pocet_znaku}{cislo}")
        
serad_cisla(numbers, delka_max_cisla, ".")