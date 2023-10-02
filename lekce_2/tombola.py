"""
V následujícím slovníku jsou uložena čísla lístků tomboly a příslušné výhry.

tombola = {
7: "Láhev kvalitního vína Château Headache",
15: "Pytel brambor z místního družstva",
23: "Čokoládový dort",
47: "Kniha o historii města",
55: "Šiška salámu",
67: "Vyhlídkový let balónem",
79: "Moderní televizor",
91: "Roční předplatné městského zpravodaje",
93: "Společenská hra Sázky a dostihy",
}
Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku. Vstup uživatele si převeď na int!
Zkontroluj, zda je číslo lístku ve slovníku. Pokud ne, vypiš text "Bohužel nevyhráváš nic." Pokud číslo ve slovníku je, vypiš uživateli, co vyhrál.
"""

cislo_listku = int(input("Zadej číslo lístku: "))
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

if cislo_listku in tombola:
    print(f"Vyhráváš {tombola[cislo_listku]}")
else:
    print("Bohužel nevyhráváš nic.")
    
# for cislo, vyhra in tombola.items():
#     if cislo_listku == cislo:
#         print(f"Vyhráváš {vyhra}")
#         break
# else:
#     print("Bohužel nevyhráváš nic.")