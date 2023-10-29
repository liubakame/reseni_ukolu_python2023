"""
Popište vlastními slovy co následující výrazy udělají se zadaným seznamem seznam. Až když máte ve svojí hlavjénce jasno, tak je zkuste napsat do Python konzole a ověřte, zda jste měli pravdu.
"""

seznam = [1, 4, 9, 16, 25, 36, 49, 64]
[x**0.5 for x in seznam]
[x % 2 for x in seznam]
[[x // 2, x % 2] for x in seznam]


















# definujeme promennou seznam, ktera obsahuje seznam cisel
seznam = [1, 4, 9, 16, 25, 36, 49, 64]
# druha odmocnina kazdeho cisla v seznamu, treba ze 4 ma vyjit 2
[x**0.5 for x in seznam]
# zustatek po deleni kazdeho cisla v seznamu dvema
[x % 2 for x in seznam] # u sudych = 0, u lichych = 1, vysledek 1,0,1,0,1,0,1,0
# dvojice cisel, kde prvni cislo je vysledek deleni cisla dvema a druhe cislo je zbytek po deleni dvema, treba u 4 to bude 2,0
[[x // 2, x % 2] for x in seznam]

seznam = ['12.03.2014', '10.01.2015', '06.06.1986']
# pro kazdy datum vrati mesic
[int(datum[3:5]) for datum in seznam]
# pro kazdy datum odecte 1 ode dne, treba 12.03.2014 bude 11
[int(datum[:2])-1 for datum in seznam]
# pro kazdy datum vrati seznam oddelenych den, mesic, rok
[[int(datum[:2]), int(datum[3:5]), int(datum[6:])] for datum in seznam]
# totez jen pomoci split
[datum.split('.') for datum in seznam]
#preformatuje datumy do formatu 12/03/2014
['/'.join(datum.split('.')) for datum in seznam]

