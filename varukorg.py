from typing import List

class produkter:
    def __init__(self, namn: str, pris: float):
        self.namn = namn
        self.pris = pris

class varukorg:
    def __init__(self):
        self.tillagda_produkter: list[produkter] = []
        self.summa = 0

    def lägg_till_produkter(self, produkt: produkter):
        self.tillagda_produkter.append(produkt)
        self.summa += produkt.pris

    def total_pris(self):
        return self.summa


korg = varukorg()

ägg = produkter("ägg",12.99)
smör = produkter("smör",26.99)

korg.lägg_till_produkter(ägg)
korg.lägg_till_produkter(smör)

print(korg.total_pris())