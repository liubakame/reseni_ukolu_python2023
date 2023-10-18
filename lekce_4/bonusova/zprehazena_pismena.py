text = """Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena. Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci, která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny znaky kromě prvního a posledního.

Nápověda: random.shuffle()

Super bonus: Napiš program, který takovou funkci využije na delší text více slov.
"""

import random

def suffle_word(word):
    mid_str = word[1:-1]
    mid_list = list(mid_str)
    suffle_list = random.shuffle(mid_list)
    suffle_str = "".join(mid_list)    
   
    return word[0] + suffle_str + word[-1]

def suffle_text(text):
    text_list = text.split()
    for word in text_list:
        if len(word) > 1:
            print(suffle_word(word), end=" ")
        else:
            print(word, end=" ")

print(suffle_word("text"))
suffle_text(text)