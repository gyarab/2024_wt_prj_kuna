import httpx

print("Zde ti prevedu meny")

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2023"

r = httpx.get(url)
#print(r.text)

in_array = r.text.split("\n")
#print(in_array)

radek_eur = ""
for line in r.text.split("\n"):
    if "|EUR|" in line:
        radek_eur = line

radek_array = radek_eur.split("|")
pprint(radek_array)

kurz_str = radek_array[-1]

kurz_str = kurz_str.replace(",", ".")

pprint(kurz_str)

#castka = input("Zadej castku v CZK: ")
#result = int(castka) * 25
#print(f"to je v eur: {result}")