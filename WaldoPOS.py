# Funksie om 'n item by die lys te voeg
def voeg_by_produkte(produkte, naam, prys):
    """Voeg 'n produk by die lys van produkte"""
    produkte.append((naam, prys))

# Funksie om die lys van produkte te vertoon
def vertoon_produkte(produkte):
    """Vertoon alle produkte en hul pryse"""
    totaal = 0
    print("\nProdukte in mandjie:")
    for produk in produkte:
        print(f"{produk[0]:<10} R{produk[1]:.2f}")
        totaal += produk[1]
    print("-" * 20)
    print(f"Totaal sonder my tip : R{totaal:.2f}\n")

# Funksie om die lys van produkte skoon te maak
def maak_mandjie_skoon(produkte):
    """Maak die lys van produkte skoon"""
    produkte.clear()
    print("Eish alles is nou weg\n")

# Hoofprogram
def main():
    produkte = []  # Lewer 'n leë lys om produkte in te stoor
    print("Welkom by my POS systeem")
    print("Gebruik 'klaar' om die program te verlaat.")

    while True:
        produk_naam = input("Gee produk se naam ('klaar' om te verlaat): ")

        if produk_naam.lower() == 'klaar':
            break

        try:
            produk_prys = float(input("Voer produkprys in: R"))
        except ValueError:
            print("Sorry hoor ons pryse lyk nie so nie. Probeer weer.\n")
            continue

        voeg_by_produkte(produkte, produk_naam, produk_prys)
        vertoon_produkte(produkte)

    print("Dankie vir jou geld!")

# Roep die hoofprogram funksie aan
if __name__ == "__main__":
    main()
