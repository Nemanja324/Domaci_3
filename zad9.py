class Turnir:
    def __init__(self):
        self.naziv_turnira = ''
        self.broj_rundi = 0
        self.lista_igraca = []

    def set_naziv_turnira(self, naziv):
        self.naziv_turnira = naziv

    def set_broj_rundi(self, broj_rundi):
        if 0 < broj_rundi < 10:
            self.broj_rundi = broj_rundi
        else:
            print('Runde moraju biti izmedju 0 i 10.')

    def set_lista_igraca(self, lista):
        self.lista_igraca = lista[:]

    def get_broj_rundi(self):
        return self.broj_rundi

    def get_naziv_turnira(self):
        return self.naziv_turnira

    def get_lista_igraca(self):
        return self.lista_igraca

    def dodaj_igraca(self, ime):
        self.lista_igraca.append((ime, 0))

    def obrisi_igraca(self, ime):
        for i in range(len(self.lista_igraca)):
            if self.lista_igraca[i][0] == ime:
                self.lista_igraca[i] = 0
        self.lista_igraca.remove(0)

    def prikazi_najboljeg_igraca(self):
        i = 0
        maxi = -1
        for j in range(len(self.lista_igraca)):
            if self.lista_igraca[j][1] > maxi:
                i = j
        print(f'Najbolji igrac je: {self.lista_igraca[i][0]}')

