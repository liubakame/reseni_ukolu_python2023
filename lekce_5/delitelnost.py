"""
Vypišme si čísla z nějakého rozsahu na základě jejich dělitelnosti dvěma čísly.

Zkuste z nějakého rozsahu čísel vypsat čísla, která jsou dělitelná 3 i 4 současně.
Zkuste z nějakého rozsahu čísel vypsat čísla, která jsou dělitelná 5 nebo 6. Stačí vypsat text: "Číslo je dělitelné 5 nebo 6."
"""
rozsah_cisel = range(1, 100)
for cislo in rozsah_cisel:
    if cislo % 3 == 0 and cislo % 4 == 0:
        print(f"{cislo} je delitelne 3 a 4")

print("je delitelne 3 a 4", [cislo for cislo in rozsah_cisel if cislo % 3 == 0 and cislo % 4 == 0])

# cisla_rozsahu = range(1, 100)
# for cislo in cisla_rozsahu:
#     if cislo % 3 == 0 and cislo % 4 == 0:
#         print("Delitelne 3 a 4", cislo)

# #print([cislo if cislo % 3 == 0 and cislo % 4 == 0 else NIC for cislo in cisla_rozsahu])
# print([cislo for cislo in cisla_rozsahu if cislo % 3 == 0 and cislo % 4 == 0 ])
        
# for cislo in cisla_rozsahu:
#     if cislo % 5 == 0 or cislo % 6 == 0:
#         print("Delitelne 5 a 6", cislo)

# print([cislo for cislo in cisla_rozsahu if cislo % 5 == 0 or cislo % 6 == 0 ])