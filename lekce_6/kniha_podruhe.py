"""
U knihy budeme chtít evidovat, kolik kusů bylo prodáno. Přidej atribut sold, jehož hodnotu bude možné nastavit v metodě __init__(). Dále přidej atribut costs, které představují náklady na jednu knihu (např. tisk, doprava do knihkupectví, podíl autora(autorky) atd.).
Přidej metodu profit(), která vrátí celkový zisk z knihy. Zisk vypočti na základě vzorce: prodané kusy * (cena - náklady).
Přidej metodu rating(), která vrátí hodnocení knihy na základě jejího zisku. Pokud bude zisk méně než 50 tisíc, vrať hodnotu "propadák". Pokud bude zisk mezi 50 tisíc a 500 tisíc, vrať hodnotu "průměr". Pokud bude vyšší než 500 tisíc, vrať hodnotu "úspěch".
"""

class Book():
    def __init__(self, title: str, pages: int, price: float, sold: int, costs: float):
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs
    
    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."

    def get_time_to_read(self):
        return f"Kniha {self.title} se přečte za {round(self.pages * 4 / 60)} hodin."
    
    def profit(self):
        return self.sold * (self.price - self.costs)
    
    def rating(self):
        if self.profit() < 50000:
            return "propadák"
        elif self.profit() < 500000:
            return "průměr"
        else:
            return "úspěch"
    
kniha_1 = Book("Harry Potter", 300, 250, 1000, 100)
print(kniha_1.get_info())
print(kniha_1.get_time_to_read())
print(kniha_1.rating())
print(kniha_1.profit())