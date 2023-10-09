"""
Jak už jsme si ověřili v lekci, datové API na adrese https://api.kodim.cz/python-data/people obsahuje seznam lidí. Napište program, který tento seznam z API stáhne a převede z formátu JSON na Python slovníky. Proveďte následující úkoly.

Zjistěte kolik lidí celkem seznam obsahuje.
Zjistěte jaké všechny informace máme o jednotlivých osobách.
Zjistěte, kolik je v souboru mužů a žen.
"""

import requests

response = requests.get('https://api.kodim.cz/python-data/people')
data = response.json()
# Zjistěte kolik lidí celkem seznam obsahuje.
print(len(data))
# Zjistěte jaké všechny informace máme o jednotlivých osobách.
print(data[0].keys())
# Zjistěte, kolik je v souboru mužů a žen.
pocet_zen = 0
pocet_muzu = 0
for item in data:
    if item["gender"]=="Female":
        pocet_zen+=1
    # else:
    #     pocet_muzu+=1
pocet_muzu = len(data) - pocet_zen
print(pocet_zen, "žen")
print(pocet_muzu, "mužů")