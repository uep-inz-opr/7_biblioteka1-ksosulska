class Biblioteka:

 def __init__ (self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.ilosc = 0

 def dodaj_ksiazke(self, tytul, autor, rok):
   ksiazki = []
   ksiazki.append({"autor": autor, "tytuł": tytul, "rok": rok})

 def __repr__(self):
        return "'" + self.autor + "', " + str(self.ilosc)


biblio = {}
n = int(input())
for i in range(n):
    ks = eval(input())
    tytul = ks[0]
    autor = ks[1]
    rok = ks[2]
    if tytul in biblio:
        biblio[tytul].ilosc += 1
    else:
        biblio[tytul] = Biblioteka(tytul, autor, rok)

print(biblio)
