class Biblioteka:
  def __init__(self):
    self.limit_wypozyczen = 3
    self.egzemplarze =[]
    self.ksiazki = []

  def dodaj(self, tytul, autor, rok_wydania):
    ksiazka = Ksiazka(tytul, autor)
    egzemplarz = Egzemplarz(ksiazka, rok_wydania)

    self.egzemplarze.append(egzemplarz)

    for k in self.ksiazki:
      if k.tytul == tytul and k.autor ==autor:
        k.liczba += 1
        return
  
    
    self.ksiazki.append(ksiazka)

    

  class Ksiazka:
    def __init__(self, tytul, autor):
      self.tytul = tytul
      self.autor = autor
      self.liczba = 1 

    def __repr__(self):
      return repr((self.tytul, self.autor,self.liczba))

  class Egzemplarz:
    def __init__(self, ksiazka, rok_wydania):
      self.ksiazka = ksiazka
      self.rok_wydania = rok_wydania
      self.wypozyczony = False

    def __repr__(self):
      return repr((self.ksiazka.tytul, self.ksiazka.autor, self.rok_wydania))

b = Biblioteka()
n = int(input())

for i in range(0, n):
    k=eval(input())
    b.dodaj(k[0], k[1], k[2])

b.ksiazki.sort(key=lambda x: x.tytul)

for ksiazka in b.ksiazki:
  print(ksiazka)


print(b.egzemplarze)