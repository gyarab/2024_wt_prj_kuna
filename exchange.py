import httpx

def get_exchange_rate():
    url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
    try:
        r = httpx.get(url)
        r.raise_for_status()
        
        for line in r.text.split("\n"):
            if "|EUR|" in line: 
                parts = line.split("|")
                rate = parts[-1].replace(",", ".")
                return float(rate)
    except Exception as e:
        print("Chyba při načítání kurzu:", e)
        return None

def convert_currency(amount, rate, direction):
    if rate is None:
        print("Nelze převádět bez platného kurzu.")
        return None
    
    if direction.lower() == "eur na czk":
        return amount * rate
    elif direction.lower() == "czk na eur":
        return amount / rate
    else:
        print("Neplatný směr převodu.")
        return None

def main():
    print("Ted ti prevedu meny!")
    rate = get_exchange_rate()
    
    if rate is None:
        print("Nepodařilo se získat kurz, ukončuji program.")
        return
    
    print("Aktuální kurz EUR/CZK je:", rate)
    
    while True:
        direction = input("EUR na CZK nebo CZK na EUR?(nebo exit)").strip()
        if direction.lower() == "exit":
            break
        try:
            amount = float(input("Zadejte částku: ").replace(",", "."))
            converted = convert_currency(amount, rate, direction)
            if converted is not None:
                print(f"Výsledná částka: {converted:.2f}")
        except ValueError:
            print("Neplatný vstup, zadejte číslo.")

if __name__ == "__main__":
    main()