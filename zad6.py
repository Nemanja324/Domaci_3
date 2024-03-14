class Televizor:
    def __init__(self, broj_tk=0, naziv_tk='Nepoznat', jacina_tona=0):
        self.kanali = []
        self.broj_tk = broj_tk
        self.naziv_tk = naziv_tk
        if jacina_tona < 0 or jacina_tona > 10:
            print('Jacina tona koju ste unijeli nije u dobrom opsegu!')
        else:
            self.jacina_tona = jacina_tona

    def set_kanali(self, novi_kanali):
        if novi_kanali:
            self.kanali = novi_kanali[:]

    def set_broj_tk(self, novi_broj_tk):
        if 0 <= novi_broj_tk <= len(self.kanali):
            self.broj_tk = novi_broj_tk
        else:
            print(f'Unijeti broj kanala nije u sklopu postojecih kanala{novi_broj_tk}')

    def set_naziv_tk(self, novi_naziv_tk):
        if novi_naziv_tk:
            self.kanali.append(novi_naziv_tk)
        else:
            print(f'Unijeti naziv kanala nije u sklopu postojecih kanala{novi_naziv_tk}')

    def set_jacina_tona(self, nova_jacina):
        if 0 <= nova_jacina <= 10:
            self.jacina_tona = nova_jacina
        else:
            print('Jacina tona koju ste unijeli nije u dobrom opsegu!')

    def get_kanali(self):
        return self.kanali

    def get_broj_tk(self):
        return self.broj_tk

    def get_naziv_tk(self):
        return self.naziv_tk

    def get_jacina_tona(self):
        return self.jacina_tona

    def dodaj_kanal(self, naziv_kanala):
        if naziv_kanala:
            self.kanali.append(naziv_kanala)

    def obrisi_kanal(self, naziv_kanala):
        if naziv_kanala and naziv_kanala in self.kanali:
            self.kanali.remove(naziv_kanala)

    def pojacaj_ton(self):
        self.jacina_tona += 1

    def ime_kanala(self, broj_kanala):
        if broj_kanala:
            return self.kanali[broj_kanala]


obj1 = Televizor(5, 'Pink', 6)
print(obj1.jacina_tona)

obj1.set_kanali(['Vijesti', 'Pink', 'Rtcg', 'Ultra', 'Dizni'])
print(obj1.get_kanali())
print(obj1.obrisi_kanal('Vijesti'))
print(obj1.get_kanali())
