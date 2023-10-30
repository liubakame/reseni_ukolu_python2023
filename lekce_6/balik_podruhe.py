"""
Vrať se k návrhu software pro zásilkovou společnost.

U třídy Package přejmenuj metodu get_info() na __str__() a vyzkoušej, jestli nyní stačí k získání informací o balíku funkce print().
Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku a zaznamená tak jeho doručení. Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen. Pokud ano, metoda vrátí zprávu "Balík již byl doručen". Tím bude řidič (řidička) informován(a) o tom, že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku. Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo".
Vyzkoušej metodu deliver(). Co se stane, pokud ji u jednoho balíku zavoláš dvakrát?
"""
class Package:
    def __init__(self, address: str, weight: float, state: str):
        self.address = address
        self.weight = weight
        self.state = state
        
    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}."
    
    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen."
        else:
            self.state = "doručen"
            return "Doručení uloženo."

balik1 = Package("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
print(balik1)

balik2 = Package("Ortenovo Náměstí 2, Liberec", 2.5, "doručen")
print(balik2)
print(balik2.deliver())
# print(balik1.deliver())
print(balik2)
