"""
Mějme zadaný následující seznam

jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
Vytvořte seznam, který obsahuje

počty písmen ve všech jménech,
všechna jména napsaná velkými písmeny,
všechna jména plus písmeno 'a' na konci (stanou se z nich tedy ženská jména),
všechna jména převedená na malá písmena s koncovkou '@email.cz'.
"""
jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']
# počty písmen ve všech jménech,
pocty_pismen = [len(jmeno) for jmeno in jmena]
print(pocty_pismen)
# všechna jména napsaná velkými písmeny,
jmena_velkymi_pismeny = [jmeno.upper() for jmeno in jmena]
print(jmena_velkymi_pismeny)
# všechna jména plus písmeno 'a' na konci (stanou se z nich tedy ženská jména),
zenska_jmena = [jmeno + 'a' for jmeno in jmena]
print(zenska_jmena)
# všechna jména převedená na malá písmena s koncovkou '@email.cz'.
emaily = [jmeno.lower() + '@email.cz' for jmeno in jmena]
print(emaily)