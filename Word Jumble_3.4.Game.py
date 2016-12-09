import random

print("""
\t\t\t\t  Pogodite rec!
\t\tBroj pokusaja je onoliki kolika je duzina te reci!
\t\t\t  Imate jednom pravo na pomoc.
""")

print("""

Birajte kategoriju:

filmovi\t\t1
sport\t\t2
hrana\t\t3
imena\t\t4
""")

filmovi = ("spiderman","lucy")
sport = ("tenis","fudbal","rukomet","kosarka","odbojka")
hrana = ("pizza","hamburger","salata","sladoled")
imena = ("tamara","mihailo","relja","tara","luka")

while True:
    try:
        kategorija = int(input("\n>"))
        break
    except:
        print("Greska pri unosu kategorije, pokusajte ponovo!")
        
while True:
    if kategorija == 1:
        pogadjanje = random.choice(filmovi)
        break

    elif kategorija == 2:
        pogadjanje = random.choice(sport)
        break

    elif kategorija == 3:
        pogadjanje = random.choice(hrana)
        break

    elif kategorija == 4:
        pogadjanje = random.choice(imena)
        break
    
    else:
        kategorija = int(input("\nUnesite postojecu kategoriju: "))

izmesana_slova = ""

nova_rec = pogadjanje[:]

for i in nova_rec:
    duzina = len(nova_rec)
    pozicija = random.randrange(duzina)
    slovo = nova_rec[pozicija]
    izmesana_slova += slovo + " "
    nova_rec = nova_rec[:pozicija] + nova_rec[pozicija+1:]


print("\n" + izmesana_slova)

pomoc = pogadjanje[0]

duzina_pogadjanje = len(pogadjanje)

while duzina_pogadjanje > 0:

    while True:
        try:
            pogadjanje_reci = input("\n>")
            break
        except:
            print("Greska!")

    if pogadjanje_reci == "1":
        print("Rec pocinje slovom: ", pomoc)
        continue

    if pogadjanje == pogadjanje_reci.lower():
        print("Cestitamo! Pogodili ste rec!")
        break

    else:
        if duzina_pogadjanje == 1:
            print("Nemate vise pokusaja!")
        else:
            print("""
Pogresna rec! Pogadjajte opet!

Za pomoc pritisnite 1 !""")

    duzina_pogadjanje -= 1

input()
