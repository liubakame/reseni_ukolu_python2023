"""Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.

Zadej slovo: ahoj
********
* ahoj *
********
Nápověda: 8 * '*' == '********'

Bonus: Znak, kterým se má text obalit, bude zadán také jako parametr.
"""

def ramecek(text, znak):
    print((len(text) + 4) * znak)
    print(znak, text, znak)
    print((len(text) + 4) * znak)
    
ramecek("Liuba Kameneva", "*")