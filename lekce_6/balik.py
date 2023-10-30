"""
Uvažuj, že navrhuješ software pro zásilkovou společnost.

Vytvoř třídu Package, která bude mít tři atributy - address, weight a state. Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.
Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. Uvažuj například větu "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".
Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.
"""
class Package:
    
    def __init__(self, address: str, weight: float, state: str):
        self.address = address
        self.weight = weight
        self.state = state
        
    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self.state}."

    
balik1 = Package("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
print(balik1.get_info())

balik2 = Package("Ortenovo Náměstí 9, Liberec", 2.5, "doručen")
print(balik2.get_info())