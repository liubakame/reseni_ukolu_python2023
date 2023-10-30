"""
Vrať se k návrhu software pro zásilkovou společnost. U třídy Package uprav atribut state tak, aby byl chráněný. Ověř, že vytváření objektů i výpisy informací o něm fungují.
"""
class Package:
    def __init__(self, address: str, weight: float, state: str):
        self.address = address
        self.weight = weight
        self._state = state
        
    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg je ve stavu {self._state}."
    
    def deliver(self):
        if self._state == "doručen":
            return "Balík již byl doručen."
        else:
            self._state = "doručen"
            return "Doručení uloženo."
    
balik1 = Package("Václavské Náměstí 12, Praha", 0.25, "nedoručen")
print(balik1)

balik2 = Package("Ortenovo Náměstí 2, Liberec", 2.5, "doručen")
print(balik2)
print(balik2.deliver())
print(balik1.deliver())
print(balik1)
