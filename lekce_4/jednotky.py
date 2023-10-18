"""
Převod kilometrů na míle a zpět
Napište dvě funkce: kilometry_na_mile(kilometry) a mily_na_kilometry(mile), které provedou převod mezi kilometry a mílemi.

Převod metrů na stopy a zpět
Napište funkce: metry_na_stopy(metry) a stopy_na_metry(stopy), které umožňují převod mezi metry a stopami.

Převod centimetrů na palce a zpět
Vytvořte dvě funkce: centimetry_na_palec(centimetry) a palce_na_centimetry(palce), které umožní převod mezi centimetry a palci.

Převod hmotnosti kilogramů na libry a zpět
Napište funkce: kilogramy_na_libry(kilogramy) a libry_na_kilogramy(libry), které provedou převod mezi kilogramy a librami.

Převod objemu litrů na galony a zpět
Vytvořte dvě funkce: litry_na_galony(litry) a galony_na_litry(galony), které umožní převod mezi litry a galony.

Převod rychlosti kilometrů za hodinu na míle za hodinu a zpět
Napište funkce: kmh_na_mph(kmh) a mph_na_kmh(mph), které umožní převod rychlosti mezi kilometry za hodinu a míli za hodinu.

Převod teploty ze stupňů Celsia na Fahrenheit a zpět
Vytvořte dvě funkce: celsia_na_fahrenheit(teplota) a fahrenheit_na_celsia(teplota), které umožňují převod teploty mezi stupni Celsia a stupni Fahrenheit.
"""
def kilometry_na_mile(kilometry):
    return kilometry * 0.621371

def mily_na_kilometry(mile):
    return mile * 1.60934

def metry_na_stopy(metry):
    return metry * 3.28084

def stopy_na_metry(stopy):
    return stopy * 0.3048

def centimetry_na_palec(centimetry):
    return centimetry * 0.393701

def palce_na_centimetry(palce):
    return palce * 2.54

def kilogramy_na_libry(kilogramy):
    return kilogramy * 2.20462

def libry_na_kilogramy(libry):
    return libry * 0.453592

def litry_na_galony(litry):
    """
    US liquid gallon
    """
    return litry * 0.264172

def galony_na_litry(galony):
    return galony * 3.78541

def kmh_na_mph(kmh):
    return kmh * 1.609344

def mph_na_kmh(mph):
    return mph * 1.60934

def celsia_na_fahrenheit(teplota):
    return teplota * 1.8 + 32

def fahrenheit_na_celsia(teplota):
    return (teplota - 32) / 1.8

print("kilometry na mile: ", kilometry_na_mile(10))
print("mily na kilometry: ", mily_na_kilometry(10))
print("metry na stopy: ", metry_na_stopy(10))
print("stopy na metry: ", stopy_na_metry(10))
print("centimetry na palec: ", centimetry_na_palec(10))
print("palce na centimetry: ", palce_na_centimetry(10))
print("kilogramy na libry: ", kilogramy_na_libry(10))
print("libry na kilogramy: ", libry_na_kilogramy(10))
print("litry na galony: ", litry_na_galony(10))
print("galony na litry: ", galony_na_litry(10))
print("kmh na mph: ", kmh_na_mph(10))
print("mph na kmh: ", mph_na_kmh(10))
print("celsia na fahrenheit: ", celsia_na_fahrenheit(10))
print("fahrenheit na celsia: ", fahrenheit_na_celsia(10))


