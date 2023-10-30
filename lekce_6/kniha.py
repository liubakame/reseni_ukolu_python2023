"""
Zkus pro nakladatelství vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Book, která reprezentuje knihu. Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.

Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.
Přidej metodu get_time_to_read(). Metoda vrátí čas potřebný na přečtení knihy v hodinách. S využitím atributu pages vypočítej čas na přečtení knihy, přičemž uvažuj, že přečtení jedné stránky zabere průměrnému čtenáři/čtenářce 4 minuty.
"""

class Book():
    def __init__(self, title: str, pages: int, price: float):
        self.title = title
        self.pages = pages
        self.price = price
    
    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."

    def get_time_to_read(self):
        return f"Kniha {self.title} se přečte za {round(self.pages * 4 / 60)} hodin."
    
kniha_1 = Book("Harry Potter", 300, 250)
print(kniha_1.get_info())
print(kniha_1.get_time_to_read())