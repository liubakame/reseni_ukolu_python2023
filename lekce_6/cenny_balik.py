"""
Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

Vytvoř třídu ValuablePackage, která dědí od třídy Package. ValuablePackage má navíc atribut value, ostatní atributy dědí od třídy Package.
Atribut value nastav pomocí funkce __init__. Ostatní parametry předej funkci __init__ třídy Package.
Přidej do výpisu informací o cenném balíku (metoda __str__) informaci o ceně balíku.
Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí. Současně si vytvoř "obyčejný" balík o zkontroluj, že u něj se nic nezměnilo.
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

class ValuablePackage(Package):
    def __init__(self, address: str, weight: float, state: str, value: float):
        super().__init__(address, weight, state)
        self.value = value
        
    def __str__(self):
        return f"{super().__str__()} Balík má hodnotu {self.value} Kč."

balik1 = Package("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
print(balik1)

balik2 = ValuablePackage("Ortenovo Náměstí 2, Liberec", 2.5, "doručen", 125)
# print(balik2.value)
print(balik2)
