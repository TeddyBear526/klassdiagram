from typing import List

class produkter:
    def __init__(self, namn: str, pris: float):
        self.namn = namn
        self.pris = pris

class varukorg:
    def __init__(self):
        self.tillagda_produkter: list[produkter] = []

    def lägg_till_produkter(self, produkt: produkter):
        self.tillagda_produkter.append(produkt)

    def räkna_pris(self):
        return list[produkter]


korg = varukorg()

ägg = produkter("ägg",12.99)
smör = produkter("smör",26.99)

korg.lägg_till_produkter(ägg)
korg.lägg_till_produkter(smör)

korg.räkna_pris()