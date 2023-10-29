"""
Mějme zadaný následující seznam

cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
Vytvořte seznam, který obsahuje

každé z čísel ze seznamu cisla vynásobené dvěma,
každé z čísel ze seznamu cisla s opačným znaménkem,
každé z čísel ze seznamu cisla umocněné na druhou,
každé z čísel ze seznamu cisla jako řetězec.
"""

cisla = [1.12, 4.51, 2.64, 13.1, 0.1]
#každé z čísel ze seznamu cisla vynásobené dvěma,
cisla_vynasobena_dvema = [cislo * 2 for cislo in cisla]
print(cisla_vynasobena_dvema)
# každé z čísel ze seznamu cisla s opačným znaménkem,
cisla_s_opacnym_znamenkem = [- cislo for cislo in cisla]
print(cisla_s_opacnym_znamenkem)
# každé z čísel ze seznamu cisla umocněné na druhou,
cisla_umocnena_na_druhou = [cislo ** 2 for cislo in cisla] 
print(cisla_umocnena_na_druhou)
# každé z čísel ze seznamu cisla jako řetězec.
cisla_jako_retezec = [str(cislo) for cislo in cisla]
print(cisla_jako_retezec)

